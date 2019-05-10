import sys
import csv ## importamos CSV
import os

CLIENT_TABLE = '.clients.csv' # creamos el archivo con una constante
CLIENT_SCHEMA = ['name', 'company', 'email', 'position'] ## lista que va a utilizar csv para crear los diccionarios
clients = [] ## Arreglo donde donde se alamacenaran los clientes

def _initialize_clients_from_storage(): ## funcion para leer nuestro CVS
  if not os.path.exists(CLIENT_TABLE): ## para generar el archivo automáticamente si no existe
    with open(CLIENT_TABLE, mode='w') as f: ## context manager abrir la tabla
      pass
  else: ## si existe se ejecuta normal con el modo reader
    with open(CLIENT_TABLE, mode='r') as f:
      reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

      for row in reader: ## inicializamos nuestra lista de clientes
        clients.append(row) ## repesentación de un cliente como si fuera un diccionario


def _save_client_to_storage(): ## función que guardar el archivo
  tmp_table_name = f'{CLIENT_TABLE}.tmp' ## tabla temporal
  with open(tmp_table_name, mode='w') as f: ## la escribimos
    writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA) ## escribimos en el archivo
    writer.writerows(clients) ## escrimos todas las filas si las tenemos en una lista (lista de diccionarios)

    os.remove(CLIENT_TABLE) ## manipular el sistema OS elimine la tabla temporal
    os.rename(tmp_table_name, CLIENT_TABLE) ## renombramos el archvo


def _print_welcome(): ## función para crear una lista de comandos en terminal
  print('WELCOME TO BICITHOPYA VENTAS')
  print('*' * 50)
  print('What would you like to do today?')
  print('[C]reate client')
  print('[L]ist clients')
  print('[U]pdate client')
  print('[D]elete client')
  print('[S]earch client')

def _get_client_field(field_name):
  field = None

  while not field:
    field = input(f'What\'s the client {field_name}:'+ ' ')

  return field


def _get_client_name(): ## función para obtener el nombre del cliente
  client_name = None

  while not client_name:
    client_name = input('What\'s the client name?' + ' ').capitalize() ## Capitalize por si ingresan en mayuculas

    if client_name == 'exit'.capitalize(): ## para salir del programa y capitalize por si ingresan mayuculas
      client_name = None ## no hay clientes
      break ## sale del programa

  if not client_name:
    sys.exit() ## metódo exit() del modulo

  return client_name


def create_client(client): ## función create_client con el parámetro client_name
  global clients ## accedemos a la variable global con el keyword global

  if client not in clients: ## para saber si cliente existe
    clients.append(client) ## método append de la listas
  else:
    print('Client already is in the client\'s List')


def search_client(client_name): ## función para buscar un cliente
  global clients

  for client in clients:
    if client['name'] != client_name:
      continue ## continue
    else:
      return True


def list_clients(): ## función para imprimir toda la lista de clientes
  print(' uid  | name  | company | email | position  ')
  print('*' * 50)
  for idx, client in enumerate(clients): ## para imprmir la lista de clientes
    print(f'''{idx} | {client['name']} | {client['company']} | {client['email']} | {client['position']}''')


def update_client(client_id, updated_client): ## funcion para actualizar la lista de clientes

  if len(clients) -1 >= client_id:
    clients[client_id] = updated_client
  else:
    print(_client_not_found())


def delete_client(client_id): ## función para borrar un cliente
  global clients

  for idx, client in enumerate(clients):
    if idx == client_id:
      del clients[idx]
      break


def _client_not_found(): ## para reutilizar el código
  return print('Client is not  found in clients\'s list')


def _get_client_from_user():
  client = {
    'name': _get_client_field('name'),
    'company': _get_client_field('company'),
    'email': _get_client_field('email'),
    'position': _get_client_field('position'),
  }

  return client


if __name__ == '__main__': ## punto de entrada de la ejecución del script en Python
  _initialize_clients_from_storage() ## inicializamos al principio de nuestro archivo

  _print_welcome()

  command = input() ## function buil-in input para la consola
  command = command.upper() ## ponemos en mayúsculas el comando por si ingresan una minuscula

  if command == 'C': ## palabra reservada command para interacturar con la consola
    client = _get_client_from_user()

    create_client(client)
    # list_clients()
    # print(clients)

  elif command == 'L':
    list_clients()

  elif command == 'U': ## operación de update
    client_id = int(_get_client_field('id'))
    updated_client = _get_client_from_user()

    update_client(client_id, updated_client)
    # list_clients()
    # print(clients)

  elif command == 'D': ## operación de delete
    client_id = int(_get_client_field('id'))

    delete_client(client_id)
    # list_clients()
    # print(clients)

  elif command == 'S': ## operación de search
    client_name = _get_client_field('name')
    found = search_client(client_name)

    if found:
      print(f'The client {client_name} is in Client\'s list')
    else:
      print(f'The client {client_name} is not in our Client\'s list')
  else:
    print('ERROR Invalid Command')

  _save_client_to_storage() ## y al final salvamos el archivo
