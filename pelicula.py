peliculas = ["Los juegos del hambre", "El club de la pelea", "El gran truco", 
             "Gladiador", "Tiempos violentos"]

categorias = [
    "Los juegos del hambre - Categoría: Mejor película de Acción",
    "El club de la pelea - Categoría: Mejor Guion",
    "El gran truco - Categoría: Mejor Guion",
    "Gladiador - Categoría: Mejor Drama",
    "Tiempos violentos - Categoría: Mejor Drama"
]

votos = {
    "Los juegos del hambre": 0,
    "El club de la pelea": 0,
    "El gran truco": 0,
    "Gladiador": 0,
    "Tiempos violentos": 0
}

reservas = []

print("Películas nominadas:")
for i in categorias:
    print("-", i)

while True:
    try:
        pelicula = input("\nIngrese el nombre de la película por la cual desea votar(salir para terminar): ")
    except Exception as e:
        print("Error al ingresar el nombre:", e)
        continue

    if pelicula.lower() == "salir":
        break

    if pelicula in peliculas:
        try:
            votos[pelicula] += 1

            print("Películas votadas:")
            for nombre, cantidad in votos.items():
                print(f"{nombre} - Votos: {cantidad}")

            reserva = {
                "pelicula": pelicula,
                "votos": votos[pelicula]
            }

            reservas.append(reserva)
        except Exception as e:
            print("Ocurrió un error al registrar el voto o la reserva:", e)
    else:
        print("La película no está disponible. Intente nuevamente.")

print("\nGracias por participar en la votación.")

mas_votada = max(votos, key=votos.get)
print(f"\n La película más votada fue: {mas_votada} con {votos[mas_votada]} votos.")

# Total de votos
print(f"Total de votos registrados: {sum(votos.values())}")
