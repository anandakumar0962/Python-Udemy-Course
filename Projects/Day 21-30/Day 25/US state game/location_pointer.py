from turtle import Turtle

FONT = ("Courier", 7, "bold")

class LocationPointer:
    
    def location_pointer(self,location,  x, y):
        new_location = Turtle()
        new_location.hideturtle()
        new_location.penup()
        new_location.goto(x, y)
        new_location.write(location, align='center', font=FONT)
