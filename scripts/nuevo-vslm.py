IPinicial = []
host = []
subredes = input("Digite el numero de subredes: ")
print("Ingrese IP inicial")
for i in range(4):
    correct = False
    while(not correct):
        try:
            inicial = (input(f"Ingrese octeto {i+1}: "))
            if (int(inicial) >= 0):
                correct = True
                IPinicial.append(inicial)
            else:
                print("\nIngrese un valor correcto. Vuelva a intentarlo...\n")
        except (RuntimeError, TypeError, NameError, IndexError, ValueError):
            print("\nIngrese un valor correcto. Vuelva a intentarlo...\n")
            
correct = False

while(not correct):
  try:
    prefijo = int(input("Ingrese mascara inicial(prefijo): "))
    if prefijo > 0:
      print(bin(prefijo))
      correct = True
    else:
      print("\nIngrese un valor correcto. Vuelva a intentarlo...\n")
  except (RuntimeError, TypeError, NameError, IndexError, ValueError):
    print("\nIngrese un valor correcto. Vuelva a intentarlo...\n")        

print("IP guardada....")
print(".".join(IPinicial),"/",prefijo)
bin(prefijo)
print('\n')




correct = False