import graphene
from graphql_relay import from_global_id

from .models import Planet, People
from .types import PlanetType, PeopleType
from .utils import generic_model_mutation_process


class UpdateOrCreatePlanet(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        rotation_period = graphene.String(required=False)
        orbital_period = graphene.String(required=False)
        diameter = graphene.String(required=False)
        climate = graphene.String(required=False)
        gravity = graphene.String(required=False)
        terrain = graphene.String(required=False)
        surface_water = graphene.String(required=False)
        population = graphene.String(required=False)

    planet = graphene.Field(PlanetType)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        raw_id = input.get('id', None)

        data = {'model': Planet, 'data': input}
        if raw_id:
            data['id'] = from_global_id(raw_id)[1]

        planet = generic_model_mutation_process(**data)
        return UpdateOrCreatePlanet(planet=planet)


class AddPeople(graphene.relay.ClientIDMutation):
    class Input:
        id = graphene.ID(required=False)
        name = graphene.String(required=True)
        height = graphene.String(required=False)
        mass = graphene.String(required=False)
        hair_color = graphene.String(required=False)
        skin_color = graphene.String(required=False)
        eye_color = graphene.String(required=False)
        birth_year = graphene.String(required=False)
        gender = graphene.String(required=False)

        home_world_id = graphene.ID(required=True)

    people = graphene.Field(PeopleType)

    @classmethod
    def mutate_and_get_payload(cls, args, context, **kwargs):
        raw_id = kwargs.get('id', None)

        kw = {'model': People, 'data': kwargs}
        if raw_id:
            kw['id'] = from_global_id(raw_id)[1]
        people = generic_model_mutation_process(**kw)
        return AddPeople(people=people)
