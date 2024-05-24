import pygame


# pygame setup
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1200, 720))

player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

game_over = False

while not game_over:

    # 이벤트
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # 화면(display), screen (하면에 그릴 정보를 갖고 있는 변수)
    screen.fill('red')
    
    pygame.draw.circle(screen, "white", player_position, 40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_position.y -= 10
    if keys[pygame.K_DOWN]:
        player_position.y += 10
    if keys[pygame.K_RIGHT]:
        player_position.x += 10
    if keys[pygame.K_LEFT]:
        player_position.x -= 10

    pygame.display.flip()

    clock.tick(60) # FPS 60 fps