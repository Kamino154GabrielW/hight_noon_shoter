import pygame
import time
import random

x_okna=1300
y_okna=800

x_celownik=0
y_celownik=0

def high_noon():
    cel_dolny = pygame.image.load("celownik_dolny.png")
    cel_boczny = pygame.image.load("celownik_boczny.png")

    x, y = 1250, 820

    def przesun_celownik(pozycja, kierunek, obraz, orientacja,prendkosci):
        while True:
            bilt_tlo()
            if orientacja == "pion":
                okno.blit(obraz, (0, pozycja))
            else:
                okno.blit(cel_dolny, (0, y))  
                okno.blit(obraz, (pozycja, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return pozycja

            pygame.time.wait(prendkosci)
            pozycja -= 5
            pygame.display.update()

    y = przesun_celownik(y, -5, cel_dolny, "pion",2)
    x = przesun_celownik(x, -5, cel_boczny, "poziom",2)

    pygame.time.wait(100)
    okno.fill((255,255,255))
    pygame.display.update()    
    pygame.time.wait(1000)
    return x, y

def bilt_tlo():
        okno.blit(tlo,(0,0))
        okno.blit(cel_obraz,(200,200))
        


tlo=pygame.image.load("background_1.png")
cel_obraz=pygame.image.load("tarcza_sztrzelecka.png")
okno = pygame.display.set_mode((x_okna,y_okna))
loop=True
while loop==True:
        bilt_tlo()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                            x_celownik,y_celownik=high_noon()
                            print(x_celownik)
                            print(y_celownik)


                            
                    


        
        pygame.time.wait(40)
        

        
        
        pygame.display.update()     
