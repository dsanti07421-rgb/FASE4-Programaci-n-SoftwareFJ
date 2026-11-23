"""
Módulo que define las clases abstractas del sistema utilizando el módulo abc.
Garantiza el cumplimiento de abstracción y contratos obligatorios en la herencia.
"""
from abc import ABC, abstractmethod
from excepciones import ServicioInvalidoError

class EntidadSistema(ABC):
    """Clase abstracta base que representa cualquier entidad identificable del sistema."""
    def __init__(self, id_entidad: str):
        if not id_entidad or not str(id_entidad).strip():
            raise ValueError("El identificador de la entidad no puede estar vacío.")
        self._id = str(id_entidad).strip()

    @property
    def id_entidad(self) -> str:
        """Retorna el identificador único de la entidad."""
        return self._id

    @abstractmethod
    def obtener_resumen(self) -> str:
        """Método abstracto obligatorio para representar textualmente la entidad."""
        pass


class Servicio(EntidadSistema, ABC):
    """Clase abstracta que modela un servicio ofrecido por la empresa Software FJ."""
    def __init__(self, id_servicio: str, nombre: str, tarifa_base: float, disponible: bool = True):
        super().__init__(id_servicio)
        self._nombre = nombre
        self._tarifa_base = tarifa_base
        self._disponible = disponible
        # Ejecuta la validación polimórfica definida por cada servicio especializado
        self.validar_parametros()

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def tarifa_base(self) -> float:
        return self._tarifa_base

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, estado: bool) -> None:
        if not isinstance(estado, bool):
            raise ServicioInvalidoError("El estado de disponibilidad debe ser booleano (True/False).")
        self._disponible = estado

    @abstractmethod
    def validar_parametros(self) -> None:
        """Valida las reglas de negocio específicas de cada tipo de servicio."""
        pass

    @abstractmethod
    def describir_servicio(self) -> str:
        """Retorna una descripción detallada y especializada del servicio."""
        pass

    @abstractmethod
    def calcular_costo(self, duracion_horas: int, descuento: float = 0.0, aplicar_iva: bool = True) -> float:
        """
        Calcula el costo total del servicio. Soporta sobrecarga mediante parámetros
        opcionales (descuento e impuesto IVA).
        """
        pass

    def obtener_resumen(self) -> str:
        estado_txt = "Disponible" if self._disponible else "No disponible"
        return f"[{self._id}] {self._nombre} | Tarifa base: ${self._tarifa_base:,.2f} | {estado_txt}"
