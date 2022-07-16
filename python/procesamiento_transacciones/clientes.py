from cuenta import *
from direccion import Direccion

CARACTERISTICAS_CLASSIC = {
    'limite_chequeras': -1,
    'limite_tajetas_credito': -1,
    'cuenta_en_dolares': False,
    'caracteristicas_cuenta': {
        'limite_extraccion_diario': 10000,
        'limite_transferencia_recibida': 50000,
        'costo_transferencias': 0.01,
        'saldo_descubierto_disponible': 0
    }
}
CARACTERISTICAS_GOLD = {
    'limite_chequeras': 1,
    'limite_tajetas_credito': 1,
    'cuenta_en_dolares': True,
    'caracteristicas_cuenta': {
        'limite_extraccion_diario': 20000,
        'limite_transferencia_recibida': 500000,
        'costo_transferencias': 0.005,
        'saldo_descubierto_disponible': 10000
    }
}
CARACTERISTICAS_BLACK = {
    'limite_chequeras': 2,
    'limite_tajetas_credito': 5,
    'cuenta_en_dolares': True,
    'caracteristicas_cuenta': {
        'limite_extraccion_diario': 100000,
        'limite_transferencia_recibida': -1,
        'costo_transferencias': 0,
        'saldo_descubierto_disponible': 10000
    }
}


class Cliente:
    def __init__(self, nombre, apellido, numero, dni, direccion, tier, caracteristicas):
        self._nombre = nombre
        self._apellido = apellido
        self._numero = numero
        self._dni = dni
        self._tier = tier
        self._cuenta = Cuenta(*caracteristicas['caracteristicas_cuenta'].values())
        self._limite_chequeras = caracteristicas['limite_chequeras']
        self._limite_tarjetas = caracteristicas['limite_tajetas_credito']
        self._cantidad_de_tarjetas_credito = 0
        self._cantidad_de_chequeras = 0
        self._cuenta_en_dolares = caracteristicas['cuenta_en_dolares']

        if direccion:
            self._direccion = Direccion(*direccion.values())
        else:
            self._direccion = None

    def get_numero(self):
        return self._numero

    def get_cuenta(self):
        return self._cuenta

    def set_cantidad_de_tarjetas_credito(self, cantidad):
        self._cantidad_de_tarjetas_credito = cantidad

    def set_cantidad_de_chequeras(self, cantidad):
        self._cantidad_de_chequeras = cantidad

    def get_cantidad_de_chequeras(self):
        return self._cantidad_de_chequeras

    def get_cantidad_de_tarjetas_credito(self):
        return self._cantidad_de_tarjetas_credito

    def get_tier(self):
        return self._tier

    def puede_crear_chequera(self):
        return self._limite_chequeras != -1 and self._cantidad_de_chequeras < self._limite_chequeras

    def puede_crear_tarjeta_credito(self):
        return self._limite_tarjetas != -1 and self._cantidad_de_tarjetas_credito < self._limite_tarjetas

    def puede_comprar_dolar(self):
        return self._cuenta_en_dolares

    def __str__(self):
        return f"Tier: {self._tier} \nNombre: {self._nombre} \nApellido: {self._apellido} \nNumero: {self._numero} \nDNI: {self._dni} \n{'Direccion: ' + str(self._direccion) if self._direccion else ''}"


class Classic(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion=None):
        super().__init__(nombre, apellido, numero, dni, direccion, 'CLASSIC', CARACTERISTICAS_CLASSIC)


class Gold(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion=None):
        super().__init__(nombre, apellido, numero, dni, direccion, 'GOLD', CARACTERISTICAS_GOLD)
        


class Black(Cliente):
    def __init__(self, nombre, apellido, numero, dni, direccion=None):
        super().__init__(nombre, apellido, numero, dni, direccion, 'BLACK', CARACTERISTICAS_BLACK)
        



