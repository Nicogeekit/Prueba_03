

numero_correcto = 10

numero_del_usuario = int(input("Diga su numero: "))


if numero_del_usuario == numero_correcto:
    print ("Ganaste, acertaste el numero")

else:
 numero_del_usuario = int(input("diga su numero nuevamente: "))

if numero_del_usuario == numero_correcto:
    print ("Ganaste, acertaste el numero")

else:
    numero_del_usuario = int (input("Diga si numero nuevamente le quedan 2 intentos: "))

if numero_del_usuario == numero_correcto:
    print ("Ganaste, acertaste el numero")

else:
    numero_del_usuario = int (input("Diga su numero nuevamente, le quedan 1 intentos: "))

if numero_del_usuario == numero_correcto:
    print ("Ganaste, acertaste el numero")

else:
    print ("Usaste todos los intentos, fallaste xD.")