from graphene import Field, Mutation
from graphene.types.scalars import ID
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from api_graphql.data.room.inputs import CreateRoomInput, UpdateRoomInput
from api_graphql.data.room.types import RoomNode
from api_graphql.utils import delete_attributes_none, transform_global_ids
from game.models import Room

# Create your mutations here


class CreateRoom(Mutation):
    """Clase para crear cuarto de juego"""

    room = Field(RoomNode)

    class Arguments:
        input = CreateRoomInput(required=True)

    def mutate(self, info, input: CreateRoomInput):
        input = delete_attributes_none(**vars(input))
        room = Room.objects.create(**input)

        return CreateRoom(room=room)


class UpdateRoom(Mutation):
    """Clase para actualizar cuarto de juego"""

    room = Field(RoomNode)

    class Arguments:
        input = UpdateRoomInput(required=True)

    def mutate(self, info, input: UpdateRoomInput):
        # Elimina nulos y transforma el id
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Room.objects.filter(pk=input.get('id')).update(**input)
        room = Room.objects.get(pk=input.get('id'))

        return UpdateRoom(room=room)


class DeleteRoom(Mutation):
    """Clase para eliminar cuarto de juego"""

    room = Field(RoomNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        # Transforma el id
        input = from_global_id(input)[1]

        try:
            room = Room.objects.get(pk=input)
            Room.objects.filter(pk=input).delete()
        except Room.DoesNotExist:
            raise GraphQLError('Room does not delete')

        return DeleteRoom(room=room)
