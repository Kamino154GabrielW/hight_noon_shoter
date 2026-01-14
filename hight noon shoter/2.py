import pygame
import random
from pygame import mixer
pygame.mixer.init()
pygame.font.init()

Strzal_dzwienk= pygame.mixer.Sound('bullet-hit-metal-84818.mp3')

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

puszka1_bool=True

puszka2_bool=True

puszka3_bool=True

puszka4_bool=True

puszka5_bool=True

puszka6_bool=True

puszka7_bool=True







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

tlo_nakladka=pygame.image.load("nakładka_py2.png")

def bilt_tlo():
        okno.blit(tlo,(0,0))
        okno.blit(tlo_nakladka,(0,0))


        if puszka1_bool:
            okno.blit(cel_obraz,(200,525))
            
        if puszka2_bool:
            okno.blit(cel_obraz,(350,325))
            
        if puszka3_bool:
            okno.blit(cel_obraz,(600,170))

        if puszka4_bool:
            okno.blit(cel_obraz,(600,450))

        if puszka5_bool:
            okno.blit(cel_obraz,(850,370))

        if puszka6_bool:
            okno.blit(cel_obraz,(950,200))
            
        if puszka7_bool:
            okno.blit(cel_obraz,(1000,700))
            
        
            
       

        


        
        if  x_celownik !=0 and y_celownik!=0:
            okno.blit(dziura, (x_celownik-10, y_celownik-10))
        okno.blit(wnik_text,(500,100))
        okno.blit(przspieszenie_text,(50,20))
        


tlo=pygame.image.load("background_1.png")
cel_obraz=pygame.image.load("puszka.png")
okno = pygame.display.set_mode((x_okna,y_okna))
loop=True
dziura=pygame.image.load("trafienie.png")

while loop==True:
        wnik_str="puszki:"+str(wynik)+"/7"
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

                        match (x_celownik, y_celownik):
                            case (x, y) if 200<x < 280 and 500<y < 625 and puszka1_bool==True:
                                print("puszka1")
                                puszka1_bool=False
                                wynik+=1
                                
                            case (x, y) if 350<x < 430 and 325< y < 425 and puszka2_bool==True:
                                print("puszka2")
                                puszka2_bool=False
                                wynik+=1
                            case (x, y) if 600<x < 680 and 170< y <270 and puszka3_bool==True:
                                print("puszka3")
                                puszka3_bool=False
                                wynik+=1

                            case (x, y) if 600<x < 680 and 450< y < 550 and puszka4_bool==True:
                                print("puszka4")
                                puszka4_bool=False
                                wynik+=1

                            case (x, y) if 850<x < 930 and 370< y < 470 and puszka5_bool==True:
                                print("puszka5")
                                puszka5_bool=False
                                wynik+=1

                            case (x, y) if 950<x < 1030 and 200< y < 300 and puszka6_bool==True:
                                 print("puszka6")
                                 puszka6_bool=False
                                 wynik+=1

                            case (x, y) if 1000<x < 1080 and 700< y < 800 and puszka7_bool==True:
                                print("puszka7")
                                puszka7_bool=False
                                wynik+=1
                            
                                
                                
                            case _:
                                print("pudło")

                        

   
                    

                        print(f"Wynik: {wynik}")

                        
                    if event.key == pygame.K_r:
                        puszka1_bool=True
                        puszka2_bool=True
                        puszka3_bool=True
                        puszka4_bool=True
                        puszka5_bool=True
                        puszka6_bool=True
                        puszka7_bool=True

                        wynik=0
                        
                        



                




        
        


                            
                    

        pygame.time.wait(40)
        
        

        
        
        pygame.display.update()     
