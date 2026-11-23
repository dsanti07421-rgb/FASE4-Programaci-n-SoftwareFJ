"""
Módulo con los servicios especializados de Software FJ.
Implementa herencia, polimorfismo y sobrecarga de métodos de cálculo.
"""
from modelos_base import Servicio
from excepciones import ServicioInvalidoError, CalculoInconsistenteError

class ReservaSala(Servicio):
    """Servicio especializado para alquiler de salas de reuniones o capacitación."""
    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, capacidad: int, disponible: bool = True):
        self.capacidad = capacidad
        super().__init__(id_servicio, nombre, tarifa_base, disponible)

    def validar_parametros(self) -> None:
        if not self._nombre or len(self._nombre.strip()) < 3:
            raise ServicioInvalidoError("El nombre de la sala es inválido.")
        if self._tarifa_base <= 0:
            raise ServicioInvalidoError("La tarifa base de la sala debe ser mayor a cero.")
        if not isinstance(self.capacidad, int) or self.capacidad <= 0:
            raise ServicioInvalidoError("La capacidad de la sala debe ser un entero positivo.")

    def describir_servicio(self) -> str:
        return f"Sala '{self._nombre}' con capacidad para {self.capacidad} personas (${self._tarifa_base:,.2f}/hora)."

    def calcular_costo(self, duracion_horas: int, descuento: float = 0.0, aplicar_iva: bool = True) -> float:
        if duracion_horas <= 0 or not (0.0 <= descuento < 1.0):
            raise CalculoInconsistenteError("Duración o porcentaje de descuento fuera de rango permitido.")
        subtotal = self._tarifa_base * duracion_horas
        # Recargo operativo de limpieza si supera 4 horas
        if duracion_horas > 4:
            subtotal += 25000.0
        total_con_descuento = subtotal * (1.0 - descuento)
        return round(total_con_descuento * (1.19 if aplicar_iva else 1.0), 2)


class AlquilerEquipo(Servicio):
    """Servicio especializado para préstamo o alquiler de equipos tecnológicos."""
    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, gama: str, disponible: bool = True):
        self.gama = gama
        super().__init__(id_servicio, nombre, tarifa_base, disponible)

    def validar_parametros(self) -> None:
        if not self._nombre or len(self._nombre.strip()) < 2:
            raise ServicioInvalidoError("El nombre del equipo no puede estar vacío.")
        if self._tarifa_base <= 0:
            raise ServicioInvalidoError("La tarifa del equipo debe ser positiva.")
        if self.gama.lower() not in ("estandar", "profesional", "servidor"):
            raise ServicioInvalidoError(f"Gama '{self.gama}' no reconocida (use: estandar, profesional o servidor).")

    def describir_servicio(self) -> str:
        return f"Equipo '{self._nombre}' (Gama {self.gama.capitalize()}) a ${self._tarifa_base:,.2f}/hora."

    def calcular_costo(self, duracion_horas: int, descuento: float = 0.0, aplicar_iva: bool = True) -> float:
        if duracion_horas <= 0 or not (0.0 <= descuento < 1.0):
            raise CalculoInconsistenteError("Parámetros inválidos en el cálculo de alquiler de equipo.")
        factor_gama = 1.25 if self.gama.lower() == "servidor" else 1.0
        subtotal = (self._tarifa_base * factor_gama) * duracion_horas
        total_con_descuento = subtotal * (1.0 - descuento)
        return round(total_con_descuento * (1.19 if aplicar_iva else 1.0), 2)


class AsesoriaEspecializada(Servicio):
    """Servicio especializado para consultoría y soporte técnico en ingeniería."""
    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, area_tecnica: str, disponible: bool = True):
        self.area_tecnica = area_tecnica
        super().__init__(id_servicio, nombre, tarifa_base, disponible)

    def validar_parametros(self) -> None:
        if not self._nombre or not self.area_tecnica.strip():
            raise ServicioInvalidoError("La asesoría debe especificar nombre y área técnica.")
        if self._tarifa_base < 50000:
            raise ServicioInvalidoError("La tarifa mínima para asesoría especializada es de $50,000.")

    def describir_servicio(self) -> str:
        return f"Asesoría en {self.area_tecnica}: '{self._nombre}' (${self._tarifa_base:,.2f}/hora)."

    def calcular_costo(self, duracion_horas: int, descuento: float = 0.0, aplicar_iva: bool = True) -> float:
        if duracion_horas <= 0 or not (0.0 <= descuento < 1.0):
            raise CalculoInconsistenteError("Datos inconsistentes para calcular costo de asesoría.")
        subtotal = self._tarifa_base * duracion_horas
        total_con_descuento = subtotal * (1.0 - descuento)
        return round(total_con_descuento * (1.19 if aplicar_iva else 1.0), 2)
