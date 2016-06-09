import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import time
										# global game parameters
global width, height, axrng							# window parameters
global paddle_speed, ypos,ypos2, dy, size, thickness, paddle_move		# paddle parameters
global radius, x, y, vx, vy, ay, dl						# ball paremeters
global dt, anim	, collision_buffer						# environment parameters

anim = False
width = height = 600
axrng = 12
paddle_speed = 0.02
paddle_move = 0
dt = 0.5
ypos = 8
ypos2 = -8
size = 8
thickness = 0.8
radius = 0.5
x = -11+thickness/2.0 + radius +0.001
y = ypos
vx = 0.01
vy = 0.01
ay = 0.001
collision_buffer = 0.4
dl = 0.1

def init():
	glClearColor(0,0,0,0)		# set background color to white

def keyboard(key, x, y):
	global anim
	if (key == chr(27)):
		sys.exit()
	if (key == '0'):
		anim = not anim

def reshape(w, h):
	global axrng
	if (h == 0):
		h = 1
	glViewport(0,0,w,h)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	if (w<=h):
		gluOrtho2D(-axrng, axrng, -axrng*h/w, axrng*h/w)
	else:
		gluOrtho2D(-axrng*w/h, axrng*w/h, -axrng, axrng)
	glMatrixMode(GL_MODELVIEW)
	glLoadIdentity()

def collision_wall():
	global y, axrng, radius, vy
	if (abs(y)+radius >= axrng):
		vy *= -1

def collision_paddle():
	global ypos, ypos2, x, y, radius, vx, size, thickness, ay, vy, paddle_move, dl
	if (y <= ypos + size/2.0 and y >= ypos - size/2.0):
		if (x-radius >= -11+thickness/2.0-collision_buffer and x-radius <= -11+thickness/2.0):
			vx *= -1
			vy += ay
			paddle_move = 0
	if (y <= ypos2 + size/2.0 and y >= ypos2 - size/2.0):
		if (x+radius <= 11-thickness/2.0+collision_buffer and x+radius >= 11-thickness/2.0):
			vx *= -1
			size -= dl
			paddle_move = 0
	
def draw():
	global axrng
	glClear(GL_COLOR_BUFFER_BIT)
	glColor3f(1, 1, 1)
	glBegin(GL_LINES)
	glVertex2f(0, axrng)
	glVertex2f(0, -axrng)
	glEnd()
	
	# draw the player
	global ypos, size, paddle_speed, paddle_move, dt, thickness
	global radius, x, y, vx, vy, anim, collision_buffer
	dy = paddle_move*paddle_speed*dt
	if (x<0):
		if (dy < 0 and ypos-size/2.0+dy >= -axrng):
			ypos += dy
		elif (dy > 0 and ypos+size/2.0+dy <= axrng):
			ypos += dy
	glColor3f(1, 0, 0)												# Set paddle color to red
	glBegin(GL_QUADS)
	glVertex2f(-11-thickness/2.0, ypos+size/2.0)
	glVertex2f(-11+thickness/2.0, ypos+size/2.0)
	glVertex2f(-11+thickness/2.0, ypos-size/2.0)
	glVertex2f(-11-thickness/2.0, ypos-size/2.0)
	glEnd()
	# draw the opponent
	global ypos2
	glColor3f(0, 0, 1)												# Set paddle color to blue
	if (x>0):
		if (dy < 0 and ypos2-size/2.0+dy >= -axrng):
			ypos2 += dy
		elif (dy > 0 and ypos2+size/2.0+dy <= axrng):
			ypos2 += dy
	glBegin(GL_QUADS)
	glVertex2f(11-thickness/2.0, ypos2+size/2.0)
	glVertex2f(11+thickness/2.0, ypos2+size/2.0)
	glVertex2f(11+thickness/2.0, ypos2-size/2.0)
	glVertex2f(11-thickness/2.0, ypos2-size/2.0)
	glEnd()
	
	# draw the ball
	collision_wall()													# check for collision with top and bottom walls
	collision_paddle()													# check for collision with paddles
	
	if (abs(x)+radius > 11-thickness/2.0+collision_buffer):
		anim = False
		print "game will exit in 5 seconds"
		time.sleep(1)
		sys.exit()
	
	if anim:
		x += vx*dt
		y += vy*dt
	glColor3f(0,1,0)												# Set ball color to green
	glPushMatrix()
	glTranslate(x, y, 0)
	glutSolidSphere(radius, 10, 10)
	glPopMatrix()

	glutSwapBuffers()

	
def special(key, x, y):
	global ypos, size, axrng, paddle_speed, dt, vx, paddle_move
	dy = dt*paddle_speed
	if (key == GLUT_KEY_UP and ypos+dy+size/2.0<=axrng):
		paddle_move = 1
	if (key == GLUT_KEY_DOWN and ypos-dy-size/2.0>=-axrng):
		paddle_move = -1
	glutPostRedisplay()

def idle():
	if (anim == True):
		glutPostRedisplay()

def main():
	global width, height
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGB|GLUT_DOUBLE)
	glutInitWindowSize(width, height)
	glutInitWindowPosition(250, 75)
	glutCreateWindow("Pong")
	glutKeyboardFunc(keyboard)
	glutReshapeFunc(reshape)
	glutDisplayFunc(draw)
	glutSpecialFunc(special)
	glutIdleFunc(idle)
	init()
	print "press 0 to start/pause"
	glutMainLoop()

main()
