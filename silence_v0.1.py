#pip install pygame --user

import pygame
from pygame import *
import all_textes as v
import image as d
import random


(largeur, hauteur) = (1920, 1080)  
BLACK=(0,0,0)
WHITE=(255,255,255)  
FPS = 60
compteur=1
change_displayed = False

text_rect =(largeur/2, hauteur/2)


pygame.init()
clock = pygame.time.Clock()  
   
fenetre = pygame.display.set_mode((0,0), pygame.FULLSCREEN) 
fenetre.fill(BLACK) 

cadre=pygame.image.load("image\cadre2.png").convert_alpha()
inventaire=pygame.image.load("image\inventaire.png").convert_alpha()
download1=pygame.image.load("image\download.png").convert_alpha()
download2=pygame.image.load("image\download2.png").convert_alpha()
next=pygame.image.load("image\\next.png").convert_alpha()
blanc=pygame.image.load("image\\blanc.png").convert_alpha()

font_obj = pygame.font.Font('ew_police.ttf', 20)  #

x=fenetre.get_size()


if x==(1920, 1080):
    (largeur, hauteur) = (1920, 1080)
    x=1920
    y=1080

elif x==(2560, 1440):
    (largeur, hauteur) = (2560, 1440)
    x=2560
    y=1440


pygame.key.set_repeat(400, 10)
continuer = True
while continuer:
    fenetre.fill(BLACK)
    image_bio=d.image_biome()
    image_weap=d.image_weapons()
    image_an=d.image_animals()
    image_foo=d.image_foods()
    fenetre.blit(cadre,(x//4.5,y//1.6))
    fenetre.blit(inventaire,(10,50))
    fenetre.blit(download1,(10,y-262))
    fenetre.blit(download2,(10,y-262*2))
    fenetre.blit(next,(x-250,y-262))
    fenetre.blit(d.image_inventaire_1(),(45,105))
    fenetre.blit(d.image_inventaire_2(),(45,305))
    clock.tick(FPS)  
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            continuer = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pos()[0] > x-250 and pygame.mouse.get_pos()[0] < x \
            and pygame.mouse.get_pos()[1] > y-262 and pygame.mouse.get_pos()[1] < y:
                v.boucle()
                compteur = random.randint(2,6)        
                change_displayed = False

            if pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[0] < 10+240 \
            and pygame.mouse.get_pos()[1] > y-262 and pygame.mouse.get_pos()[1] < y-262+252:
                d.mettre_dans_inventaire1()

            if pygame.mouse.get_pos()[0] > 10 and pygame.mouse.get_pos()[0] < 10+240 \
            and pygame.mouse.get_pos()[1] > y-262*2 and pygame.mouse.get_pos()[1] < y-(262*2)+252:
                d.mettre_dans_inventaire2()

        if compteur == 1:
            text1_obj = font_obj.render(str(v.nom), True, BLACK)
            fenetre.blit(text1_obj, (x/3.7,y/1.4))
            image_biome=pygame.image.load(image_bio).convert_alpha()
            fenetre.blit(image_biome, (x/2.65, y/7.5))

        #biomes
        if compteur == 2 and not change_displayed:
            change_text_biome = font_obj.render(str(v.change()), True, BLACK)
            change_displayed = True


        if change_displayed and compteur == 2:
            fenetre.blit(change_text_biome, (x / 3.4, y / 1.4))
            image_biome=pygame.image.load(image_bio).convert_alpha()
            fenetre.blit(image_biome, (x/2.65, y/7.5))
        
        #weapons
        if compteur == 3 and not change_displayed:
            change_text_weapon = font_obj.render(str(v.weapons()), True, BLACK)
            change_displayed = True

        if change_displayed and compteur == 3:
            no_more_place=font_obj.render(str(v.change_weapons_first),True, BLACK)
            fenetre.blit(no_more_place, (x / 3.4, y /1.45))
            fenetre.blit(change_text_weapon, (x / 3.4, y / 1.4))
            image_weapon=pygame.image.load(image_weap).convert_alpha()
            fenetre.blit(image_weapon, (x/2.65, y/7.5))

        #foods
        if compteur ==4 and not change_displayed:
            change_text_food = font_obj.render(str(v.food()), True, BLACK)
            change_displayed = True
            
        if change_displayed and compteur == 4:
            no_more_place2=font_obj.render(str(v.change_food_first),True, BLACK)
            fenetre.blit(no_more_place2, (x / 3.4, y /1.45))
            fenetre.blit(change_text_food, (x / 3.4, y / 1.4))
            image_foods=pygame.image.load(image_foo).convert_alpha()
            fenetre.blit(image_foods, (x/2.65, y/7.5))
            
        #animals
        if compteur ==5 and not change_displayed:
            change_text_animal = font_obj.render(str(v.animal()), True, BLACK)
            change_displayed = True
            
        if change_displayed and compteur == 5:
            no_more_place3=font_obj.render(str(v.change_animal_first),True, BLACK)
            fenetre.blit(no_more_place3, (x / 3.4, y /1.45))
            fenetre.blit(change_text_animal, (x / 3.4, y / 1.4))
            image_animal=pygame.image.load(image_an).convert_alpha()
            fenetre.blit(image_animal, (x/2.65, y/7.5))
        
        if compteur== 6 and not change_displayed or compteur== 7 and not change_displayed:
            b=v.rien_a_faire()
            noth1=font_obj.render(str(b[0]), True, BLACK)
            noth2=font_obj.render(str(b[1]), True, BLACK)
            change_displayed = True
        
        if change_displayed and compteur == 6 or change_displayed and compteur == 7:
            fenetre.blit(noth1, (x / 3.4, y /1.45))
            fenetre.blit(noth2, (x / 3.4, y / 1.4))
            
        text2_obj = font_obj.render(str(compteur), True, WHITE, BLACK)
        fenetre.blit(text2_obj, (10,10))
        biome_obj = font_obj.render("Vous etes "+str(v.read_biome_from_csv()), True, WHITE, BLACK)
        fenetre.blit(biome_obj, (30,10))
        
        
        
        
        pygame.display.flip()  
if continuer == False:
    pygame.quit()


