import pygame

pygame.init()

# creation de la fenêtre
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("My SokoBan")
outsideBlockIni = pygame.image.load('./assets/block.PNG').convert_alpha()
outsideBlock = pygame.transform.scale(outsideBlockIni, (50, 50))
marioLeftIni = pygame.image.load('./assets/mario-left.png')
marioLeft = pygame.transform.scale(marioLeftIni, (50, 50))
flatBlockIni = pygame.image.load('./assets/flat-block.PNG').convert_alpha()
flatBlock = pygame.transform.scale(flatBlockIni, (50, 50))
caisseIni = pygame.image.load('./assets/caisse.PNG').convert_alpha()
caisse = pygame.transform.scale(caisseIni, (50, 50))
caisseOkIni = pygame.image.load('./assets/caisseok.PNG').convert_alpha()
caisseOk = pygame.transform.scale(caisseOkIni, (50, 50))
grassIni = pygame.image.load('./assets/grass.png').convert_alpha()
grass = pygame.transform.scale(grassIni, (50, 50))
# numéro touche

# boucle du jeu
running = True

# map
gameMap = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 1],
    [1, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 1],
    [1, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 20, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
];
gameMapIni = gameMap


def moveCharacter(move, axis):
    print(axis)
    if axis == 'x':
        print(gameMap[marioX + move + move][marioY])
        if gameMap[marioX + move][marioY] == 5:
            if gameMap[marioX + move + move][marioY] == 20:
                gameMap[marioX + move][marioY] == 0
                gameMap[marioX + (move + move)][marioY] = 50
                gameMap[marioX][marioY] = 0
                gameMap[marioX + move][marioY] = 99
            elif gameMap[marioX + move + move][marioY] == 1:
                print('out of range')
            else:
                gameMap[marioX + move][marioY] == 0
                gameMap[marioX + (move + move)][marioY] = 5
                gameMap[marioX][marioY] = 0
                gameMap[marioX + move][marioY] = 99
        elif gameMap[marioX + move][marioY] == 5 and gameMap[marioX + move + move][marioY] == 1:
            print('caisse mur')
        elif 14 > marioX + move >= 1 and gameMap[marioX + move][marioY] != 20 and gameMap[marioX + move][marioY] != 50:
            gameMap[marioX][marioY] = 0
            gameMap[marioX + move][marioY] = 99
        else:
            print('out of range')
    elif axis == 'y':
        print(marioY + move)
        if gameMap[marioX][marioY + move] == 5:
            if gameMap[marioX][marioY + move + move] == 20:
                gameMap[marioX][marioY + move] == 0
                gameMap[marioX][marioY + (move + move)] = 50
                gameMap[marioX][marioY] = 0
                gameMap[marioX][marioY + move] = 99
            elif gameMap[marioX][marioY + move + move] == 1:
                print('out of range')
            else:
                gameMap[marioX][marioY + move] == 0
                gameMap[marioX][marioY + (move + move)] = 5
                gameMap[marioX][marioY] = 0
                gameMap[marioX][marioY + move] = 99
        elif gameMap[marioX][marioY + move] == 5 and gameMap[marioX][marioY + move + move] == 1:
            print('caisse mur')
        elif 14 > marioY + move >= 1 and gameMap[marioX][marioY + move] != 20 and gameMap[marioX][marioY + move] != 50:
            gameMap[marioX][marioY] = 0
            gameMap[marioX][marioY + move] = 99
        else:
            print('out of range')


while running:
    for i in range(0, 15):
        for j in range(0, 15):
            if gameMap[i][j] == 1:
                screen.blit(outsideBlock, (50 * i, 50 * j))
            elif gameMap[i][j] == 99:
                screen.blit(marioLeft, (50 * i, 50 * j))
                marioX = i
                marioY = j
            elif gameMap[i][j] == 5:
                screen.blit(caisse, (50 * i, 50 * j))
            elif gameMap[i][j] == 50:
                screen.blit(caisseOk, (50 * i, 50 * j))
            elif gameMap[i][j] == 20:
                screen.blit(flatBlock, (50 * i, 50 * j))
            elif gameMap[8][2] == 50 and gameMap[2][11] == 50 and gameMap[6][3] == 50 and gameMap[12][8] == 50:
                font = pygame.font.Font('freesansbold.ttf', 25)
                text = font.render("You win, appuyer sur esc pour quitter!", True, (255, 255, 255))
                screen.blit(text, (320, 320))
            else:
                screen.blit(grass, (50 * i, 50 * j))
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif gameMap[8][2] == 50 and gameMap[2][11] == 50 and gameMap[6][3] == 50 and gameMap[12][8] == 50:
            print(event.type)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        else:
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_SPACE:
                    print('space')
                    i=0
                if event.key == pygame.K_LEFT:
                    moveCharacter(-1, 'x')
                elif event.key == pygame.K_RIGHT:
                    moveCharacter(+1, 'x')
                elif event.key == pygame.K_UP:
                    moveCharacter(-1, 'y')
                elif event.key == pygame.K_DOWN:
                    moveCharacter(+1, 'y')
pygame.quit()
