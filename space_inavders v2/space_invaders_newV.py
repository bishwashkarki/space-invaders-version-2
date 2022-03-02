import pygame

screen = pygame.display.set_mode((1600,900))
#screen = pygame.display.set_mode((1500,800))

background = pygame.image.load('images/background_space.bmp').convert()
player1=pygame.image.load('images/player1.bmp').convert()
projectile1=pygame.image.load('images/fireball1.gif').convert()
player1 = pygame.transform.scale(player1, (50, 50))
projectile1 = pygame.transform.scale(projectile1, (20, 20))
FPS=60
fpsClock=pygame.time.Clock()



class space_ship:

    def space_ship_movement():
        spritex=700
        spritey=800
        proj_x=spritex
        proj_y=spritey
        speed=2

        WHITE=(255, 255, 255)
        player1.set_colorkey(WHITE)

        main=True

        while main:
            screen.blit(background,(0,0))
            screen.blit(player1, (spritex, spritey))

            

            keys_pressed = pygame.key.get_pressed()

            if keys_pressed[pygame.K_LEFT]:
                spritex -= speed

            if keys_pressed[pygame.K_RIGHT]:
                spritex += speed

            if keys_pressed[pygame.K_UP]:
                spritey -= speed

            if keys_pressed[pygame.K_DOWN]:
                spritey += speed

            if keys_pressed[pygame.K_z]:
                screen.blit(projectile1, (proj_x, proj_y))
                proj_y -= 10
                pygame.time.delay(100)
                
                
                
                






            pygame.display.update()
            fpsClock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit(); 
                    main = False
                if event.type == pygame.KEYDOWN:
                    if event.key == ord('q'):
                        pygame.quit()
                        main = False 

        

