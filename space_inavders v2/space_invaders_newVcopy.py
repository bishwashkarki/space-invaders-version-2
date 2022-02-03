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
    def __init__(self):
        # Initialization of the Strings
        self.String1 ="Hello"
        self.String2 ="World"

    def shoot_proj(self):
        cycle=0
        ball_position = projectile1.get_rect(midbottom=(700,800))
        screen.blit(projectile1, ball_position)
        
        while True:
            screen.blit(background, ball_position, ball_position)
            ball_position = ball_position.move(0, -10)
            screen.blit(projectile1, ball_position) 
            pygame.display.update()
            pygame.time.delay(30)
            cycle+=1
            if cycle==100:
                break

    def space_ship_movement(self):
        spritex=700
        spritey=800
        
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
                    if event.key == event.key == ord('z'):
                        self.shoot_proj()
                        

        

#class shoot_projectile:
#    #def __init__(self,spritex,spritey,vel):
#    #    self.spritex=spritex
#    #    self.spritey=spritey
#    #    self.vel=vel
    

#proj_cor = shoot_projectile(500,500,2)