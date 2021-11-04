from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from game.models import Player

# Create your objects types here.


class PlayerNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Player
        filter_fields = {
            'active': ['exact'],
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
