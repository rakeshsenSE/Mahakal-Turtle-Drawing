import turtle
from PIL import Image, ImageFilter
IMAGE_PATH = r"siva.jpg"

try:
    img = Image.open(IMAGE_PATH)
except FileNotFoundError:
    print(f"Error: {IMAGE_PATH} here is no image ")
    exit()

img = img.convert('L') 
img = img.filter(ImageFilter.FIND_EDGES)  

img = img.convert('RGB')
width, height = img.size

screen = turtle.Screen()

screen_width = width + 50
screen_height = height + 50

screen.setup(width=screen_width, height=screen_height, startx=0, starty=50)

screen.bgcolor("black") 
screen.title("Mahakal Outline Drawing")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.penup()
t.hideturtle()

print("waited...")

for y in range(height):
    for x in range(width):
        r, g, b = img.getpixel((x, y))

        if r > 50 or g > 50 or b > 50:
            turtle.colormode(255)
            t.goto(x - width // 2, height // 2 - y)

            if y < height * 0.32 and x > width * 0.65 and r > 160:
                t.dot(2, (255, 255, 255))  
            else:
                t.dot(2, (0, 210, 255))   
    if y % 5 == 0:
        screen.update()

screen.update()
print("Completed")
screen.mainloop()