from turtle import *
import pandas
import csv
turtle = Turtle()
screen = Screen()
screen.setup(600,600)
image=r"India-States\India-locator-map-blank.gif"
screen.addshape(image)
screen.setup(450,450)
turtle.shape(image)
correct_input=0

game_is_on=True
while game_is_on:
       data=pandas.read_csv("India-States\states.csv")
       user_state=screen.textinput(f"Correct Enteries {correct_input}","Enter the state name:")
       # if user_state in data.States:
       #        print("Yeah")
      
               
       to_go=data[data.States==user_state]
       # Converting to list so that we can move the state at tje position
       list=to_go.values.tolist()

       #Writing on the position
       my_state=Turtle()
       my_state.penup()
       my_state.hideturtle()
       my_state.goto(float(list[0][1]),float(list[0][2]))
       my_state.write(user_state)

screen.mainloop()

