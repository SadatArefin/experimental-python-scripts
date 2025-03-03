import tkinter as tk
from OpenGL import GL
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import time

# Global variables
angle = 0.0
last_time = 0
rotation_speed = 90.0  # degrees per second

def configure_rendering():
    """Configure OpenGL rendering state and properties."""
    GL.glClearColor(0.0, 0.0, 0.0, 0.0)
    GL.glEnable(GL.GL_DEPTH_TEST)
    GL.glEnable(GL.GL_BLEND)
    GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)

def setup_camera():
    """Set up perspective projection for the camera view."""
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 50.0)
    GL.glMatrixMode(GL.GL_MODELVIEW)


def create_window():
    """
    Create a window using OpenGL and GLUT libraries and set up the viewing parameters.
    """
    # Initialize GLUT
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400, 400)
    glutCreateWindow(b"OpenGL Cube")
    
    # Configure OpenGL rendering settings
    configure_rendering()
    
    # Set up camera perspective
    setup_camera()

def update(value):
    '''
    Update the angle of rotation based on elapsed time for smooth animation
    regardless of frame rate fluctuations.
    '''
    global angle, last_time
    
    # Get current time
    current_time = glutGet(GLUT_ELAPSED_TIME) / 1000.0  # Convert to seconds
    
    # Initialize last_time on first run
    if last_time == 0:
        last_time = current_time
    
    # Calculate time delta
    delta = current_time - last_time
    last_time = current_time
    
    # Use elapsed time to calculate rotation increment
    # Direction changes every 5 seconds
    direction = 1 if int(current_time / 2.0) % 2 == 0 else -1
    angle += rotation_speed * delta * direction
    
    # Keep angle within 0-360 range to prevent floating point issues over time
    angle %= 360.0
    
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)  # ~60 fps target

def draw_sphere(radius=0.7, slices=32, stacks=32, color=(1.0, 1.0, 1.0, 0.8)):
    """Draw a sphere with the given parameters"""
    GL.glPushMatrix()
    GL.glColor4f(*color)
    quad = gluNewQuadric()
    gluSphere(quad, radius, slices, stacks)
    GL.glPopMatrix()

def draw_cube(size=1.0, colors=None, alpha=0.8):
    """Draw a cube with the given size and colors"""
    if colors is None:
        colors = [
            (1.0, 0.0, 0.0, alpha),  # Front - red
            (0.0, 1.0, 0.0, alpha),  # Back - green
            (0.0, 0.0, 1.0, alpha),  # Top - blue
            (1.0, 1.0, 0.0, alpha),  # Bottom - yellow
            (1.0, 0.0, 1.0, alpha),  # Right - purple
            (0.0, 1.0, 1.0, alpha)   # Left - cyan
        ]
    
    # Define the 8 vertices of the cube
    vertices = [
        (-size, -size, -size),  # 0: left bottom back
        (size, -size, -size),   # 1: right bottom back
        (size, size, -size),    # 2: right top back
        (-size, size, -size),   # 3: left top back
        (-size, -size, size),   # 4: left bottom front
        (size, -size, size),    # 5: right bottom front
        (size, size, size),     # 6: right top front
        (-size, size, size)     # 7: left top front
    ]
    
    # Define indices of vertices for each face
    face_indices = [
        [4, 5, 6, 7],  # Front
        [0, 3, 2, 1],  # Back
        [3, 7, 6, 2],  # Top
        [0, 1, 5, 4],  # Bottom
        [1, 2, 6, 5],  # Right
        [0, 4, 7, 3]   # Left
    ]
    
    GL.glBegin(GL.GL_QUADS)
    for i, indices in enumerate(face_indices):
        GL.glColor4f(*colors[i])
        for idx in indices:
            GL.glVertex3f(*vertices[idx])
    GL.glEnd()

def draw_scene():
    """Draw the complete scene with cube and sphere"""
    global angle
    GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
    GL.glLoadIdentity()
    
    # Set the view position
    GL.glTranslatef(0.0, 0.0, -6.0)
    
    # Get smooth time-based y-rotation direction
    current_time = glutGet(GLUT_ELAPSED_TIME) / 1000.0
    y_rotation = 1.0 if int(current_time / 5.0) % 2 == 0 else -1.0
    
    # Apply rotation
    GL.glRotatef(angle, 1.0, y_rotation, 1.0)
    
    # Draw sphere first (inside)
    draw_sphere(radius=0.7, color=(1.0, 1.0, 1.0, 0.8))
    
    # Draw transparent cube (outside)
    draw_cube(size=1.0, alpha=0.5)  # More transparent to better see the sphere
    
    glutSwapBuffers()

def main():
    create_window()
    glutDisplayFunc(draw_scene)
    glutTimerFunc(50, update, 0)
    glutMainLoop()

if __name__ == '__main__':
    main()