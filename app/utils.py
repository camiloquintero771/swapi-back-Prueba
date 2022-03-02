def generic_model_mutation_process(model, data, id=None, commit=True):
    """
        La función crea y actualiza objetos utilizando los siguientes
        parametros

        model: Model de Django:.
        data: Dict con los fields para el objeto a creat/actualizar.
        id: Int para buscar el objeto a actualizar
        commit: Indica si se debe guardar el objeto.
        model instance.

        ACTUALIZAR Si el atributo de clave principal del objeto se establece en un
         valor que se evalúa como True (es decir esxite en la base de datos).

        CREAR si el atributo de clave principal del objeto no está configurado o
         si la ACTUALIZACIÓN no actualizó nada (por ejemplo, si la clave principal
         está configurada no existe en la base de datos).
         Crea un nuevo objeto con las ** kwargs (data),
         guardandolo en la base de datos y retornando el objeto creado.

        No tiene restriccion alguna en el uso de la funcion.
    """
    if id:
        item = model.objects.get(id=id)
        try:
            del data['id']
        except KeyError:
            pass

        for field, value in data.items():
            setattr(item, field, value)
    else:
        item = model(**data)

    if commit:
        item.save()

    return item
