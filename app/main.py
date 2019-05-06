
clients = 'pablo, ricardo, ' ## creamos la variable global clients


def create_client(client_name): ## función create_client con el parámetro client_name
  global clients ## accedemos a la variable global con el keyword global

  if client_name not in clients: ## para saber si cliente existe
    clients += client_name ## añadimos el cliente
    _add_comma() ## adicionamos la comma
  else:
    print('Client already is in the client\'s List')

def list_clients(): ## función para imprimir la lista de clientes
  global clients

  print(clients)

def update_client(client_name): ## funcion para actualizar la lista de clientes
  global clients

  if client_name in clients:
    updated_client_name = input('What\'s the updated client name?' + ' ')
    clients = clients.replace(client_name + ',', updated_client_name + ',')
  else:
    print('Client is not found in the client\'s list')


def _add_comma(): ## función para añadir una comma
  global clients

  clients += ','

def _print_welcome(): ## función para crear una
  print('WELCOME TO PLATZI VENTAS')
  print('*' * 50)
  print('What would you like to do today?')
  print('[C]reate client')
  print('[U]pdate client')
  print('[D]elete client')

def _get_client_name(): ## función para reutilzzar la misma pregunta
  return input('What\'s the client name?' + ' ')

if __name__ == '__main__': ## punto de entrada de la ejecución del script
  _print_welcome()

  command = input() ## function buil-in input para la consola
  command = command.upper() ## ponemos en mayúsculas el comando por si ingresan una minuscula

  if command == 'C': ## palabra reservada command para interacturar con la consola
    client_name = _get_client_name()
    create_client(client_name)
    list_clients()
  elif command == 'D': ## operación de delete
    pass
  elif command == 'U': ## operación de update
    client_name = _get_client_name()
    update_client(client_name)
    list_clients()
  else:
    print('Invalid command')
