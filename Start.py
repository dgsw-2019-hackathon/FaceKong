#-*-encoding:utf-8
import pygame
import pygame.camera
from pygame.locals import *
import sys

import faceapi

#씬 위치
scene = 0

#게임 모드
mod = 1

#결과 저장 변수


#해상도
width = 800
height = 480

#배경색
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ground_color = WHITE


#메인화면 이미지
img_start = pygame.image.load('image/Start.png')

#배경화면 이미지
img_background = pygame.image.load('image/background.png')

#버튼 이미지 메인화면
img_mod1 = pygame.image.load('image/Mod_1.png')
img_mod2 = pygame.image.load('image/mod_2.png')
img_return = pygame.image.load('image/Return.png')

#버튼 이미지 결과창
img_home = pygame.image.load('image/Home.png')
img_retry = pygame.image.load('image/ReTry.png')

#선택창 이미지들

#img_list = ["슬픔", "경멸스러움", "역겨움", "화남", "놀람", "무서움", "행복함"]
img_list = [pygame.image.load('image/Home.png'), pygame.image.load('image/Home.png'), pygame.image.load('image/Home.png'), pygame.image.load('image/Home.png'),
            pygame.image.load('image/Home.png'), pygame.image.load('image/Home.png'), pygame.image.load('image/Home.png')]


#버튼 좌표 설정 - 시작화면
button_start_pos = img_start.get_rect(x = 0, y = 0)

#배경화면 좌표 설정
button_background_pos = img_background.get_rect(x = 0, y = 0)

#버튼 좌표 설정 - 메인화면 
button_mod1_pos = img_mod1.get_rect(x = 100, y = 190)
button_mod2_pos = img_mod2.get_rect(x = 450, y = 190)
button_return_pos = img_return.get_rect(x = 660, y = 390)

#버튼 좌표 설정 - 결과창
button_home_pos = img_home.get_rect(x = 500, y = 370)
button_retry_pos = img_retry.get_rect(x = 170, y = 370)

button_capture_pos = img_home.get_rect(x = 300, y = 400)
#버튼 좌표 설정 - 선택창
i = 0
list_lenght = len(img_list)
print(list_lenght)

button_list_pos = list()

while(i < list_lenght):
    if i > 3:
        x_pos = 100 * (i - 3)
        y_pos = 100
    else:
        x_pos = 100 * i
        y_pos = 0
    button_list_pos.append(img_list[i].get_rect(x = x_pos, y = y_pos))
    i += 1


#배경 화면 설정 함수
def background():

    global pad
    
    pad.fill(WHITE)
    pad.blit(img_background, button_background_pos)

#선택 기능 함수
def select_scene():

    global pad, scene, list_lenght

    background()

    i = 0

    while(i < list_lenght):
        pad.blit(img_list[i], button_list_pos[i])
        i += 1
        
    pad.blit(img_home, button_home_pos)
        
    #pad.blit(img_list[0], img_list[0].get_rect(x = 0, y = 0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_home_pos.collidepoint(pygame.mouse.get_pos()):
                scene = 1
                print("씬 1로 넘김")

def play_scene():
    global pad, scene, cam

    background()

    #cam.start()
    cam_image = cam.get_image()
    pad.blit(cam_image, (0, 0))
    
    pad.blit(img_retry, button_capture_pos)
    pad.blit(img_home, button_home_pos)
 
 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
	    if button_home_pos.collidepoint(pygame.mouse.get_pos()):
	        cam.stop()
		scene = 1
		print("메인 화면으로")
            elif button_capture_pos.collidepoint(pygame.mouse.get_pos()):
	        cam.stop()
		faceapi.play()
		print('faceapi play end')
		scene = 5
		cam.start()
		print("결과창으로")


#결과 씬 함수
def result_scene():
    
    global pad, scene

    background()
    
    pad.blit(img_home, button_home_pos)
    pad.blit(img_retry, button_retry_pos)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_home_pos.collidepoint(pygame.mouse.get_pos()):
                scene = 1
                print("씬 1로 넘김")
            elif button_retry_pos.collidepoint(pygame.mouse.get_pos()):
                if mod :
                    print("준비중")
                else :
                    select_scene()

# 메인 씬 함수
def main_scene():

    global pad, scene, mod
    
    background()
    
    pad.blit(img_mod1, button_mod1_pos)
    pad.blit(img_mod2, button_mod2_pos)
    pad.blit(img_return, button_return_pos)
    
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_mod1_pos.collidepoint(pygame.mouse.get_pos()):
                print("씬3으로 넘김")
                scene = 3
               # print("임시 결과창으로 넘김")
                #scene = 5
                mod = 1
                print(mod)
            elif button_mod2_pos.collidepoint(pygame.mouse.get_pos()):
                print("씬2으로 넘김")
                scene = 2
                mod = 2
                print(mod)
            elif button_return_pos.collidepoint(pygame.mouse.get_pos()):
                print("씬 0으로 넘김")
                scene = 0

# 시작 씬 함수      
def start_scene():
    
    global exit_scene, scene

    pad.fill(ground_color)
    
    pad.blit(img_start, button_start_pos)
    
    for event in pygame.event.get(): # 이벤트가 있을때 반복 
        if event.type == pygame.QUIT: # 우측 상단 X키 누르면 꺼짐
            exit_scene = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_start_pos.collidepoint(pygame.mouse.get_pos()):
                print("씬1로 넘김")
                scene = 1
	elif event.type == pygame.KEYDOWN:
	    if event.key == pygame.K_ESCAPE:
	    	exit_scene = True
		
#동작 메인
def main():
    
    global pad, clock, scene, exit_scene, cam

    exit_scene = False # 클릭 False
    
    while not exit_scene:
        if scene == 1:
            main_scene()
        elif scene == 2:
            select_scene()
        elif scene == 3:
	    play_scene()
        elif scene == 5:
            result_scene()
        else:    
            start_scene()
            
        pygame.time.delay(1) #딜레이 설정
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    sys.exit()

#시작 셋팅
def start():
    
    global pad, clock, cam

    pygame.init()
    pygame.camera.init()
    pad = pygame.display.set_mode((width, height), pygame.FULLSCREEN)

    cam = pygame.camera.Camera("/dev/video0", (800, 400))
    cam.start()
    pygame.display.set_caption('FACE')
    clock = pygame.time.Clock()

    main()

#######시작########
start()    
