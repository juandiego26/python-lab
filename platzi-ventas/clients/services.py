import csv
import os

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


  ##Lógica para actualizar un cliente
  def update_clients(self, updated_client): ## recibe como parametro self segundo parametro un cliente que ya está actualizado
    clients = self.list_clients() ## obtenemos una lista de clientes de la lista que ya tenemos

    updated_clients = [] ## variable auxiliar para el ciclo y solo tomar al cliente que se modificó y los demás dejarlos como se modificó
    for client in clients: ## por cado cliente en los clientes
      if client['uid'] == updated_client.uid: ## si su iud es igual al updated_client.uid
        updated_clients.append(updated_client.to_dict()) ## añadimos el cliente que ha sido actualizado con el método to_dict para que python csv diccionarios y no objetos to_dict() lo convierte a diccionario
      else:
        updated_clients.append(client) ## si el cliente no ha sido actualizado simplemente se mete como está

    self._save_to_disk(updated_clients) ## guardar en disco

## Logica para borrar un cliente****
    def delete_client(self, client_uid):
        clients = self.list_clients()
        updated_clients = [client for client in clients if client['uid'] != client_uid]

        self._save_to_disk(updated_clients)


  def _save_to_disk(self, clients): ## metodo privado
    tmp_table_name = self.table_name + '.tmp' ## creamos un archivo temporal porque ya arbimos el archivo porque lo abrimos en modo lectura cuando obtuvimos nuestra lista de clientes
    with open(tmp_table_name, mode='w') as f: ## abrimos el archivo temporal
      writer = csv.DictWriter(f, fieldnames=Client.schema()) ## comenzamos a declarar nuestro writer
      writer.writerows(clients) ## escribimos todas las filas

    os.remove(self.table_name) ## removemos la tabla original
    os.rename(tmp_table_name, self.table_name) ## renombramos la tabla temporal con el nombre original de la tabla

