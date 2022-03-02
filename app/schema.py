import graphene
from django.db.models import Q
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from graphql_relay.node.node import from_global_id

from .models import Planet, People, Film, Director, Producer
from .mutations import UpdateOrCreatePlanet
from .types import PlanetType, PeopleType, FilmType, DirectorType, ProducerType


class Query(graphene.ObjectType):
    planet = graphene.relay.Node.Field(PlanetType)
    all_planets = DjangoFilterConnectionField(PlanetType)
    film = graphene.relay.Node.Field(FilmType)
    all_films = DjangoFilterConnectionField(FilmType)

    director = graphene.relay.Node.Field(DirectorType)
    all_directors = DjangoFilterConnectionField(DirectorType)

    producer = graphene.relay.Node.Field(ProducerType)
    all_producers = DjangoFilterConnectionField(ProducerType)

    people = graphene.relay.Node.Field(PeopleType)
    all_people = DjangoFilterConnectionField(PeopleType,
                                             GENDER=graphene.String())

    """ fILTRADO POR LOS VALORES DE GENERO"""
    def resolve_all_people(root, info, GENDER):
            return People.object.filter(G=GENDER)


schema = graphene.Schema(query=Query)


class Mutation(graphene.ObjectType):
    add_planet_mutation = UpdateOrCreatePlanet.Field()
