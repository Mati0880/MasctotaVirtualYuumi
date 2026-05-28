nombre = "milo"
energia = 100
felicidad = 100
print(f"energia inicial de {nombre}, energia {energia}, felicidad {felicidad}")
while energia > 0:
    print("¿que quieres hacer?: ")
    print("1.-ALIMENTAR")
    print("2.-Ver estado de salud")
    print("3.-Jugar")
    print("4.-No hacer nada")
    opcion = input("seleccione: ")
    if opcion =="1":
        energia = energia + 20
        felicidad = felicidad + 1
        print(f"Alimentaste a {nombre}, esta muy feliz contigo..")
    elif opcion == "2":
        energia = energia - 15
        felicidad = felicidad + 20
    elif opcion == "3":
        print("       /\__       ")
        print("      (    *\___  ")
        print("      /         * ")
        print("     /     (____/ ")
        print("    /______/      ")
        print(f"energia: {energia}")
        print(f"felicidad: {felicidad}")
    elif opcion == "4":
        felicidad = felicidad - 30
        energia = energia -5
        print(f"{nombre} esta muy aburrido...")
    else:
        print("Error de ingreso")
        