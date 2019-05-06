
## Variable global
clients = 'pablo, ricardo, '

## creamos una función create_client con parámetro client_name

def create_client(client_name):
  global clients ## accedemos a la variable global con el keyword global
  clients += client_name

  _add_comma()

def list_clients():
  global clients

  print(clients)

## add una función privada para add la comma
def _add_comma():
  global clients

  clients += ','

## Es la forma en la que el interprete de python que es el punto de entrada para la
## ejecución del script
if __name__ == '__main__':
  list_clients()

  create_client('David') ## llamamos la funcíon y le pasamos parámetros

  list_clients()
