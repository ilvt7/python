#Funcion para sumar 2 numeros
def somar_numeros(a,b):
    resultado = a+b
    print("La Suma es: "+str(resultado))

#Funcion para restar 2 numeros
def sub_numeros(a,b):
    resultado = a-b
    print("La Resta es: "+str(resultado))

#Funcion para multiplicar 2 numeros
def mult_numeros(a,b):
    resultado = a*b
    print("La Multiplicacion es: "+str(resultado))

#Funcion para dividir 2 numeros
def div_numeros(a,b):
    if a==0 or b==0:
      print("division invalida")
    else:
      resultado = a/b
      print("la division es: "+str(resultado))



def menu_calculadora():
    isAswer = True
    while isAswer:
      print("******")
      print("1 - Sumar A y B\n2 - Restar A y B\n3 - Multiplicacion A y B\n4 - Division A y B\n5 - Salir")
      print("******")
      op = input("Seleccione una de las operaciones: " )
      if op.isnumeric() :
        opInt=int(op)
        if opInt == 5:
          print("programa encerrado")
          isAswer = False
        elif opInt > 5:
          print("Operacion Invalida")
        else:
          a=input("Ingrese numero ENTERO: ")
          b=input("Ingrese numero ENTERO: ")
          print("")
          if a.isnumeric() and b.isnumeric():
            aInt=int(a)
            bInt=int(b)
            if opInt == 1:
              somar_numeros(aInt,bInt)
              isAswer = False
            elif opInt== 2:
              sub_numeros(aInt,bInt)
              isAswer = False
            elif opInt == 3:
              mult_numeros(aInt,bInt)
              isAswer = False
            elif opInt == 4:
              div_numeros(aInt,bInt)
              isAswer = False 
          else:
            print("A = ["+a+"] o "+" B = ["+b+"] no son numeros, por favor ingresar numeros ENTEROS validos")
      else:
        print(op+ " no es una operacion valida ")    

        

#Llama la funcion calculadora
menu_calculadora()