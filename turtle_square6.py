import turtle
import numpy as np
import threading
import time

turtle.setup(800, 600)

#wn = turtle.Screen()
turtle.bgcolor('black')
caos = turtle.Turtle()
turtle.tracer(0, 0)

caos.speed(0)

turtle.fd(50)
caos.penup()
caos.hideturtle()
caos.ht()

random_x = np.random.randint(-350, high=350)
random_y = np.random.randint(-250, high=250)

def dibujar_punto(coordenada_x, coordenada_y, color):
    caos.color(color)
    caos.setx(coordenada_x)
    caos.sety(coordenada_y)
    return caos.dot(1)

def puntos_en_circunferencia(numero_de_puntos):
    n = numero_de_puntos
    vector_de_posiciones = []
    r = 400
    for i in range(n):
        angulo =((2 * 3.1416 * i) / n) + (0 * 3.1416/180)
        punto_x = r * np.cos(angulo)
        punto_y = r * np.sin(angulo)
        vector_de_posiciones.append(punto_x)
        vector_de_posiciones.append(punto_y)

    return vector_de_posiciones

numero_de_vertices = 5

puntos = puntos_en_circunferencia(numero_de_vertices)


j = 0
for i in range(numero_de_vertices):
    dibujar_punto(puntos[i + j], puntos[i+1+ j], 'white')
    j+=1


def fractal(num_de_puntos, pos_vertices, num_vertices, init_random_x, init_random_y):
    i = 0
    eleccion_anterior_del_punto = 000
    while i < num_de_puntos:
        eleccion_random_del_punto = np.random.randint(num_vertices)

        if eleccion_anterior_del_punto != eleccion_random_del_punto:
            l = 0
            for k in range(num_vertices):
                if  eleccion_random_del_punto == k:
                    init_random_x = (pos_vertices[k + l] + init_random_x)/2
                    init_random_y = (pos_vertices[k + 1 + l] + init_random_y)/2
                    dibujar_punto(init_random_x, init_random_y, 'cyan')
                l += 1
            i +=1
        eleccion_anterior_del_punto = eleccion_random_del_punto

fractal(50000, puntos, numero_de_vertices, random_x, random_y)


turtle.mainloop()

time.sleep(2)