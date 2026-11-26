# Nombre del estudiante: Jacqueline Tovar
# Grupo: 213022A_2204
# Programa: Ingeniería de Sistemas
#
# Fase 5 - Evaluación Final POA
# Problema 2: Gestión de menú de restaurante - Aplicación de promoción
#
# Un restaurante gestiona su menú mediante una matriz con el formato:
# [Nombre del producto, Categoría, Precio base]
# Se debe aplicar un 15% de descuento a los productos que pertenezcan a
# una categoría objetivo definida y cuyo precio base supere un umbral
# establecido. Si no cumplen las dos condiciones, el precio final es
# igual al precio base.

# --- Constantes del negocio (fáciles de ajustar si cambian las reglas) ---
CATEGORIA_OBJETIVO = "Platos fuertes"
UMBRAL_PRECIO = 25000
PORCENTAJE_DESCUENTO = 0.15


def calcular_precio_final(categoria, precio_base):
    """Calcula el precio final de un producto aplicando la promoción.

    Regla de negocio:
      - Si el producto pertenece a la categoría objetivo Y su precio base
        es mayor al umbral establecido, se aplica un 15% de descuento.
      - En cualquier otro caso, se mantiene el precio base sin cambios.

    Se usa una estructura condicional compuesta (and) porque las dos
    condiciones deben cumplirse al mismo tiempo para que aplique el
    descuento.
    """
    if categoria == CATEGORIA_OBJETIVO and precio_base > UMBRAL_PRECIO:
        descuento = precio_base * PORCENTAJE_DESCUENTO
        precio_final = precio_base - descuento
        return precio_final
    else:
        return precio_base


def generar_informe(menu):
    """Recorre la matriz del menú (estructura de repetición) y muestra,
    para cada producto, su nombre, precio base y precio final luego de
    evaluar la promoción.
    """
    print("\n=================================================================")
    print(" INFORME DE PRECIOS - MENÚ DEL RESTAURANTE")
    print("=================================================================")
    print(f"{'Producto':<22}{'Categoría':<16}{'Precio base':>14}{'Precio final':>16}")
    print("-----------------------------------------------------------------")

    for producto in menu:
        nombre = producto[0]
        categoria = producto[1]
        precio_base = producto[2]

        precio_final = calcular_precio_final(categoria, precio_base)

        if precio_final < precio_base:
            etiqueta = " (con promoción)"
        else:
            etiqueta = ""

        print(f"{nombre:<22}{categoria:<16}{precio_base:>14,.0f}{precio_final:>16,.0f}{etiqueta}")

    print("-----------------------------------------------------------------")
    print(f"Categoría en promoción: {CATEGORIA_OBJETIVO}")
    print(f"Umbral de precio base: ${UMBRAL_PRECIO:,.0f}")
    print(f"Descuento aplicado: {int(PORCENTAJE_DESCUENTO * 100)}%")


def main():
    # --- Datos iniciales: matriz con 6 productos de distintas categorías ---
    menu = [
        ["Ensalada César",       "Entradas",      18000],
        ["Sopa de guineo",       "Entradas",      12000],
        ["Lomo a la pimienta",   "Platos fuertes", 35000],
        ["Pechuga a la plancha", "Platos fuertes", 28000],
        ["Cheesecake de maracuyá", "Postres",      15000],
        ["Limonada de coco",     "Bebidas",        8000],
    ]

    generar_informe(menu)


if __name__ == "__main__":
    main()
