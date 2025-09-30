# 3D Missile Intercept Simulation using vpython
from vpython import sphere, vector, rate, color, canvas, box, arrow

# Set up the 3D scene
scene = canvas(title='Missile Intercept Simulation (3D)', width=800, height=600, background=color.gray(0.95))
scene.userspin = True  # Allow mouse camera movement
scene.userzoom = True

# Draw 3D axes
axis_len = 15
arrow(pos=vector(0,0,0), axis=vector(axis_len,0,0), color=color.red, shaftwidth=0.1)   # X axis
arrow(pos=vector(0,0,0), axis=vector(0,axis_len,0), color=color.green, shaftwidth=0.1) # Y axis
arrow(pos=vector(0,0,0), axis=vector(0,0,axis_len), color=color.blue, shaftwidth=0.1)  # Z axis

# Add a floor
floor = box(pos=vector(0,-7,0), size=vector(30,0.2,30), color=color.cyan, opacity=0.3)

# Missile and interceptor parameters
missile_start = vector(-10, 0, -5)
missile_velocity = vector(0.1, 0.05, 0.04)
interceptor_start = vector(10, -5, 7)
interceptor_velocity = vector(-0.12, 0.09, -0.05)

missile = sphere(pos=missile_start, radius=0.5, color=color.red, make_trail=True, trail_color=color.red)
interceptor = sphere(pos=interceptor_start, radius=0.5, color=color.blue, make_trail=True, trail_color=color.blue)

# Simple simulation loop
time = 0
max_time = 300

while time < max_time:
    rate(60)
    missile.pos += missile_velocity
    interceptor.pos += interceptor_velocity
    
    # Check for interception (distance threshold)
    if (missile.pos - interceptor.pos).mag < 1.0:
        print('Interception!')
        break
    time += 1

if time >= max_time:
    print('Missile was not intercepted.')
