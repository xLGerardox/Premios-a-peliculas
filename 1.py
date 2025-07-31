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
    pelicula = input("\nIngrese el nombre de la película por la cual desea votar(salir para terminar): ")

    if pelicula.lower() == "salir":
        break

    if pelicula in peliculas:
        votos[pelicula] += 1

        print("Películas votadas:")
        for nombre, cantidad in votos.items():
            print(f"{nombre} - Votos: {cantidad}")

        reserva = {
            "pelicula": pelicula,
            "votos": votos[pelicula]
        }
        reservas.append(reserva)
    else:
        print("La película no está disponible. Intente nuevamente.")

print("\nGracias por participar en la votación.")
