while True:
    print("\nmenu")
    print("1.persona")
    print("2.vehiculos")
    print("3.universidades")
    print("4.notas")
    print("5.salir")
    
    opcion = input("Seleccione una opcion (1-5): ")
    
    if opcion == '1':
       print("Hola has presionado la opcion persona")
    elif opcion == '2':
       print("Hola has presionado la opcion vehiculos: ")
    elif opcion == '3':
       print("Hola has presionado la opcion universidades: ")
    elif opcion == '4':
       print("Hola has presionado la opcion notas: ")
    elif opcion == '5':
       print("Adios, el programa se ha finalizado: ")
       break
    else:
      print("opcion invalida, por favor seleccione una opcion valida  (1-5).")

    