import turtle
wn=turtle.Screen()
wn.screensize(10000.10000)
sun=turtle.Turtle()
earth=turtle.Turtle()
mercury=turtle.Turtle()
venus=turtle.Turtle()
mars=turtle.Turtle()
jupiter=turtle.Turtle()
saturn=turtle.Turtle()

colors=["red","blue","yellow","green","black","pink","purple"]
def location (x,y,name,n):
    name.shape("circle")
    name.color(colors[n])
    name.up()
    name.goto(x,y)
    name.down()
    return 

def ellipse (a,c,name):
    for x in range(c-a,a+c+1,1):
        b2=a**2-c**2
        n=1-(x-c)**2/a**2
        y=(b2*n)**0.5
        name.goto(x,y)
    for x in range(a+c,c-a-1,-1):
        b2=a**2-c**2
        n=1-(x-c)**2/a**2
        y=-(b2*n)**0.5
        name.goto(x,y)
    return

location(0,0,sun,0)
planets=[mercury,venus,earth,mars,jupiter,saturn]
a=[40,90,160,200,300,400]
c=[8,1,3,19,13,20]

for n in range(6):
    location(c[n]-a[n],0,planets[n],n+1)
    ellipse(a[n],c[n],planets[n])

wn.exitonclick()
    