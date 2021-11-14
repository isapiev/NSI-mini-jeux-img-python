"""
Programme réalisé par Sapiev, Ibrahim, 1G7
"""
import pygame

essence=0
def G_essence():
    global essence
    essence=1

cle=0
def G_cle():
    global cle
    cle=1

lampe=0
def G_lampe():
    global lampe
    lampe=1

pieddebiche=0
def G_pieddebiche():
    global pieddebiche
    pieddebiche=1

sol=0
def G_sol():
    global sol
    sol=1


#initialisation graphique
pygame.init()
fenetre = pygame.display.set_mode((640, 360))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 20)

image1=pygame.image.load("depart.jpg")
image2=pygame.image.load("arbre-geant.jpg")
image3=pygame.image.load("voiture.jpg")
image20=pygame.image.load("foret20.jpg")
image21=pygame.image.load("foret21.jpg")
image22=pygame.image.load("foret22.jpg")
image23=pygame.image.load("foret23.jpg")
image24=pygame.image.load("foret24.jpg")
image4=pygame.image.load("chemin-vers-cabane.jpg")
image5=pygame.image.load("cabane.jpg")
image6=pygame.image.load("entregrotte.jpg")
image7=pygame.image.load("grotte.jpg")
image8=pygame.image.load("table-foret.jpg")
image9=pygame.image.load("arbre-creux.jpg")
image10=pygame.image.load("cabane-interieur.jpg")
image11=pygame.image.load("sous-grotte1.jpg")
image12=pygame.image.load("sous-grotte-chemin.jpg")
image13=pygame.image.load("echelle.jpg")
image14=pygame.image.load("squelette.jpg")
image15=pygame.image.load("fin.jpg")



text1 = font.render("Vous vous réveillez dans une forêt immense", True, (255,255,255),(0, 0, 0))
text2 = font.render("Vous vous trouvez devant un  arbre gigantesque", True, (255,255,255),(0, 0, 0))
text3 = font.render("Vous vous trouvez devant une voiture, impossible a démarrer", True, (255,255,255),(0, 0, 0))
text20 = font.render("Vous êtes dans un passage banal de la forêt", True, (255,255,255),(0, 0, 0))
text21 = font.render("Vous êtes dans un passage banal de la forêt", True, (255,255,255),(0, 0, 0))
text22 = font.render("Vous êtes dans un passage banal de la forêt", True, (255,255,255),(0, 0, 0))
text23 = font.render("Vous êtes dans un passage banal de la forêt", True, (255,255,255),(0, 0, 0))
text24 = font.render("Vous êtes dans un passage banal de la forêt", True, (255,255,255),(0, 0, 0))
text4 = font.render("vous vous retrouvez devant un chemin", True, (255,255,255),(0, 0, 0))
text5 = font.render("vous êtes devant une cabane barricader", True, (255,255,255),(0, 0, 0))
text6 = font.render("Vous êtes devant une grotte, il fait trop sombre pour avancer", True, (255,255,255),(0, 0, 0))
text7 = font.render("Vous êtes entrer la grotte, le sol semble fragile", True, (255,255,255),(0, 0, 0))
text8 = font.render("vous trouvez devant des tables", True, (255,255,255),(0, 0, 0))
text9 = font.render("Vous êtes devant un arbre creux", True, (255,255,255),(0, 0, 0))
text10 = font.render("Vous êtes dans la cabane", True, (255,255,255),(0, 0, 0))
text38 = font.render("Vous avez trouver un pied de biche", True, (255,255,255),(0, 0, 0))
text39 = font.render("Vous avez trouver de l'essence", True, (255,255,255),(0, 0, 0))
text40 = font.render("Vous avez trouver une lampe torche", True, (255,255,255),(0, 0, 0))
text11 = font.render("le sol vien de s'éffondre vous vous retrouver sous la grotte", True, (255,255,255),(0, 0, 0))
text12 = font.render("vous trouvez un chemin", True, (255,255,255),(0, 0, 0))
text13 = font.render("vous êtes devant une echelle", True, (255,255,255),(0, 0, 0))
text14 = font.render("vous trouvez un squelette", True, (255,255,255),(0, 0, 0))
text44 = font.render("vous avez trouver une cle dans le squelette", True, (255,255,255),(0, 0, 0))
text33 = font.render("il vous faut sa clé et de l'essece pour l'utiliser", True, (255,255,255),(0, 0, 0))
text15 = font.render("BIEN JOUER vous vous êtes enfuit, appuyer sur 'e' pour quitter", True, (255,255,255),(0, 0, 0))
text37 = font.render("il n'y a rien ici", True, (255,255,255),(0, 0, 0))

dansQuellePierceEstLePersonnage=1


def decrireLaPiece(piece):
    if piece==1:
        fenetre.blit(image1,(0,0))
        fenetre.blit(text1,(0,300))
    elif piece==2:
        fenetre.blit(image2,(0,0))
        fenetre.blit(text2,(0,300))
    elif piece==3:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text3,(0,300))
    elif piece==20:
        fenetre.blit(image20,(0,0))
        fenetre.blit(text20,(0,300))
    elif piece==21:
        fenetre.blit(image21,(0,0))
        fenetre.blit(text21,(0,300))
    elif piece==22:
        fenetre.blit(image22,(0,0))
        fenetre.blit(text22,(0,300))
    elif piece==23:
        fenetre.blit(image23,(0,0))
        fenetre.blit(text23,(0,300))
    elif piece==24:
        fenetre.blit(image24,(0,0))
        fenetre.blit(text24,(0,300))
    elif piece==4:
        fenetre.blit(image4,(0,0))
        fenetre.blit(text4,(0,300))
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(0,300))
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(0,300))
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(0,300))
    elif piece==8:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(0,300))
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(0,300))
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(0,300))
    elif piece==38:
        fenetre.blit(image8,(0,0))
        fenetre.blit(text38,(0,300))
    elif piece==39:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text39,(0,300))
    elif piece==40:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text40,(0,300))
    elif piece==11:
        fenetre.blit(image11,(0,0))
        fenetre.blit(text11,(0,300))
    elif piece==12:
        fenetre.blit(image12,(0,0))
        fenetre.blit(text12,(0,300))
    elif piece==13:
        fenetre.blit(image13,(0,0))
        fenetre.blit(text13,(0,300))
    elif piece==14:
        fenetre.blit(image14,(0,0))
        fenetre.blit(text14,(0,300))
    elif piece==15:
        fenetre.blit(image15,(0,0))
        fenetre.blit(text15,(0,300))
    elif piece==44:
        fenetre.blit(image14,(0,0))
        fenetre.blit(text44,(0,300))
    elif piece==33:
        fenetre.blit(image3,(0,0))
        fenetre.blit(text33,(0,300))
    elif piece==37:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text37,(0,300))


def decision(direction,piece):
    print("Vous désirez allez au",direction)
    memorisePiece=piece
    if direction=='m':
        if piece==13:
            piece=10
        elif piece==10:
            if sol==1:
                piece=13
    elif direction=='c':
        if piece==8:
            if pieddebiche==0:
                piece=38
                G_pieddebiche()
            else:
                print("vous avez déjà fouiller")
        elif piece==9:
            if essence==0:
                piece=39
                G_essence()
            else:
                print("vous avez déjà fouiller")
        elif piece==10:
            if lampe==0:
                piece=40
                G_lampe()
            else:
                print("vous avez déjà fouiller")
        elif piece==14:
            if cle==0:
                G_cle()
                piece=44
            else:
                print("vous avez déjà fouiller")
        elif piece==3:
            if cle==0 or essence==0:
                print("il manque quelque chose")
            elif cle==1 and essence==1:
                piece=15
        elif piece==7:
            piece=37
    else:
        print("il n'y a rien a trouver")

    if direction=='z':
        if piece==1:
            piece=2
        elif piece==3:
            piece=20
        elif piece==20:
            piece=8
        elif piece==2:
            piece=21
        elif piece==21:
            piece=6
        elif piece==24:
            piece=23
        elif piece==23:
            piece=22
        elif piece==22:
            piece=4
        elif piece==5 :
            if pieddebiche==0:
                print("Impossible a ouvrir à main nue")
            else:
                piece=10
        elif piece==6:
            if lampe==0:
                print("il fait trop smbre pour avancez")
            elif lampe==1 and sol==0:
                piece=7
            elif lampe==1 and sol==1:
                print("le sol c'est effondré impossibe d'avancé")
    elif direction=='s':
        if piece==2:
            piece=1
        elif piece==20:
            piece=3
        elif piece==23:
            piece=24
        elif piece==8:
            piece=20
        elif piece==21:
            piece=2
        elif piece==6:
            piece=21
        elif piece==22:
            piece=23
        elif piece==4:
            piece=22
        elif piece==38:
            piece=20
        elif piece==10:
            piece=5
        elif piece==40:
            piece=5
        elif piece==7:
            G_sol()
            piece=11
        elif piece==37:
            G_sol()
            piece=11
    elif direction=='d':
        if piece==3:
            piece=1
        elif piece==20:
            piece=2
        elif piece==8:
            piece=21
        elif piece==1:
            piece=24
        elif piece==2:
            piece=23
        elif piece==21:
            piece=22
        elif piece==23:
            piece=9
        elif piece==4:
            piece=5
        elif piece==38:
            piece=21
        elif piece==11:
            piece=12
        elif piece==12:
            piece=13
        elif piece==14:
            piece=11
        elif piece==44:
            piece=11
    elif direction=='q':
        if piece==1:
            piece=3
        elif piece==2:
            piece=20
        elif piece==21:
            piece=8
        elif piece==22:
            piece=21
        elif piece==23:
            piece=2
        elif piece==24:
            piece=1
        elif piece==9:
            piece=23
        elif piece==5:
            piece=4
        elif piece==39:
            piece=23
        elif piece==11:
            piece=14
        elif piece==12:
            piece=11
        elif piece==13:
            piece=12
    if memorisePiece==piece:
        print("Déplacement impossible")
    else:
        print("C'est possible")
    return piece


print("Voici les touches:")
print('Z = Nord')
print('D = Est')
print('S = Sud')
print('Q = Ouest')
print('C = Chercher/Utiliser')
print('M = Monter/Descendre')

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.KEYDOWN:
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'e':
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
    pygame.display.flip()
pygame.quit()

