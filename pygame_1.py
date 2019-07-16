#!/usr/bin/env /python

import pygame, sys
import pygame.camera
from pygame.locals import *

import faceapi

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)

cam = pygame.camera.Camera("/dev/video0", (800, 400))
cam.start()

def onButton():
	global cam
	cam.stop()
	faceapi.play()

def button(x, y, w, h):
	global screen

	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()
	
	pygame.draw.rect(screen, (0, 200, 0), (x, y, w, h))
	if x+w > mouse[0] > x and y+h > mouse[1] > y:
		if click[0] == 1:
			onButton()

while 1:
	image = cam.get_image()
	screen.blit(image, (0, 0))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				pygame.quit()
				sys.exit()
		if event.type == pygame.QUIT:
			sys.exit()

	
	button(400, 380, 100, 100)
