from graphene import ObjectType
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField

from .data.room.types import RoomNode
from .data.player.types import PlayerNode
from .data.player.mutations import(
    CreatePlayer,
    UpdatePlayer,
    DeletePlayer
)
from .data.room.mutations import(
    CreateRoom,
    UpdateRoom,
    DeleteRoom
)

class Query(ObjectType):
    """Endpoint para consultar registros"""

    room = Node.Field(RoomNode)
    player = Node.Field(PlayerNode)
    all_rooms = DjangoFilterConnectionField(RoomNode)
    all_players = DjangoFilterConnectionField(PlayerNode)


class Mutation(ObjectType):
    """Endpoint para crear, actualizar y eliminar registros"""

    create_player = CreatePlayer.Field()
    update_player = UpdatePlayer.Field()
    delete_player = DeletePlayer.Field()

    create_room = CreateRoom.Field()
    update_room = UpdateRoom.Field()
    delete_room = DeleteRoom.Field()
