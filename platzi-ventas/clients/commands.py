import click
from clients.services import ClientService
from clients.models import Client

@click.group() ## decorador para convertir a comandos de click convierte a la funcion clients en otro decorador
def clients(): ## funcion para definir cual es el grupo al cual van a pertenecer todas estas funciones
  """Manages the clients lifecycle""" ## doted string nos sirven para generar la interfaz de usuario
  pass

##**** Interfaz de consola para la creación de clientes******
@clients.command() ## para decirle que este es un comando
@click.option('-n', '--name', ## parametro para de click short name -n y nombre --name
              type=str, ## typo string
              prompt=True, ## que si no dan via patron abreviado debemos pedirselo al usuario
              help='The client name') ## ayuda
@click.option('-c', '--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-e', '--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-p', '--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_context ## pasamos el contexto
def create(ctx, name, company, email, position): ## definimos el comando create con el contexto y los parámetros
  """Creates a new client """ ## Dot string
  client = Client(name, company, email, position) ## incializamos el cliente
  client_service = ClientService(ctx.obj['clients_table']) ## jalamos del contexto el nombre de la tabla

  client_service.create_client(client) ## le pasamos la referencia a nuestro cliente

##**** Interfaz de consola para la creación de clientes******
## list no necesita nungun parametro ni ninguna opcion porque solo mostramos la lista
@clients.command() ##comando clients
@click.pass_context ## contexto
def list(ctx): ## funcion list solo recibe el contexto que un diccionario vacio
  """List all clients"""
  client_service = ClientService(ctx.obj['clients_table']) ## refeenciamos nustro ClientService

  client_list = client_service.list_clients() ## traemos nuestra lista de clientes de la clase list_clients de la logica de negocio services.py

  click.echo(' ID  | NAME  | COMPANY | EMAIL | POSITION  ') ## tabla para imprimir los headers,lo hacemos como ECHO porque en distintos S.O print se muestra diferente
  click.echo('*' * 100) ## una linea

  for client in client_list: ## iteramos la lista de los clientes
    click.echo(f'''{client['uid']} | {client['name']} | {client['company']} | {client['email']} | {client['position']}''')


@clients.command()
@click.pass_context
def update(ctx, client_uid): ## función update
  """Updates a Client"""
  pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid): ## función Delete
  """Deletes a client"""
  pass


all = clients ## definimos un alias para que sea fácil declarar todas estas funciones en un solo code
