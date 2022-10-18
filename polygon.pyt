import turtle

def polygon(sides, length):
  t = turtle.Turtle()
  t.color("lime")
  t.speed(0)
  angle = 360 / sides
  for side in range(sides):
    t.forward(length)
    t.right(angle)
  t.hideturtle()

for n in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    polygon(n, 35)
