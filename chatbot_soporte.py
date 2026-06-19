# Simulador de Chatbot - Soporte Técnico Nivel 1
# Trabajo Práctico Integrador - Organización Empresarial

import time

# 1. INTEGRACIÓN DE DATOS (Simulación de Base de Datos y Persistencia)
# Tabla de Clientes (Validación)
db_clientes = {
    "38444555": {"nombre": "Ana López", "estado_servicio": "ACTIVO"},
    "40111222": {"nombre": "Carlos Gómez", "estado_servicio": "ACTIVO"}
}

# 2. GESTIÓN DE ESTADOS (Memoria del Bot)
estado_bot = "INICIO"
contador_errores = 0
ticket_actual = {}

print("--- INICIANDO SIMULADOR DEL CHATBOT ---")
print("(Escribí 'salir' en cualquier momento para terminar la simulación)\n")

# Bucle principal de atención (Simula la espera constante de mensajes)
while True:
    mensaje_usuario = input("Usuario: ").strip().lower()
    
    if mensaje_usuario == 'salir':
        print("Bot: Sistema apagado. ¡Hasta luego!")
        break

    # 3. LÓGICA DE DECISIONES Y COMPUERTAS (El modelo BPMN en código)
    
    if estado_bot == "INICIO":
        print("Bot: ¡Hola! Soy el asistente virtual de Soporte Técnico.")
        print("Bot: Para poder ayudarte, por favor ingresá tu número de DNI (solo números).")
        estado_bot = "ESPERANDO_DNI" # Transición de estado
        
    elif estado_bot == "ESPERANDO_DNI":
        dni_ingresado = mensaje_usuario
        
        # COMPUERTA EXCLUSIVA: ¿Cliente Validado?
        if dni_ingresado in db_clientes:
            # CAMINO FELIZ (SÍ)
            cliente = db_clientes[dni_ingresado]
            print(f"Bot: ¡Gracias {cliente['nombre']}! Validamos tu cuenta con éxito.")
            print("Bot: ¿Qué problema presenta tu servicio?")
            print("1. Sin internet (Luz LOS roja)")
            print("2. Navegación lenta")
            estado_bot = "MENU_SOPORTE"
            contador_errores = 0 # Reiniciamos los errores
        else:
            # CAMINO INFELIZ (NO) - Manejo de la robustez
            contador_errores += 1
            if contador_errores >= 3:
                print("Bot: Límite de intentos superado. Generando ticket y derivando a un operador humano...")
                print("--- FIN DEL PROCESO (DERIVADO) ---")
                estado_bot = "INICIO" # Resetea para el próximo usuario
                contador_errores = 0
            else:
                print(f"Bot: DNI no encontrado. Por favor, intentá nuevamente. (Intento {contador_errores}/3)")
                
    elif estado_bot == "MENU_SOPORTE":
        if mensaje_usuario == "1":
            print("Bot: Entendido. Vamos a realizar una prueba técnica.")
            print("Bot: Por favor, desconectá el módem de la corriente por 10 segundos, volvé a conectarlo y escribí 'LISTO'.")
            estado_bot = "ESPERANDO_REINICIO"
        elif mensaje_usuario == "2":
            print("Bot: Estamos revisando los niveles de señal de tu zona. Aguardá un momento...")
            time.sleep(2)
            print("Bot: Hemos aplicado una actualización. Tu servicio debería mejorar en breve.")
            print("--- FIN DEL PROCESO (SOLUCIONADO) ---")
            estado_bot = "INICIO"
        else:
            print("Bot: Opción no válida. Por favor, ingresá '1' o '2'.")
            
    elif estado_bot == "ESPERANDO_REINICIO":
        if mensaje_usuario == "listo":
            print("Bot: Perfecto. ¿Se restableció la conexión a internet? (Escribí 'SI' o 'NO')")
            estado_bot = "VALIDANDO_SOLUCION"
        else:
            print("Bot: Sigo esperando. Cuando el módem encienda, escribí la palabra 'LISTO'.")
            
    elif estado_bot == "VALIDANDO_SOLUCION":
        # COMPUERTA EXCLUSIVA: ¿Se restableció la conexión?
        if mensaje_usuario == "si":
            print("Bot: ¡Excelente! Me alegra haberlo solucionado. Registrando ticket como cerrado...")
            print("--- FIN DEL PROCESO (SOLUCIONADO) ---")
            estado_bot = "INICIO"
        elif mensaje_usuario == "no":
            print("Bot: Lamento que siga fallando. Generando ticket de Nivel 2 para visita técnica...")
            print("--- FIN DEL PROCESO (DERIVADO) ---")
            estado_bot = "INICIO"
        else:
            print("Bot: Por favor, respondé únicamente con 'SI' o 'NO'.")
