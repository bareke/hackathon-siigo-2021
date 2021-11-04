from graphene.relay import Node
from graphene_django import DjangoObjectType

from api_graphql.connections import TotalCountConnection
from game.models import Room

# Create your objects types here.


class RoomNode(DjangoObjectType):
    """
    Clase que representa el componente básico que se utiliza
    para definir la relación entre los campos del esquema
    y cómo se recuperan los datos.
    """

    class Meta:
        model = Room
        filter_fields = {
            'code': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection
