from ursina import *
app = Ursina()
me = Animation(
    'assets\player',
    collider='box',y=5
)
Sky()
camera.orthographic = True
camera.fov = 20
app.run()
