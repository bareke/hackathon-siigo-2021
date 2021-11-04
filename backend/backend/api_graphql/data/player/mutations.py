from graphene import Field, Mutation
from graphene.types.scalars import ID
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from api_graphql.data.player.inputs import CreatePlayerInput, UpdatePlayerInput
from api_graphql.data.player.types import PlayerNode
from api_graphql.utils import delete_attributes_none, transform_global_ids
from game.models import Player

# Create your mutations here


class CreatePlayer(Mutation):
    """Clase para crear jugador"""

    player = Field(PlayerNode)

    class Arguments:
        input = CreatePlayerInput(required=True)

    def mutate(self, info, input: CreatePlayerInput):
        input = delete_attributes_none(**vars(input))
        player = Player.objects.create(**input)

        return CreatePlayer(player=player)


class UpdatePlayer(Mutation):
    """Clase para actualizar jugador"""

    player = Field(PlayerNode)

    class Arguments:
        input = UpdatePlayerInput(required=True)

    def mutate(self, info, input):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Player.objects.filter(pk=input.get('id')).update(**input)
        player = Player.objects.get(pk=input.get('id'))

        return UpdatePlayer(player=player)


class DeletePlayer(Mutation):
    """Clase para eliminar jugador"""

    player = Field(PlayerNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        # Transforma el id
        input = from_global_id(input)[1]

        try:
            player = Player.objects.get(pk=input)
            Player.objects.filter(pk=input).delete()
        except Player.DoesNotExist:
            raise GraphQLError('Player does not delete')

        return DeletePlayer(player=player)
