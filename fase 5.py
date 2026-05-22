
# SISTEMA DE AUDITORÍA Y REABASTECIMIENTO DE




def mostrar_menu():
    """
    Función que muestra el menú principal del programa.
    No recibe parámetros y no retorna nada, solo imprime en pantalla.
    """
    print("\n" + "=" * 60)
    print(" SISTEMA DE AUDITORÍA DE INVENTARIO")
    print("=" * 60)
    print("1. Ingresar artículos al inventario")
    print("2. Ver inventario completo")
    print("3. Generar lista de pedidos (reabastecimiento)")
    print("4. Salir del programa")
    print("=" * 60)


def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Función que calcula la cantidad exacta que se debe pedir de un artículo.

    Parámetros:
        stock_actual (int): Cantidad actual disponible del artículo
        stock_minimo (int): Cantidad mínima requerida del artículo

    Retorna:
        int: Cantidad que se debe pedir (0 si no necesita reabastecimiento)

    Lógica de negocio:
        - Si stock actual < stock mínimo: pedir la diferencia
        - Si stock actual >= stock mínimo: no pedir nada (retorna 0)
    """
    if stock_actual < stock_minimo:
        # Necesita reabastecimiento: calculamos la diferencia
        cantidad_a_pedir = stock_minimo - stock_actual
        return cantidad_a_pedir
    else:
        # Stock suficiente: no necesita pedido
        return 0


def ingresar_articulos():
    """
    Función que solicita al usuario ingresar los datos de los artículos.
    Crea y retorna una matriz (lista de listas) con la información del inventario.

    Retorna:
        list: Matriz con los artículos ingresados. Cada artículo es una lista con:
              [código, nombre, stock_actual, stock_mínimo]
    """
    # Inicializamos la matriz vacía que almacenará todos los artículos
    inventario = []

    print("\n--- INGRESO DE ARTÍCULOS AL INVENTARIO ---")

    # Preguntamos cuántos artículos desea ingresar (mínimo 5 según requisitos)
    while True:
        try:
            cantidad_articulos = int(input("\n¿Cuántos artículos desea ingresar? (mínimo 5): "))
            if cantidad_articulos >= 5:
                break
            else:
                print("  Debe ingresar al menos 5 artículos.")
        except ValueError:
            print("  Por favor ingrese un número válido.")

    # Ciclo para ingresar cada artículo
    for i in range(cantidad_articulos):
        print(f"\n--- Artículo {i + 1} de {cantidad_articulos} ---")

        # Solicitamos cada dato del artículo
        codigo = input("Código del artículo: ").strip()
        nombre = input("Nombre del artículo: ").strip()

        # Validamos que los números sean correctos
        while True:
            try:
                stock_actual = int(input("Stock actual: "))
                stock_minimo = int(input("Stock mínimo requerido: "))
                break
            except ValueError:
                print("  Por favor ingrese números válidos para el stock.")

        # Creamos una lista con los datos del artículo
        articulo = [codigo, nombre, stock_actual, stock_minimo]

        # Agregamos el artículo a la matriz de inventario
        inventario.append(articulo)

    print(f"\n✓ Se han ingresado {cantidad_articulos} artículos correctamente.")
    return inventario


def mostrar_inventario(inventario):
    """
    Función que muestra todos los artículos del inventario en formato tabla.

    Parámetros:
        inventario (list): Matriz con los artículos del inventario
    """
    if len(inventario) == 0:
        print("\n  El inventario está vacío. Primero debe ingresar artículos.")
        return

    print("\n" + "=" * 80)
    print(" INVENTARIO COMPLETO")
    print("=" * 80)
    print(f"{'Código':<10} {'Nombre':<25} {'Stock Actual':<15} {'Stock Mínimo':<15}")
    print("-" * 80)

    # Ciclo para recorrer cada artículo de la matriz
    for articulo in inventario:
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        print(f"{codigo:<10} {nombre:<25} {stock_actual:<15} {stock_minimo:<15}")

    print("=" * 80)


def generar_lista_pedidos(inventario):
    """
    Función que genera y muestra la lista de pedidos de reabastecimiento.
    Utiliza la función calcular_cantidad_a_pedir() para cada artículo.

    Parámetros:
        inventario (list): Matriz con los artículos del inventario
    """
    if len(inventario) == 0:
        print("\n  El inventario está vacío. Primero debe ingresar artículos.")
        return

    print("\n" + "=" * 70)
    print(" LISTA DE PEDIDOS - REABASTECIMIENTO NECESARIO")
    print("=" * 70)
    print(f"{'Nombre del Artículo':<30} {'Cantidad a Pedir':<20} {'Estado':<20}")
    print("-" * 70)

    # Variable para contar cuántos artículos necesitan reabastecimiento
    articulos_a_reabastecer = 0

    # Ciclo para procesar cada artículo del inventario
    for articulo in inventario:
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        # Llamamos a la función que calcula la cantidad a pedir
        cantidad_a_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)

        # Determinamos el estado del artículo
        if cantidad_a_pedir > 0:
            estado = " REABASTECER"
            articulos_a_reabastecer += 1
        else:
            estado = "✓ Stock OK"

        # Mostramos la información del artículo
        print(f"{nombre:<30} {cantidad_a_pedir:<20} {estado:<20}")

    print("=" * 70)
    print(f"\nResumen: {articulos_a_reabastecer} artículo(s) necesitan reabastecimiento.")
    print(f"Total de artículos en inventario: {len(inventario)}")


# ============================================================================
# PROGRAMA PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta el programa.
    Controla el flujo del menú y las opciones del usuario.
    """
    # Matriz principal que almacenará todos los artículos del inventario
    inventario = []

    # Ciclo principal del programa
    while True:
        mostrar_menu()

        # Solicitamos la opción al usuario
        opcion = input("\nSeleccione una opción (1-4): ").strip()

        # Estructura condicional para manejar las opciones del menú
        if opcion == "1":
            # Opción 1: Ingresar artículos
            inventario = ingresar_articulos()

        elif opcion == "2":
            # Opción 2: Ver inventario completo
            mostrar_inventario(inventario)

        elif opcion == "3":
            # Opción 3: Generar lista de pedidos
            generar_lista_pedidos(inventario)

        elif opcion == "4":
            # Opción 4: Salir del programa
            print("\n" + "=" * 60)
            print(" Gracias por usar el Sistema de Auditoría de Inventario")
            print("=" * 60)
            break

        else:
            # Opción inválida
            print("\n  Opción no válida. Por favor seleccione una opción entre 1 y 4.")


# Punto de entrada del programa
# Esto asegura que el programa solo se ejecute si se llama directamente
if __name__ == "__main__":
    main()