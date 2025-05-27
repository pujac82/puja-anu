from ursina import *
import random

app = Ursina()


colours = [color.red, color.green, color.dark_gray, color.blue, rgb(164,12,125),rgb(100,14,211),rgb(10,255,109),rgb(14,1,15)]

# Create the cube
cube = Entity(
    model='cube',
    color=random.choice(colours),
    scale=2,
    collider='box'  # Needed for click detection
)

def update():
    # This empty update function keeps the app running
    pass

def input(key):
    if key == 'left mouse down':
        if cube.hovered:
            cube.color = random.choice(colours)

app.run()
