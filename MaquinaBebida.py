def menu_beverage():
  isAnswer = True
  isType = True

  while isAnswer:
    print("*****************************")
    print("1) Coca-cola\n2) Sprite\n3) Fanta\n0) Salir\n")
    print("*****************************")
    codeBeverage=(input("ingrese el codigo de la bebida: "))
    if codeBeverage.isnumeric():
      codeBeverageInt = int(codeBeverage)
      if codeBeverageInt > 3:
        print(str(codeBeverageInt)+" no es una opcion valida")
      else:    
        if codeBeverageInt==1:
          print("\n---> Coca-cola")
          while isType:
             codeSugar = int(input("Ingrese 1) para Zero o 2) para Normal: "))
             if codeSugar == 1:
               print("Coca-cola Zero")
               isType = False
             elif codeSugar == 2:
               print("Coca-cola Normal")
               isType = False
          isAnswer=False
        elif codeBeverageInt==2:
          print("\n---> Sprite")
          isAnswer=False
        elif codeBeverageInt == 3:
          print("\n---> Fanta")
          isAnswer=False
        if codeBeverageInt == 0:
          print("\n---> Terminado")
          isAnswer=False
    else:
      print(codeBeverage+" es invalido")

#Llamar funcion bebida
menu_beverage()


 