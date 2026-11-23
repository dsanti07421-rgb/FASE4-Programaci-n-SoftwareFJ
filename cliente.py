"""
Módulo que implementa la clase Cliente con encapsulación estricta
y validaciones de datos personales.
"""
from modelos_base import EntidadSistema
from excepciones import ClienteInvalidoError

class Cliente(EntidadSistema):
    """Representa un cliente registrado en el sistema de Software FJ."""
    def __init__(self, id_cliente: str, nombre: str, correo: str, telefono: str):
        try:
            super().__init__(id_cliente)
        except ValueError as err:
            # Encadenamiento de excepción hacia excepción de dominio
            raise ClienteInvalidoError("ID de cliente inválido o vacío.") from err

        # Uso de setters para aplicar validaciones desde la instanciación
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not valor or len(valor.strip()) < 3:
            raise ClienteInvalidoError("El nombre del cliente debe tener al menos 3 caracteres.")
        self.__nombre = valor.strip()

    @property
    def correo(self) -> str:
        return self.__correo

    @correo.setter
    def correo(self, valor: str) -> None:
        if not valor or "@" not in valor or "." not in valor.split("@")[-1]:
            raise ClienteInvalidoError(f"El correo electrónico '{valor}' no tiene un formato válido.")
        self.__correo = valor.strip().lower()

    @property
    def telefono(self) -> str:
        return self.__telefono

    @telefono.setter
    def telefono(self, valor: str) -> None:
        limpio = str(valor).strip()
        if not limpio.isdigit() or len(limpio) < 7:
            raise ClienteInvalidoError(f"El teléfono '{valor}' debe contener al menos 7 dígitos numéricos.")
        self.__telefono = limpio

    def obtener_resumen(self) -> str:
        return f"Cliente [{self.id_entidad}]: {self.__nombre} | Correo: {self.__correo} | Tel: {self.__telefono}"
