class Cuenta:
    def __init__(self, limite_extraccion_diario, limite_transferencia_recibida, costo_transferencias, saldo_descubierto_disponible):
        self.__limite_extraccion_diario = limite_extraccion_diario
        self.__limite_transferencia_recibida = limite_transferencia_recibida
        self.__monto = 0
        self.__costo_transferencias = costo_transferencias
        self.__saldo_descubierto_disponible = saldo_descubierto_disponible
        self.__cupo_diario_restante = 0

    def get_limite_extraccion_diario(self):
        return self.__limite_extraccion_diario

    def get_limite_transferencia_recibida(self):
        return self.__limite_transferencia_recibida

    def get_monto(self):
        return self.__monto
    
    def set_monto(self, monto):
        self.__monto = monto

    def get_costo_transferencias(self):
        return self.__costo_transferencias
    
    def get_cupo_diario_restante(self):
        return self.__cupo_diario_restante

    def set_cupo_diario_restante(self, cupo_diario_restante):
        self.__cupo_diario_restante = cupo_diario_restante
        
    def get_saldo_descubierto_disponible(self):
        return self.__saldo_descubierto_disponible

    def __str__(self):
        return f"{self.__monto} {self.__limite_extraccion_diario} {self.__limite_transferencia_recibida} {self.__costo_transferencias} {self.__saldo_descubierto_disponible}"


