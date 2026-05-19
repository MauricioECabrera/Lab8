# Laboratorio 8 - Ingeniería de Software II

## Descripción

Aplicación web sencilla desarrollada en Flask para demostrar gestión de versiones usando Feature Flags.

La aplicación cuenta con dos versiones:

- Versión 1: saludo básico en español.
- Versión 2: interfaz mejorada en inglés con nuevas funcionalidades.

## Tecnologías usadas

- Python
- Flask
- HTML
- CSS
- Git

## Estrategia de versiones

Se utilizó una Feature Flag para activar o desactivar funcionalidades de la versión 2.

```python
VERSION_2_ACTIVA = True