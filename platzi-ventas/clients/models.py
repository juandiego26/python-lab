import uuid

class Client:

  def __init__(self, name, company, email, position, uid=None): ## self es this
    self.name = name ## instanciamos el objeto name de la clase Client
    self.company = company
    self.email = email
    self.position = position
    self.uid = uid or uuid.uuid4() ## utilizamos el modulo uuid o uuid4 standar de la industria

  def to_dict(self): ##
    return vars(self) ## funcion global vars chequea que regresa el metodo dunder __init__ y nos permite acceder a un diccionario porque para poder escribirlo a disco CSV necesitamos convertirlo a diccionario

  @staticmethod ## decorador para declarar metodos estaticos  se puede ejecutar sin necesidad de una instancia de clase
  def schema(): #guardamos el esquema serian como las columnas
    return ['name', 'company', 'email', 'position', 'uid'] ## regresa una lista de objetos
