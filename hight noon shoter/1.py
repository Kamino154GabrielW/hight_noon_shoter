import pygame
import random
from pygame import mixer
pygame.mixer.init()
pygame.font.init()

Strzal_dzwienk= pygame.mixer.Sound('bullet-hit-metal-84818.mp3')
Trafienie_dzwienk=pygame.mixer.Sound('ground-impact-352053 (1).mp3')

mixer.music.load('cowboy-rythym-solo-louder-ver-25312.mp3') 
pygame.mixer.music.set_volume(2)  
mixer.music.play(-1)

x_okna=1300
y_okna=800

x_celownik=-100
y_celownik=-100

przspieszenie=10

x_wnik=0
y_wnik=0
wynik=0

X_START, X_END = 400, 800
Y_START, Y_END = 210, 590




X_MID = 600
Y_MID = 400


OFFSET_SUBTRACT = 150
font = pygame.font.SysFont("Comic Sans MS", 24)


def high_noon(przspieszenie):
    cel_dolny = pygame.image.load("celownik_dolny.png")
    cel_boczny = pygame.image.load("celownik_boczny.png")

    x, y = 1250, 820

    def przesun_celownik(pozycja, kierunek, obraz, orientacja,prendkosci):
        while True:
            bilt_tlo()
            if orientacja == "pion":
                okno.blit(obraz, (0, pozycja-10))
            else:
                okno.blit(cel_dolny, (0, y-10))  
                okno.blit(obraz, (pozycja-10, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return pozycja+26

            pygame.time.wait(prendkosci)
            pozycja -= 10
            pygame.display.update()

    y = przesun_celownik(y, -10, cel_dolny, "pion",przspieszenie)
    x = przesun_celownik(x, -10, cel_boczny, "poziom",przspieszenie)

    pygame.time.wait(500)
    okno.fill((255,255,255))
    pygame.mixer.Sound.play(Strzal_dzwienk)
    pygame.display.update()    
    pygame.time.wait(600)
    if x<=0:
        x=0
    if y<=0:
        y=0
    return x, y

def bilt_tlo():
        okno.blit(tlo,(0,0))
        okno.blit(cel_obraz,(203,200))
        if  x_celownik !=0 and y_celownik!=0:
            okno.blit(dziura, (x_celownik-10, y_celownik-10))
        okno.blit(wnik_text,(500,100))
        okno.blit(przspieszenie_text,(50,20))
        


tlo=pygame.image.load("background_1.png")
cel_obraz=pygame.image.load("tarcza_sztrzelecka.png")
okno = pygame.display.set_mode((x_okna,y_okna))
loop=True
dziura=pygame.image.load("trafienie.png")

while loop==True:
        wnik_str="wynik:"+str(wynik)
        wnik_text = font.render(wnik_str, True, (255, 255, 255))

        przspieszenie_str=f"<{przspieszenie}>"
        przspieszenie_text=font.render(przspieszenie_str, True, (255, 255, 255))
        
        bilt_tlo()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type ==pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if przspieszenie>1:
                            przspieszenie-=1
                        else:
                            przspieszenie=20
                    if event.key == pygame.K_RIGHT:
                        if przspieszenie<20:
                            przspieszenie+=1
                        else:
                            przspieszenie=1
                            
                    if event.key == pygame.K_SPACE:
                        x_celownik, y_celownik = high_noon(przspieszenie)

                        print(f"Celownik: ({x_celownik}, {y_celownik})")

   
                        if X_START < x_celownik < X_END and Y_START < y_celownik < Y_END:
        
        
                            x_dist_center = abs(x_celownik - X_MID) 
                            y_dist_center = abs(y_celownik - Y_MID) 

       
                            x_wnik = 200 - x_dist_center 
        
        
                            y_wnik = 190 - y_dist_center 

        
                            wynik = y_wnik + x_wnik
                            wynik -= OFFSET_SUBTRACT
                            print(wynik,(wynik/przspieszenie/2))
                            wynik=wynik+ (wynik/przspieszenie/2)

        
                            wynik = max(0, wynik)
                            pygame.mixer.Sound.play(Trafienie_dzwienk)
        
                        else:
                            wynik = 0

                        print(f"Wynik: {wynik}")



                




        
        


                            
                    

        pygame.time.wait(40)
        
        

        
        
        pygame.display.update()     
