from graphene import InputObjectType
from graphene.types.scalars import ID
from graphene.types.scalars import String

# Create your inputs types here.


class CreateRoomInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la creación del cuarto de juego
    """

    code = String(required=True)


class UpdateRoomInput(InputObjectType):
    """
    Clase que encapsula los datos necesarios
    para la actualización del cuarto de juego
    """

    id = ID(required=True)
    code = String()
