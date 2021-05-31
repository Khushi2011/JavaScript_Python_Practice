# import random
# a=random.randint(100,101)
# print(a)
# b=random.random()*100
# print(b)
# list=(1,2,3,4,5,6) #in ludo we can use
# print(random.choice(list))
# This will import turtle module
import turtle
turtle.speed(6)
my_turtle=turtle.Turtle() #it will give turtle object so we can use that class method..
my_turtle.shape("arrow")
my_turtle.screen.title("Snake Game")
my_turtle.screen.bgcolor("aqua")
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(150)
turtle.done() #turtle.done() use for window open otherwise it will close within second
# When you will run the code snippets of this tutorial in any Python IDE you will notice that the turtle window will open and close immediately.
# To allow the turtle window stay so you can see the output of your program,
