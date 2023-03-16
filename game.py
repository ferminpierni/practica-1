from random import choice, randrange
from datetime import datetime
operators = ["+", "-","*","/"]
times = 5
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
cantC = 0
cantI = 0
for i in range(0, times):
  number_1 = randrange(10)
  number_2 = randrange(10)
  operator = choice(operators)
  print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
  result = int(input("resultado: "))
  if operator == '+':
    if result == number_1 + number_2:
      print ('El resultado es CORRECTO')
      cantC += 1
    else:
      print ('EL resultado es INCORRECTO')
      cantI += 1
  else:
    if operator == '-':
      if result == number_1 - number_2:
        print ('El resultado es CORRECTO')
        cantC += 1
      else:
        print ('EL resultado es INCORRECTO')
        cantI += 1
    else:
      if operator == '*':
        if result == number_1 * number_2:
          print ('El resultado es CORRECTO')
          cantC += 1
        else:
          print ('EL resultado es INCORRECTO')
          cantI += 1
      else:
        if operator == '/':
          if result == number_1 - number_2:
            print ('El resultado es CORRECTO')
            cantC += 1
          else:
            print ('EL resultado es INCORRECTO')
            cantI += 1
end_time = datetime.now()
total_time = end_time - init_time
print(f"\n Tardaste {total_time.seconds} segundos.")
print (f"\n {cantC} resultados Correctos")
print (f"\n {cantI} resultados Incorrectos")