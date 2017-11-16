import turtle
from math import hypot
from numpy import *
def initial(aphelion, perihelion): #在远日点处行星的速度公式
    return math.sqrt(2 * perihelion * G * M / aphelion / (aphelion + perihelion))

pixel = 3 * 10**9 #图中一像素=天上十光秒
time = 86400 #图中一秒=天上一日
M = 1.988 * 10**30 #太阳质量
G = 6.6738 * 10**-11 / pixel**3 #引力常数，并进行量纲约化
sun, mer, ven, ear, mar, jup, sat = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
source = {mer: (0.698, 0.460, 'red'), ven: (1.089, 1.075, 'orange'), ear: (1.521, 1.471, 'blue'),
          mar: (2.492, 2.067, 'gray'), jup: (8.166, 7.405, 'brown'), sat: (15.145, 13.525, 'green')} #行星近日点远日点，单位：10**11米。
data = {planet: array([0, initial(info[0] * 10**11 / pixel, info[1] * 10**11 / pixel)]) for planet, info in source.items()} #假定行星一开始都在远日点，计算它们的初速度，并用列表存储

sun.shape('circle')
sun.color('yellow')
for planet, info in source.items():
    planet.shapesize(0.3)
    planet.shape('circle')
    planet.color(info[2])
    planet.up()
    planet.forward(info[0] * 10**11 / pixel) #行星前进至远日点
    planet.down()

while 1:
    for planet, velocity in data.items():
        x, y = planet.position() #获取位置
        r = hypot(x, y) #计算该位置与太阳的距离
        acceleration = array([- G * M * x / r**3, - G * M * y / r**3]) #计算行星的加速度，以向量表示
        velocity += acceleration * [time] #计算行星末速度，以向量表示
        planet.speed(hypot(velocity[0], velocity[1]) * time) #求速度向量的模，然后放大t倍用于演示
        planet.goto(x + velocity[0] * time, y + velocity[1] * time) #计算下一时刻行星位置并去往
        data[planet] = velocity #末速度存储覆盖初速度
