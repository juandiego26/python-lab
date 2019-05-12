
import click ## importamos librería click

from clients import commands as clients_commands ## importamos los comandos de la carpeta clients

CLIENTS_TABLE = '.clients.csv' ## variable global
@click.group() ## decorador para decirle al módulo click que este es nuestro punto de entrada
@click.pass_context ## decorador que nos da un objeto contexto
def cli(ctx): ## definimos nuestro punto de entrada
  ctx.obj = {} ## inicializamos el objeto contexto como un diccionario vacio
  ctx.obj['clients_table'] = CLIENTS_TABLE ## añadimos al contexto

cli.add_command(clients_commands.all) ## registramos estos comandos CLI hace refencia a esta funcion dentro de ese modulo utulizamos la variabe all
