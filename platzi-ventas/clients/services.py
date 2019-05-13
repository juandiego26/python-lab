import csv

from clients.models import Client

class ClientService: ## declaramos la clase logica de negocio

  def __init__(self, table_name): ## decaramos la función nombre de la tabla donde la vamos a guardar
    self.table_name = table_name ## lo guardamos en una variable de instancia

  ## lógica para crear el cliente
  def create_client(self, client): ## create client reside dentro de una clase
    with open(self.table_name, mode='a') as f: ## logica para abrir un archivo en modo append para añadir el cliente al final
      writer = csv.DictWriter(f, fieldnames=Client.schema()) ## cuales son las columnas
      writer.writerow(client.to_dict()) ## escribimos una nueva fila DictWrite necesita diccionarios el cliente que recibimos como parametro lo convertimos a diccionario

  ## Lógica para mostrar la lista de los cliente
  def list_clients(self):
    with open(self.table_name, mode='r') as f: ## abrimos el archivo en modo reader referenciandolo como f
      reader = csv.DictReader(f, fieldnames=Client.schema()) ## solo leemos el archivo

      return list(reader) ## y lo retornamos como una lista para que sea leído
