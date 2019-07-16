#!/usr/bin/env /python

import pygame, sys
import pygame.camera
from pygame.locals import *

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN)

cam = pygame.camera.Camera("/dev/video0", (800, 480))
cam.start()

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



