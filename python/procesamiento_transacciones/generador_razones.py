from razones import *

TIPO_TRANSACCION = {'RETIRO_EFECTIVO_CAJERO_AUTOMATICO': 0, 'ALTA_TARJETA_CREDITO': 1,
                    'ALTA_CHEQUERA': 2, 'COMPRA_DOLAR': 3, 'TRANSFERENCIA_ENVIADA': 4, 'TRANSFERENCIA_RECIBIDA': 5}

def crear_razon(cliente, transaccion):
    if transaccion['estado'] == 'ACEPTADA':
        return None
    
    cliente.set_cantidad_de_tarjetas_credito(int(transaccion['totalTarjetasDeCreditoActualmente']))
    cliente.set_cantidad_de_chequeras(int(transaccion['totalChequerasActualmente']))

    cuenta = cliente.get_cuenta()
    cuenta.set_monto(int(transaccion['saldoEnCuenta']))
    cuenta.set_cupo_diario_restante(int(transaccion['cupoDiarioRestante']))

    
    match TIPO_TRANSACCION[transaccion['tipo']]:
        case 0:
            razon = RazonRetiroEfectivo()
        case 1:
            razon = RazonAltaTarjetaCredito()
        case 2:
            razon = RazonAltaChequera()
        case 3:
            razon = RazonCompraDolar()
        case 4:
            razon = RazonTransferenciaEnviada()
        case 5:
            razon = RazonTransferenciaRecibida()
    
    razon.resolver(cliente, transaccion)
    return razon
