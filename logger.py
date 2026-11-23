"""
Módulo encargado de registrar eventos y errores en un archivo de texto (logs),
cumpliendo el requisito de no utilizar bases de datos.
"""
from datetime import datetime

class RegistradorLogs:
    """Gestiona la escritura segura de eventos y excepciones en archivo plano."""
    def __init__(self, ruta_archivo: str = "sistema_fj.log"):
        self.ruta_archivo = ruta_archivo

    def registrar_evento(self, nivel: str, modulo: str, mensaje: str) -> None:
        """Escribe una línea formateada con fecha y hora en el archivo de logs."""
        marca_tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"[{marca_tiempo}] [{nivel.upper()}] [{modulo}] -> {mensaje}\n"
        try:
            # Abre el archivo en modo anexar (append) con codificación UTF-8
            with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
                archivo.write(linea)
        except OSError as error_io:
            # Si falla la escritura en disco, se informa en consola sin detener el sistema
            print(f"[ALERTA CRÍTICA DE LOG] No se pudo escribir en {self.ruta_archivo}: {error_io}")
