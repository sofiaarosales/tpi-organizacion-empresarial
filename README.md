# TPI - Simulador de Chatbot de Soporte Técnico

## Descripción
Este repositorio contiene el código fuente del Trabajo Práctico Integrador para la materia Organización Empresarial. Es un simulador en consola desarrollado en Python que emula el comportamiento de un chatbot de Soporte Técnico Nivel 1, basado en un modelo BPMN 2.0.

## Características Técnicas Implementadas
* **Máquina de Estados:** Se utiliza la variable `estado_bot` para que el sistema tenga "memoria" del flujo de la conversación y no pierda el contexto.
* **Persistencia Simulada:** Uso de diccionarios locales (`db_clientes`) para simular la consulta a una base de datos real.
* **Robustez (Camino Infeliz):** Implementación de la variable `contador_errores` para atajar entradas no válidas y derivar de forma segura tras 3 intentos fallidos.

## Cómo desplegar el simulador
1. Asegurarse de tener Python instalado en el equipo.
2. Descargar el archivo `chatbot_soporte.py`.
3. Abrir la terminal o línea de comandos en la carpeta donde se descargó.
4. Ejecutar el comando: `python chatbot_soporte.py`.
5. Interactuar con la consola. *(Tip: Para probar el camino feliz, utilizar el DNI 38444555).*
