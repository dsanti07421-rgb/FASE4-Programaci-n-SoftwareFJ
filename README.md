# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

**Curso:** Programación (Código: 213023) – Fase 4: Componente Práctico (Prácticas Simuladas)  
**Institución:** Universidad Nacional Abierta y a Distancia (UNAD)  
**Escuela:** Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)  
**Autor:** David Santiago Acosta Santos  
**Lenguaje:** Python 3.10+  

---

## 1. Descripción General del Proyecto

Este repositorio contiene la implementación modular del **Sistema Integral de Gestión de Clientes, Servicios y Reservas** diseñado para la empresa **Software FJ**. El objetivo técnico de la solución es evidenciar la aplicación rigurosa de los principios de la **Programación Orientada a Objetos (POO)** y el **manejo avanzado de excepciones** en Python, garantizando la continuidad operativa y estabilidad del software frente a fallos en tiempo de ejecución sin emplear motores de bases de datos.

---

## 2. Arquitectura y Estructura Modular

El proyecto está organizado en siete módulos independientes bajo el principio de separación de responsabilidades:

| Módulo | Responsabilidad Técnica | Conceptos POO / Excepciones Aplicados |
| :--- | :--- | :--- |
| `excepciones.py` | Define la jerarquía de errores del dominio (`ErrorSistemaFJ` y excepciones específicas). | Herencia de excepciones y códigos de error estructurados. |
| `logger.py` | Gestiona la persistencia de eventos operativos, auditorías y fallos en `sistema_fj.log`. | Manejo seguro de archivos planos (`with open`) y control de `OSError`. |
| `modelos_base.py` | Establece las clases abstractas `EntidadSistema` y `Servicio` mediante el módulo `abc`. | Abstracción y contratos obligatorios (`@abstractmethod`). |
| `cliente.py` | Modela la entidad `Cliente` con validación estricta de identificación, correo y teléfono. | Encapsulación (`__atributos`), `@property` y encadenamiento de excepciones. |
| `servicios.py` | Implementa `ReservaSala`, `AlquilerEquipo` y `AsesoriaEspecializada`. | Herencia, polimorfismo y sobrecarga mediante parámetros opcionales (descuento e IVA). |
| `reserva.py` | Controla el ciclo de vida de las reservas (`PENDIENTE`, `CONFIRMADA`, `CANCELADA`). | Bloques `try / except / else / finally` y encadenamiento (`raise ... from`). |
| `main.py` | Orquesta una simulación secuencial de **12 operaciones** (válidas e inválidas). | Tolerancia a fallos y ejecución continua sin interrupciones. |

---

## 3. Requisitos y Ejecución

### Requisitos del entorno
* **Python 3.10 o superior** (no requiere instalación de librerías externas; emplea únicamente la biblioteca estándar `abc` y `datetime`).

### Instrucciones de ejecución
1. Clonar el repositorio o descargar los archivos fuente:
   ```bash
   git clone [https://github.com/dsanti07421-rgb/FASE4-Programaci-n-SoftwareFJ.git](https://github.com/dsanti07421-rgb/FASE4-Programaci-n-SoftwareFJ.git)
   cd FASE4-Programaci-n-SoftwareFJ
