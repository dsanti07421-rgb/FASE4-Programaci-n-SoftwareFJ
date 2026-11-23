"""
Archivo principal de ejecución y simulación del Sistema Integral de Gestión
de Clientes, Servicios y Reservas - Software FJ (Fase 4 - UNAD).
Simula 12 operaciones completas (válidas e inválidas) demostrando estabilidad
y manejo avanzado de excepciones sin bases de datos.
"""
from logger import RegistradorLogs
from cliente import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ErrorSistemaFJ

def ejecutar_simulacion() -> None:
    logger = RegistradorLogs("sistema_fj.log")
    clientes = []
    servicios = []
    reservas = []

    print("=" * 75)
    print("INICIANDO SIMULACIÓN DEL SISTEMA DE GESTIÓN - SOFTWARE FJ")
    print("=" * 75)
    logger.registrar_evento("INFO", "Main", "Inicio de simulación de 12 operaciones del sistema.")

    # OPERACIÓN 1: Registro válido de Cliente 1
    try:
        c1 = Cliente("CLI-01", "Laura Martínez", "laura.martinez@correo.com", "3104567890")
        clientes.append(c1)
        logger.registrar_evento("INFO", "Clientes", f"Registrado: {c1.obtener_resumen()}")
        print(f"[OP 01 - ÉXITO] {c1.obtener_resumen()}")
    except ErrorSistemaFJ as e:
        print(f"[OP 01 - ERROR] {e}")

    # OPERACIÓN 2: Registro válido de Cliente 2
    try:
        c2 = Cliente("CLI-02", "Carlos Gómez", "carlos.gomez@empresa.co", "3209876543")
        clientes.append(c2)
        logger.registrar_evento("INFO", "Clientes", f"Registrado: {c2.obtener_resumen()}")
        print(f"[OP 02 - ÉXITO] {c2.obtener_resumen()}")
    except ErrorSistemaFJ as e:
        print(f"[OP 02 - ERROR] {e}")

    # OPERACIÓN 3: Registro inválido de Cliente (correo mal formado)
    try:
        c_invalido = Cliente("CLI-03", "Pedro Pérez", "pedro_sin_arroba.com", "3001112233")
        clientes.append(c_invalido)
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", "Clientes", f"Fallo esperado en OP 03 ({e.codigo_error}): {e}")
        print(f"[OP 03 - CONTROLADO] Excepción capturada ({e.codigo_error}): {e}")

    # OPERACIÓN 4: Registro inválido de Cliente (ID vacío -> encadenamiento)
    try:
        c_sin_id = Cliente("", "Ana Rojas", "ana@correo.com", "3112223344")
        clientes.append(c_sin_id)
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", "Clientes", f"Fallo esperado en OP 04 ({e.codigo_error}): {e}")
        print(f"[OP 04 - CONTROLADO] Excepción encadenada ({e.codigo_error}): {e}")

    # OPERACIÓN 5: Creación válida de Servicio 1 (Sala)
    try:
        s1 = ReservaSala("SRV-01", "Sala Innovación Norte", 80000.0, capacidad=15)
        servicios.append(s1)
        logger.registrar_evento("INFO", "Servicios", f"Creado: {s1.describir_servicio()}")
        print(f"[OP 05 - ÉXITO] {s1.describir_servicio()}")
    except ErrorSistemaFJ as e:
        print(f"[OP 05 - ERROR] {e}")

    # OPERACIÓN 6: Creación válida de Servicio 2 (Equipo)
    try:
        s2 = AlquilerEquipo("SRV-02", "Servidor Rack Dell", 120000.0, gama="servidor")
        servicios.append(s2)
        logger.registrar_evento("INFO", "Servicios", f"Creado: {s2.describir_servicio()}")
        print(f"[OP 06 - ÉXITO] {s2.describir_servicio()}")
    except ErrorSistemaFJ as e:
        print(f"[OP 06 - ERROR] {e}")

    # OPERACIÓN 7: Creación válida de Servicio 3 (Asesoría)
    try:
        s3 = AsesoriaEspecializada("SRV-03", "Arquitectura Cloud y Seguridad", 150000.0, area_tecnica="Ciberseguridad")
        servicios.append(s3)
        logger.registrar_evento("INFO", "Servicios", f"Creado: {s3.describir_servicio()}")
        print(f"[OP 07 - ÉXITO] {s3.describir_servicio()}")
    except ErrorSistemaFJ as e:
        print(f"[OP 07 - ERROR] {e}")

    # OPERACIÓN 8: Creación inválida de Servicio (tarifa negativa)
    try:
        s_invalido = ReservaSala("SRV-04", "Sala Defectuosa", -50000.0, capacidad=10)
        servicios.append(s_invalido)
    except ErrorSistemaFJ as e:
        logger.registrar_evento("ERROR", "Servicios", f"Fallo esperado en OP 08 ({e.codigo_error}): {e}")
        print(f"[OP 08 - CONTROLADO] Excepción capturada ({e.codigo_error}): {e}")

    # OPERACIÓN 9: Reserva exitosa con descuento e IVA (Sobrecarga de parámetros)
    try:
        r1 = Reserva("RES-01", clientes[0], servicios[0], duracion_horas=5, logger=logger)
        total_r1 = r1.procesar_y_confirmar(descuento=0.10, aplicar_iva=True)
        reservas.append(r1)
        print(f"[OP 09 - ÉXITO] {r1.obtener_resumen()}")
    except ErrorSistemaFJ as e:
        print(f"[OP 09 - ERROR] {e}")

    # OPERACIÓN 10: Reserva fallida (intento de reservar la misma sala ya ocupada)
    try:
        r2 = Reserva("RES-02", clientes[1], servicios[0], duracion_horas=2, logger=logger)
        r2.procesar_y_confirmar()
        reservas.append(r2)
    except ErrorSistemaFJ as e:
        print(f"[OP 10 - CONTROLADO] Excepción capturada ({e.codigo_error}): {e}")

    # OPERACIÓN 11: Reserva fallida por descuento inconsistente (encadenamiento)
    try:
        r3 = Reserva("RES-03", clientes[1], servicios[1], duracion_horas=3, logger=logger)
        r3.procesar_y_confirmar(descuento=1.5)  # Descuento > 100% inválido
        reservas.append(r3)
    except ErrorSistemaFJ as e:
        print(f"[OP 11 - CONTROLADO] Excepción encadenada ({e.codigo_error}): {e}")

    # OPERACIÓN 12: Reserva exitosa de asesoría sin IVA y posterior cancelación controlada
    try:
        r4 = Reserva("RES-04", clientes[1], servicios[2], duracion_horas=2, logger=logger)
        r4.procesar_y_confirmar(descuento=0.05, aplicar_iva=False)
        reservas.append(r4)
        print(f"[OP 12 - ÉXITO] {r4.obtener_resumen()}")
        r4.cancelar()
        print(f"[OP 12b - CANCELACIÓN] {r4.obtener_resumen()}")
    except ErrorSistemaFJ as e:
        print(f"[OP 12 - ERROR] {e}")

    print("=" * 75)
    print(f"SIMULACIÓN FINALIZADA SIN INTERRUPCIONES.")
    print(f"Clientes válidos: {len(clientes)} | Servicios activos: {len(servicios)} | Reservas registradas: {len(reservas)}")
    print("Todos los eventos y errores fueron guardados en 'sistema_fj.log'.")
    print("=" * 75)
    logger.registrar_evento("INFO", "Main", "Fin de la simulación. Ejecución estable completada.")

if __name__ == "__main__":
    ejecutar_simulacion()
