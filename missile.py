import random
import pygame
################################################
pygame.init() #초기화임

#화면의 크기
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height)) #이게 화면 크기다 하하하

#FPS
clock = pygame.time.Clock()

#배경 이미지
background = pygame.image.load(r'background.png')

#솔져 스프라이트
sol = pygame.image.load(r"C:\Users\rub77\Music\zkim\programs\missile\sol.png")
sol_size = sol.get_rect().size
sol_width = sol_size[0]
sol_height = sol_size[0]
sol_x_pos = (screen_width / 2) - (sol_width / 2)
sol_y_pos = screen_height - sol_height

#솔의 속도
to_x = 0
sol_speed = 10

##########################################3

#총알? 미사일? 대포? 난몰라
bullet = pygame.image.load(r"C:\Users\rub77\Music\zkim\programs\missile\bullet.png")
bullet_size = bullet.get_rect().size
bullet_width = bullet_size[0]
bullet_height = bullet_size[1] 
bullet_x_pos = random.randint(0, screen_width - bullet_width)
bullet_y_pos = 0
bullet_speed = 5

#이벤트 루프
running = True #게임이 진행중인가요? true
while running:

    dt = clock.tick(60) #게임 화면의 초당 프레임 수

    for event in pygame.event.get(): #게임이 진행중일때 어떤 이벤트가 발생하면 여기서 처리 (ex.마우스, 키보드 클릭킹 등등)
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생하였는가? 
            running = False #창이 닫힌다 = 게임도 진행이 멈춘다.

        if event.type == pygame.KEYDOWN: #키를 눌렀을때
            if event.key == pygame.K_LEFT: #왼쪽을 누르면 왼쪽으로
                to_x -= sol_speed
            elif event.key == pygame.K_RIGHT: #오른쪽을 누르면 오른쪽으로
                to_x += sol_speed

        if event.type == pygame.KEYUP: #아무것도 누르지 않으면 걍 가자미!!
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    sol_x_pos  += to_x

    #솔의 탈영막기 (가로막기)
    if sol_x_pos < 0:
        sol_x_pos = 0
    elif sol_x_pos > screen_width - sol_width:
        sol_x_pos = screen_width - sol_width

    bullet_y_pos += bullet_speed #총알 떨어지기

    #총알 떨어지기
    if bullet_y_pos > screen_height:
        bullet_y_pos = 0
        bullet_x_pos = random.randint(0, screen_width - bullet_width)

    #충돌처리 불쌍한 솔,,,
    sol_rect = sol.get_rect()
    sol_rect.left = sol_x_pos
    sol_rect.top = sol_y_pos

    #총알의 충돌처리
    bullet_rect = bullet.get_rect()
    bullet_rect.left = bullet_x_pos
    bullet_rect.top = bullet_y_pos

    if sol_rect.colliderect(bullet_rect):
        print ("당신은 정말 저질이군요 당신 때문에 쟤 인생은 망했스빈다")
        running = False

    screen.blit(background, (0, 0)) #배경의 위치 (aka 좌표)
    screen.blit(sol, (sol_x_pos, sol_y_pos)) #솔의 위치
    screen.blit(bullet, (bullet_x_pos, bullet_y_pos)) #총알의 좌표

    pygame.display.update()

#게임이 종료하면 pygame도 종료
pygame.quit()
