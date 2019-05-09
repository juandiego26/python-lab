def fibonacci(max):
  #max = max
  print(max)
  print('')
  a, b = 0, 1
  while a < max:
    yield a
    print(a)#el valor de retorno
    a, b = b, a+b


fib1 = fibonacci(20)
fib_nums = [num for num in fib1]
print(fib_nums)#se muestra la lista generada
print('*'.center(50,'*'))

double_fib_nums = [num * 2 for num in fib1] # no va a funcionar(no se muestra los valores de fib1), ya que fib1 se utilizo arriba
print(double_fib_nums)#se muestra una lista vacia por que ya no exiten los valores de fib1

double_fib_nums = [num * 2 for num in fibonacci(30)] # sí funciona, ya que se vulve a llamar a fibonacci(x), un un leve cambio que n se multiplicara x 2
print(double_fib_nums)#se muestran los valores recien generados #
print('')
print('Ejemplos extra'.center(50,'-'))
##ejemplos
# define a list
lista = [4, 7, 0, 3]

# get an iterator using iter()
mi_iterador = iter(lista)#establecemos el objeto iterador

## iterate through it using next()

#prints 4
print(next(mi_iterador))#muestra el siguiente elemento de la lista

#prints 7
print(next(mi_iterador))#muestra el siguiente elemento de la lista

## next(obj) is same as obj.__next__()

#prints 0
print(mi_iterador.__next__())#muestra el siguiente elemento de la lista

#prints 3
print(mi_iterador.__next__())#muestra el siguiente elemento de la lista

## This will raise error, no items left
next(mi_iterador)#muestra error xq ya no hay elementos a mostrar