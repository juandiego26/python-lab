
class Person: ## declaramos la clase
  def __init__(self, name, age): ## dunder init este método iniciliza los valores
    self.name = name ## palabra que hace refencia a las propiedades de la clase equivalente this
    self.age = age


  def say_hello(self):
    print(f'Hello, my name is {self.name} and I\'m {self.age} years old')


if __name__ == '__main__':
  person = Person('David', 34)

  print(f'Age: {person.age}')
  person.say_hello()