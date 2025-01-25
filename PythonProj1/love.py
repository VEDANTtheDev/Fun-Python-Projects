from turtle import *
color('red','pink')
begin_fill()
left(50)
forward(100)
circle(40,180)
left(260)
circle(40,180)
forward(100)
end_fill()

getcanvas().postscript(file="heart_drawing.eps")


done()