from enum import Enum

class OrderStatus(Enum):
    CREATED = 'Creado'
    PAYED = 'Pagado'
    COMPLETED = 'Completado'
    CANCELED = 'Cancelado'

choices = [(item.value, item.value) for item in OrderStatus]