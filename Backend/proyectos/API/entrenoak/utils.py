from enum import IntEnum

class TiposAlertas(IntEnum):
    SEGURO = 1
    CALOR = 2
    FRIO = 3
    MAL_TIEMPO = 4
    OTROS = 5

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

class TiposEstados(IntEnum):
    BORRADOR = 1 #La intención es que cuando se quede a medias se guarde como borrador.
    PUBLICADO = 2 #Lo ven todos los miembros del equipo (a lo mejor se puede plantear una especie de red social y que lo vean todos los usuarios)
    OCULTO = 3 #El usuario puede ocultar el entrenamiento de manera que lo visualiza como si lo hubiera publicado pero solo en su perfil.

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
