
clients = 'Pablo,Ricardo' ## creamos la variable global clients


def _print_welcome(): ## función para crear una lista de comandos en terminal
  print('WELCOME TO BICITHOPYA VENTAS')
  print('*' * 50)
  print('What would you like to do today?')
  print('[C]reate client')
  print('[L]ist clients')
  print('[U]pdate client')
  print('[D]elete client')
  print('[S]earch client')


def _get_client_name(): ## función para obtener el nombre del cliente
  return input('What\'s the client name?' + ' ').capitalize()


def create_client(client_name): ## función create_client con el parámetro client_name
  global clients ## accedemos a la variable global con el keyword global

  if client_name not in clients: ## para saber si cliente existe
    clients += client_name ## añadimos el cliente
    _add_comma() ## adicionamos la comma
  else:
    print('Client already is in the client\'s List')


def _add_comma(): ## función para añadir una comma y reutilizar el código
  global clients

  clients += ','


def search_client(client_name): ## función para buscar un cliente
  client_list = clients.split(',') ## metodo split de los string para convertir a estructura separadas por ,

  for client in client_list:
    if client != client_name:
      continue ## continue
    else:
      return True


def list_clients(): ## función para imprimir toda la lista de clientes
  global clients

  print(clients)


def update_client(client_name): ## funcion para actualizar la lista de clientes
  global clients

  if client_name in clients:
    updated_client_name = input('What\'s the updated client name?' + ' ')
    clients = clients.replace(client_name + ',', updated_client_name + ',')
  else:
    print(_client_not_found())


def delete_client(client_name): ## función para borrar un cliente
  global clients

  if client_name in clients:
    clients = clients.replace(client_name + ',', '')
  else:
    print(_client_not_found())


def _client_not_found(): ## para reutilizar el código
  return print('Client is not  found in clients\'s list')


if __name__ == '__main__': ## punto de entrada de la ejecución del script en Python
  _print_welcome()

  command = input() ## function buil-in input para la consola
  command = command.upper() ## ponemos en mayúsculas el comando por si ingresan una minuscula

  if command == 'C': ## palabra reservada command para interacturar con la consola
    client_name = _get_client_name()
    create_client(client_name)
    #list_clients()
    print(clients)

  elif command == 'L':
    list_clients()

  elif command == 'U': ## operación de update
    client_name = _get_client_name()
    update_client(client_name)
    #list_clients()
    print(clients)

  elif command == 'D': ## operación de delete
    client_name = _get_client_name()
    delete_client(client_name)
    #list_clients()
    print(clients)

  elif command == 'S': ## operación de search
    client_name = _get_client_name()
    found = search_client(client_name)

    if found:
      print(f'The client {client_name} is in Client\'s list')
    else:
      print(f'The client {client_name} is not in our Client\'s list')
  else:
    print('ERROR Invalid Command')
