peliculas = ["Los juegos del hambre", "El club de la pelea", "El gran truco", 
             "Gladiador", "Tiempos violentos"]
categoria = ["Los juegos del hambre Categoria: Mejor pelicula de Acción", "El club de la pelea Categoria: Mejor Guion", "El gran truco Categoria: Mejor Guion", 
             "Gladiador Categoria: Mejor drama", "Tiempos violentos Categoria: mejor drama"]
reservas = []

print("Películas nominadas:")
for i in categoria:
    print("-", i)


pelicula = input("Ingrese el nombre de la película la cual desea votar: ")

voto1=0
voto2=0
voto3=0
voto4=0
voto5=0
while True:
    if pelicula in peliculas:
        if pelicula == "Los juegos del hambre":
            voto1+=1
            break
        elif pelicula == "El club de la pelea":
            voto2+=1
            break
        elif pelicula == "El gran truco":
            voto3+=1
            break
        elif pelicula == "Gladiador":
            voto4+=1
            break
        elif pelicula == "Tiempos violentos":
            voto5+=1
            break
        
        print("Películas votadas:")
        print("Los juegos del hambre votos:",voto1)
        print("El gran truco votos:",voto3)
        print("El club de la pelea votos:",voto2)
        print("Gladiador votos:",voto4)
        print("Tiempos violentos votos:",voto5)

        reserva = {
            "pelicula": pelicula,
            "votos": voto1
        }
        reservas.append(reserva)

    else:
        print("La película no está disponible.")
        break