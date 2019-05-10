import random ## para generar numeros aleatorios

def binary_search(data, target, low, high): ## función recursiva para encontrar nuestro numero en la lista
  if low > high: ## condición para determinar si el numero menos es mayor y salirse
    return False ## si no retornamos false

  mid = (low +  high) // 2 ## buscamos el indice de la lista medio

  ## casos

  if target == data[mid]: ## valor medio si el indice coincide con el valor medio return true
    return True
  elif target < data[mid]: ## valor cuando el dato es menor que lo que hay en el indice
    return binary_search(data, target, low, mid - 1) ## Función recursiva con indices de mitad abajo
  else:
    return binary_search(data, target, mid + 1, high) ## Función recursiva con indices de mitad para arriba


if __name__ == '__main__': ## punto de ingreso
  data = [random.randint(0, 100) for i in range(10)] ##  en vez de loops utilizamos list comprehensions

  data.sort() ## ordenamos nuestros datos modifando la lista original

  print(data) ## imprimimos la lista ordenada

  target = int(input('What number would you like to find? ')) ## preguntamos que quiere hacer
  found = binary_search(data, target, 0, len(data) - 1) ## le pasamos los parámetros a la función

  print(found) ## Imprimimos el numero encontrado
