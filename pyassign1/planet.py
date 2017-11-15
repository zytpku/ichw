import turtle
import math

#太阳质量和引力常数
M_sun = 1.988 * 10**30
G = 6.6738 * 10**-11
sun,mer,ven,ear,mar,jup,sat=turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle(),turtle.Turtle()

#水金地火木土的远日点和近日点，单位：10^11 m。颜色。 数据来源：wikipedia
data = {mer: (0.698, 0.460, 'red'), ven: (1.089, 1.075, 'orange'), ear: (1.521, 1.471, 'blue'),
        mar: (2.492, 2.067, 'gray'), jup: (8.166, 7.405, 'brown'), sat: (15.145, 13.525, 'green')}

#根据能量守恒定律，计算远日点速度
def velocity_at_aphelion(aphelion, perihelion):
    a = (aphelion + perihelion) / 2
    c = (aphelion - perihelion) / 2
    return math.sqrt((a-c) * G * M_sun / (a+c) / a)

#根据牛顿第二定律，计算任何位置的向心加速度
def acceleration_at_position(P):
    a = G * M_sun / P[0]**2
    return a * t

#直角坐标-极坐标转换函数
def cartesian_to_polar(p):
    x,y = p[0], p[1]
    r = math.sqrt(x*x + y*y)
    if x>=0:
        return (r, math.asin(y/r))
    else:
        return (r, math.pi-math.asin(y/r))

#假定所有行星最开始都位于远日点，计算初速度
velocity = {planet: (velocity_at_aphelion(value[0] * 10**11, value[1] * 10**11), math.pi/2) for planet, value in data.items()}

#以天为单位刷新数据
t = 86400

#初始化行星位置
sun.shape('circle')
sun.color('yellow')
for planet, value in data.items():
    planet.shapesize(0.3)
    planet.shape('circle')
    planet.color(value[2])
    planet.up()
    planet.forward(value[0]*10**11*10**-9.5) #比例尺：1像素等于10^9.5米
    planet.down()

# 简便起见，记每一个过程中初始速度、速度改变量、最终速度为u(x,y)、v(x,y)、w(x,y)，极坐标为U(r,a)、V(r,a)、W(r,a)。
# 记行星所在的初始点、最终点为p(x,y)、q(x,y)，转化为极坐标为P(r,a)、Q(r,a)。
# 前缀pseudo_表示这是屏幕上显示的假想坐标、速度，不带前缀的是真实坐标、速度。
while 1:
    for planet in velocity:
        V = velocity[planet]
        pseudo_p = planet.position()
        p = (pseudo_p[0] * 10**9.5, pseudo_p[1] * 10**9.5)
        P = cartesian_to_polar(p)
        U = (acceleration_at_position(P), math.pi + P[1])
        w = (V[0] * math.cos(V[1]) + U[0] * math.cos(U[1]), V[0]*math.sin(V[1]) + U[0]*math.sin(U[1]))
        W = cartesian_to_polar(w)
        q = (p[0] + w[0] * t, p[1] + w[1] * t)
        pseudo_q = (q[0] / 10**9.5, q[1] / 10**9.5)
        planet.speed(W[0]* 10**-3)#把真实速度减慢10000倍演示
        planet.goto(pseudo_q)
        velocity[planet] = W
