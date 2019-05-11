
PASSWORD = '12345' ## placeHolder de la contraseña


def password_require(func): ## definimos una función (decorador) que require el password y parámetro función
  def wrapper(): ## función dentro de otra función normalmente es password
    password = input('Cual es tu contraseña? ') ## método input para captura de datos

    if password == PASSWORD: ## lógica para el password
      return func() ## si es correcto llamamos la función
    else:
      print('La contreña no es correcta.') ## si no es correcta
  return wrapper ## retornamos la funcíon wrapper

@password_require ## forma que tiene Python para utilizar los decoradores y se colocan por encima de las funciones
def needs_password():
  print('La contraseña es correcta')


def upper(func):
  def wrapper(*args, **kwargs): ## argumentos para *tuplas y **diccionarios para tomar una cantidad indefinida de argumentos
    result = func(*args, **kwargs)

    return result.upper()

  return wrapper

@upper
def say_my_name(name):
  return f'Hola, {name}'


if __name__ == '__main__':
  print(say_my_name('Juan'))
