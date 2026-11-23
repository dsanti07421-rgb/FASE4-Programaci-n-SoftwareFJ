"""
Módulo de excepciones personalizadas para el sistema de gestión de Software FJ.
Permite controlar errores específicos del dominio sin detener la aplicación.
"""

class ErrorSistemaFJ(Exception):
    """Excepción base para todos los errores controlados del sistema Software FJ."""
    def __init__(self, mensaje: str, codigo_error: str = "ERR-000"):
        super().__init__(mensaje)
        self.codigo_error = codigo_error

class ClienteInvalidoError(ErrorSistemaFJ):
    """Se lanza cuando los datos de un cliente son inválidos o están incompletos."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo_error="ERR-CLI-01")

class ServicioInvalidoError(ErrorSistemaFJ):
    """Se lanza cuando los parámetros de creación de un servicio son incorrectos."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo_error="ERR-SRV-01")

class ServicioNoDisponibleError(ErrorSistemaFJ):
    """Se lanza cuando se intenta reservar un servicio que no tiene disponibilidad."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo_error="ERR-SRV-02")

class ReservaInvalidaError(ErrorSistemaFJ):
    """Se lanza ante operaciones no permitidas o estados inválidos en una reserva."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo_error="ERR-RES-01")

class CalculoInconsistenteError(ErrorSistemaFJ):
    """Se lanza cuando ocurre un fallo aritmético o tarifario al calcular costos."""
    def __init__(self, mensaje: str):
        super().__init__(mensaje, codigo_error="ERR-CAL-01")
    
