nombre = "Jo"
energia = 100
felicidad = 100
print(f"Energia inicial{nombre}, energia{energia}, felecidaD {felicidad}")
while energia > 0:
    print("¿Que quieres hacer?")
    print("1. Alimaentar")
    print("2. Ver estado de salud")
    print("3. Jugar")
    print("4. No hacer nada")
    opcion = input("seleccione:")
    if opcion =="1":
        energia = energia
        felicidad = felicidad
        print(f"Alimentarce a {nombre},esta muy feliz de jugar conmigo:")
    elif opcion =="2":
        energia = energia -15
        felicidad = felicidad +20
    elif opcion =="3":
        print("    /\__  ")
        print("   (   * \___")
        print("   /         O")
        print("  /    (_____/")
        print(" /        /")
        print("/________/ ")
        print(f"energia: {energia}")
        print(f"Felecidad: {felicidad}")
    elif opcion =="4":
        energia = energia -5
        felicidad = felicidad +10
        print(f"{nombre} esta muy aburrido")
    else:
        print("error ingresado")
