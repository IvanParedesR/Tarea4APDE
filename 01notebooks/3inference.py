## Con el modelo antes calculado, aquí le pedimos al usuario que señale sus valores esperados para cada variable.
numero1 = float(input(f"Del 1 al 10 en que tan buena condición esperas que este la casa, siendo 1 mala y 10 excelente: "))
numero2 = float(input(f"De qué tamaño esperas que sea el terreno en pies cuadrados: "))
numero3 = float(input(f"Cuántos lugares de estacionamiento quieres: "))
numero4 = float(input(f"Año de su última renovación en 4 cifras: "))

# Realizamos el cálculo
resultado = -8.485e+05 + (numero1 * 2.989e+04) + (numero2 * 1.1699) + (numero3 * 2.29e+04) + (numero4 * 399.0900)

# Imprimimos el resultado
print(f"El precio aproximado de una casa con esas caracteristicas es: {int(resultado)}")
