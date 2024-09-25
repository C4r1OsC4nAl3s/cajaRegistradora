def mostrar_menu():
    print("Bienvenido a la caja registradora")
    print("Por favor, ingresa los artículos que deseas comprar.")
    print("Escribe 'fin' para terminar y calcular el total.")

def agregar_articulo():
    articulos = {}
    
    while True:
        nombre = input("Nombre del artículo: ")
        if nombre.lower() == 'fin':
            break
        
        try:
            precio = float(input(f"Precio de {nombre}: $"))
            cantidad = int(input(f"Cantidad de {nombre}: "))
            
            # Validar que la cantidad sea positiva
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser un número positivo.")
            
            # Agregar el artículo al diccionario
            articulos[nombre] = {'precio': precio, 'cantidad': cantidad}
        
        except ValueError as ve:
            print(f"Error: {ve}. Por favor, introduce valores válidos.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    return articulos

def calcular_total(articulos):
    total = 0
    for articulo, detalles in articulos.items():
        subtotal = detalles['precio'] * detalles['cantidad']
        total += subtotal
        print(f"{articulo}: ${detalles['precio']} x {detalles['cantidad']} = ${subtotal:.2f}")
    return total

def caja_registradora():
    mostrar_menu()
    articulos = agregar_articulo()
    
    if not articulos:
        print("No se ingresaron artículos.")
        return

    total_a_pagar = calcular_total(articulos)
    print(f"Total a pagar: ${total_a_pagar:.2f}")

    try:
        dinero_insertado = float(input("Inserta el dinero: $"))
        
        # Validar que el dinero insertado sea suficiente
        if dinero_insertado < total_a_pagar:
            raise ValueError("Dinero insuficiente. Por favor, inserta más dinero.")
        
        # Calcular y mostrar el cambio
        cambio = dinero_insertado - total_a_pagar
        if cambio > 0:
            print(f"Cambio devuelto: ${cambio:.2f}")
        
        print("Gracias por tu compra. ¡Vuelve pronto!")
    
    except ValueError as ve:
        print(f"Error: {ve}. Asegúrate de introducir valores válidos.")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Llamar a la función para ejecutar la caja registradora
caja_registradora()

