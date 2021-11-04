from django.db.models import Model
from django.db.models import CharField
from django.db.models import BooleanField
from django.db.models import JSONField
from django.db.models import ForeignKey
from django.db.models import CASCADE

# Create your models here.


class Room(Model):
    """"Clase que representa una Cuarto de Juego"""

    code = CharField(max_length=45, help_text="código hexadecimal")

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """
        return self.code


class Player(Model):
    """"Clase que representa un Jugador"""

    active = BooleanField(help_text="usuario activo")
    board = JSONField(help_text="tablero")

    # Relations
    room = ForeignKey(
        Room,
        related_name='players',
        on_delete=CASCADE,
        help_text='cuarto de juego'
    )

    def __str__(self) -> str:
        """
        Función que representa al objeto
        cuando es recuperado
        """
        return str(self.active)
