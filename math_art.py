from __future__ import division
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

# Set the width and the height of the window with global variables
# Set the axis range using the global variable axrng
global width
global height
global axrng

# Initial values
width = 600
height = 600
axrng = 6

# Tasks to perform while initialization
def init():
	glClearColor(1, 1, 1, 1)		# set background color to white

def draw():
	glClear(GL_COLOR_BUFFER_BIT)	# clear the background
	glPointSize(1)
	glBegin(GL_POINTS)
	step_x = 2*axrng/width
	step_y = 2*axrng/height
	for x in arange(-axrng, axrng, step_x):
		for y in arange(-axrng, axrng, step_y):
		
			# Coloring equations #
			r = sin(x*y)
			glColor3f(x*r, r*r, y*r)
			######################
			
			glVertex2f(x, y)
	
	glEnd()
	glFlush()

def reshape(w, h):
	# To ensure we do not have a zero height window
	if (h == 0):
		h = 1
	# Fill the entire graphics window
	glViewport(0,0,w,h)
	# Set the projection Matrix
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	# Set the aspect ratio of the plotting
	if (w<=h):
		gluOrtho2D(-axrng, axrng, -axrng*h/w, axrng*h/w)
	else:
		gluOrtho2D(-axrng*w/h, axrng*w/h, -axrng, axrng)
	# Set the matrix for the object we are drawing
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def keyboard(key, x, y):
	if key == chr(27):
		sys.exit()

def main():
	global width, height

        glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB|GLUT_SINGLE)
	glutInitWindowSize(width, height)
	glutInitWindowPosition(0, 0)
	glutCreateWindow("Math Art")
	glutReshapeFunc(reshape)
	glutDisplayFunc(draw)
	glutKeyboardFunc(keyboard)
	
	init()
	glutMainLoop()

main()
