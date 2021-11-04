from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String

# Create your inputs types here.


class CreatePlayerInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación del jugador
    """

    active = String(required=True)
    board = String(required=True)

    # Relaciones
    user_id = ID(required=True)


class UpdatePlayerInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización del jugador
    """

    id = ID(required=True)
    active = String()
    board = String()

    # Relaciones
    room_id = ID()
