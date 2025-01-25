import time
import datetime as dt
import turtle


# create a turtle to display time
t = turtle.Turtle()

# create a turtle to create rectangle box
t1 = turtle.Turtle()

# create screen
s = turtle.Screen()

# set background color of the screen
s.bgcolor("purple")

# obtain current hour, minute and second
# from the system
sec = dt.datetime.now().second
min = dt.datetime.now().minute
hr = dt.datetime.now().hour
t1.pensize(3)
t1.color('black')
t1.penup()

# set the position of turtle
t1.goto(-20, 0)
t1.pendown()

# create rectangular box
for i in range(2):
	t1.forward(200)
	t1.left(90)
	t1.forward(70)
	t1.left(90)

# hide the turtle
t1.hideturtle()


# Function to update clock
def update_clock():
	global sec, min, hr
	t.hideturtle()
	t.clear()
	t.write(str(hr).zfill(2) + ":" + str(min).zfill(2) + ":" + str(sec).zfill(2),
			font=("Arial Narrow", 35, "bold"))

	s.getcanvas().postscript(file="digital_clock.eps")  # Save snapshot

	time.sleep(1)
	sec += 1

	if sec == 60:
		sec = 0
		min += 1

	if min == 60:
		min = 0
		hr += 1

	if hr == 13:
		hr = 1

	s.ontimer(update_clock, 1000)


# Start clock update
update_clock()
turtle.done()
# while True:
# 	t.hideturtle()
# 	t.clear()
# 	# display the time
# 	t.write(str(hr).zfill(2)
# 			+ ":"+str(min).zfill(2)+":"
# 			+ str(sec).zfill(2),
# 			font=("Arial Narrow", 35, "bold"))
# 	time.sleep(1)
# 	sec += 1
#
# 	if sec == 60:
# 		sec = 0
# 		min += 1
#
# 	if min == 60:
# 		min = 0
# 		hr += 1
#
# 	if hr == 13:
# 		hr = 1
