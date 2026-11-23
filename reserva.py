"""
Módulo de gestión de reservas de Software FJ.
Implementa bloques try/except/else/finally, control de estados y encadenamiento de excepciones.
"""
from modelos_base import EntidadSistema, Servicio
from cliente import Cliente
from excepciones import ReservaInvalidaError, ServicioNoDisponibleError, CalculoInconsistenteError
from logger import RegistradorLogs

class Reserva(EntidadSistema):
    """Integra un Cliente, un Servicio y una duración bajo control transaccional."""
    ESTADOS_VALIDOS = ("PENDIENTE", "CONFIRMADA", "CANCELADA")

    def __init__(self, id_reserva: str, cliente: Cliente, servicio: Servicio, duracion_horas: int, logger: RegistradorLogs):
        super().__init__(id_reserva)
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("Se requiere una instancia válida de Cliente para reservar.")
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("Se requiere una instancia válida de Servicio para reservar.")
        if not isinstance(duracion_horas, int) or duracion_horas <= 0:
            raise ReservaInvalidaError("La duración de la reserva debe ser un número entero mayor a 0.")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion_horas = duracion_horas
        self.estado = "PENDIENTE"
        self.costo_total = 0.0
        self.logger = logger

    def procesar_y_confirmar(self, descuento: float = 0.0, aplicar_iva: bool = True) -> float:
        """
        Procesa el costo y confirma la reserva demostrando bloques
        try / except / else / finally y encadenamiento de excepciones.
        """
        try:
            if self.estado == "CANCELADA":
                raise ReservaInvalidaError(f"La reserva {self.id_entidad} ya fue cancelada y no puede confirmarse.")
            if self.estado == "CONFIRMADA":
                raise ReservaInvalidaError(f"La reserva {self.id_entidad} ya se encuentra confirmada.")
            if not self.servicio.disponible:
                raise ServicioNoDisponibleError(f"El servicio '{self.servicio.nombre}' no está disponible actualmente.")

            # Cálculo polimórfico del costo
            costo_calculado = self.servicio.calcular_costo(
                duracion_horas=self.duracion_horas,
                descuento=descuento,
                aplicar_iva=aplicar_iva
            )
        except CalculoInconsistenteError as err_calc:
            # Encadenamiento de excepción de cálculo hacia error de reserva
            self.logger.registrar_evento("ERROR", "Reserva", f"Fallo en cálculo de {self.id_entidad}: {err_calc}")
            raise ReservaInvalidaError(f"No se pudo procesar el valor de la reserva {self.id_entidad}.") from err_calc
        except (ReservaInvalidaError, ServicioNoDisponibleError) as err_negocio:
            self.logger.registrar_evento("ERROR", "Reserva", f"Rechazo en {self.id_entidad}: {err_negocio}")
            raise
        else:
            # Se ejecuta únicamente si el bloque try no lanzó ninguna excepción
            self.costo_total = costo_calculado
            self.estado = "CONFIRMADA"
            self.servicio.disponible = False
            self.logger.registrar_evento(
                "INFO",
                "Reserva",
                f"Reserva {self.id_entidad} CONFIRMADA para {self.cliente.nombre}. Total: ${self.costo_total:,.2f}"
            )
            return self.costo_total
        finally:
            # Se ejecuta siempre, haya ocurrido error o éxito
            self.logger.registrar_evento(
                "AUDIT",
                "Reserva",
                f"Auditoría finalizada para intento de confirmación de reserva {self.id_entidad} (Estado: {self.estado})."
            )

    def cancelar(self) -> None:
        """Cancela una reserva activa y libera el servicio asociado."""
        if self.estado == "CANCELADA":
            raise ReservaInvalidaError(f"La reserva {self.id_entidad} ya estaba cancelada previamente.")
        estado_anterior = self.estado
        self.estado = "CANCELADA"
        if estado_anterior == "CONFIRMADA":
            self.servicio.disponible = True
        self.logger.registrar_evento("INFO", "Reserva", f"Reserva {self.id_entidad} CANCELADA correctamente.")

    def obtener_resumen(self) -> str:
        return (
            f"Reserva [{self.id_entidad}] | Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} ({self.duracion_horas}h) | "
            f"Estado: {self.estado} | Total: ${self.costo_total:,.2f}"
        )
