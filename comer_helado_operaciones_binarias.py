

apetece_helado_input = input ("Te apetece un helado? (Si / NO): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print ("Respuesta incorrecta lo tomo como un NO")
    apetece_helado = False

tiene_dinero_input = input ("Tienes dinero? (Si / NO) : ").upper()
esta_el_señor_helado_input = input ("¿Esta el señor de los helados? (Si / No)").upper()
esta_tu_tia_input = input ("¿Estas con tu tia? : ").upper()

apetece_helado = apetece_helado_input == "SI"
puede_permitirselo = tiene_dinero_input == "SI" or esta_tu_tia_input == "SI"
esta_el_señor_de_los_helados = esta_el_señor_helado_input == "SI"



if apetece_helado and puede_permitirselo and esta_el_señor_de_los_helados:
    print ("Pues comete un helado")
else:
    print ("entonces nada")
