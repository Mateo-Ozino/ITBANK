class Razon:
    def __init__(self):
        self._mensaje = " "

    def get_mensaje(self):
        return self._mensaje

    def resolver(self, cliente, transaccion):
        pass

class RazonAltaChequera(Razon):
    def resolver(self, cliente, transaccion):
        if not cliente.puede_crear_chequera():
            if cliente.get_cantidad_de_chequeras() == 0:
                self._mensaje = f"El cliente {cliente.get_tier()} no puede poseer chequeras."
            else:
                self._mensaje = f"El cliente {cliente.get_tier()} no puede poseer mas de {cliente.get_cantidad_de_chequeras()} chequeras."
        else:
            self._mensaje = "ERROR: razon desconocida. Incosistencia en los datos del archivo."


class RazonAltaTarjetaCredito(Razon):
    def resolver(self, cliente, transaccion):
        if not cliente.puede_crear_tarjeta_credito():
            if cliente.get_cantidad_de_tarjetas_credito() == 0:
                self._mensaje = f"El cliente {cliente.get_tier()} no puede poseer tarjetas de credito."
            else:
                self._mensaje = f"El cliente {cliente.get_tier()} no puede poseer mas de {cliente.get_cantidad_de_tarjetas_credito()} tarjetas de credito."
        else:
            self._mensaje = "ERROR: razon desconocida. Incosistencia en los datos del archivo."
        

class RazonCompraDolar(Razon):
    def resolver(self, cliente, transaccion):
        if not cliente.puede_comprar_dolar():
            self._mensaje = f"El cliente {cliente.get_tier()} no puede comprar dólares."
        elif transaccion['monto'] > cliente.get_cuenta().get_monto():
            self._mensaje = f"El cliente {cliente.get_tier()} no puede comprar dólares por ${transaccion['monto']}. Saldo insuficiente."        
        else:
            self._mensaje = "ERROR: razon desconocida. Incosistencia en los datos del archivo."


class RazonRetiroEfectivo(Razon):
    def resolver(self, cliente, transaccion):
        if cliente.get_cuenta().get_cupo_diario_restante() <= transaccion['monto']:
            self._mensaje = f"El cliente {cliente.get_tier()} no puede retirar ${transaccion['monto']}. Cupo diario de extracción insuficiente."
        elif cliente.get_cuenta().get_monto() + cliente.get_cuenta().get_saldo_descubierto_disponible() <= transaccion['monto']:
            self._mensaje = f"El cliente {cliente.get_tier()} no puede retirar ${transaccion['monto']}. Saldo insuficiente."
        else:
            self._mensaje = "ERROR: razon desconocida. Incosistencia en los datos del archivo."

class RazonTransferenciaEnviada(Razon):
    def resolver(self, cliente, transaccion):
        if cliente.get_cuenta().get_monto() + cliente.get_cuenta().get_saldo_descubierto_disponible() <= transaccion['monto']*(1 + cliente.get_cuenta().get_costo_transferencias()):
            self._mensaje = f"El cliente {cliente.get_tier()} no puede transferir ${transaccion['monto']}. Saldo insuficiente."
        else:
            self._mensaje = "ERROR: razon desconocida. Incosistencia en los datos del archivo."

class RazonTransferenciaRecibida(Razon):
    def resolver(self, cliente, transaccion):
        if cliente.get_cuenta().get_limite_transferencia_recibida() != -1 and transaccion['monto'] > cliente.get_cuenta().get_limite_transferencia_recibida():
            self._mensaje = f"El cliente {cliente.get_tier()} no puede recibir ${transaccion['monto']}. Se ha superado el limite de transferencia y no ha recibido ninguna autorización."
        else:
            self._mensaje = "ERROR: razon desconocida. Incosistencia en los datos del archivo."

