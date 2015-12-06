"""
__          ___          __       ____       ____________   ______     __      __    |||     ______
\ \        / _ \        / /      /    \      |___    ___|  /  __  \   |  |    |  |   |||    / \ |  \
 \ \      / / \ \      / /      /  /\  \         |  |      | /  \_|   |  |____|  |   |||   |   \    |
  \ \    / /   \ \    / /      /  /__\  \        |  |      | |   _    |   ____   |   |||   |--  O --|
   \ \__/ /     \ \__/ /      /  /____\  \       |  |      | \__/ |   |  |    |  |   |||   |   /    |
    \____/       \____/      /__/      \__\      |__|      \______/   |__|    |__|   |||    \___|__/
"""
import pygame
from math import floor
from time import time as time
pygame.init()

#   SCREEN SET   #
screen_size=[500,500]
screen = pygame.display.set_mode(screen_size)

#   COLORS   #
white  = (255 , 255 , 255)
black  = (000 , 000 , 000)
red    = (255 , 000 , 000)
green  = (000 , 255 , 000)
blue   = (000 , 000 , 255)
yellow = (255 , 255 , 000)
purple = (255 , 000 , 255)

#   CAPTION   #
pygame.display.set_icon(pygame.image.load("icon.ico"))
pygame.display.set_caption("Watch")
pygame.mouse.set_visible(0)

#   VARIABLES   #
showTime = [0,0,0]
cursor = pygame.image.load("cursor.png")
imgs = []
for num in range(1,22):
    imgs.append(pygame.image.load(str(num) + ".png"))
    imgs[num - 1].set_colorkey(white)
count = True
state = 0
mili = 0
load = 0
frame = 0
timenow = time()

#   FUNCTIONS   #
def typetext(font, size, text, x, y, alias, color, upside):
    defined_font = pygame.font.Font(font, size)
    stamp = defined_font.render(text, alias, color)
    if upside:
        stamp = pygame.transform.flip(stamp, False, True)
    screen.blit(stamp, [x,y])

def padZero(num,value):
    if int(num) < 10:
        num = '0' + str(num)
    num = str(num)
    if value == 0:
        return num[0]
    elif value == 1:
        return num[1]
    else:
        return num


'''######################################################################################'''

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    screen.fill(white)
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if (pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 100 + 50) and (pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 50 + 400):
                state = 1
                if not count:
                    mili = 34
                timenow = time()
            
            elif (pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 100 + 200) and (pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 50 + 400):
                state = 0
                showTime = [0,0,0]
            
            elif (pygame.mouse.get_pos()[0] > 350 and pygame.mouse.get_pos()[0] < 100 + 350) and (pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 50 + 400):
                state = 0
############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################
############################################################################################################################################################################
                #10HR
            if state == 0:
                if (pygame.mouse.get_pos()[0] > 20 and pygame.mouse.get_pos()[0] < 25 + 20) and (pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 25 + 100):
                    if showTime[0] > 49:
                        showTime[0] -= 50
                    else:
                        showTime[0] += 10
                #01HR
                elif (pygame.mouse.get_pos()[0] > 70 and pygame.mouse.get_pos()[0] < 25 + 70) and (pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 25 + 100):
                    if showTime[0] == 59:
                        showTime[0] = 50
                    elif showTime[0] % 10 == 9:
                        showTime[0] -= 9
                    else:
                        showTime[0] += 1
                #10M
                elif (pygame.mouse.get_pos()[0] > 190 and pygame.mouse.get_pos()[0] < 25 + 190) and (pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 25 + 100):
                    if showTime[1] > 49:
                        showTime[1] -= 50
                    else:
                        showTime[1] += 10
                #01M
                elif (pygame.mouse.get_pos()[0] > 240 and pygame.mouse.get_pos()[0] < 25 + 240) and (pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 25 + 100):
                    
                    if showTime[1] == 59:
                        showTime[1] = 50
                    elif showTime[1] % 10 == 9:
                        showTime[1] -= 9
                    else:
                        showTime[1] += 1
                #10S
                elif (pygame.mouse.get_pos()[0] > 360 and pygame.mouse.get_pos()[0] < 25 + 360) and (pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 25 + 100):
                    if showTime[2] > 49:
                        showTime[2] -= 50
                    else:
                        showTime[2] += 10
                #01S
                elif (pygame.mouse.get_pos()[0] > 410 and pygame.mouse.get_pos()[0] < 25 + 410) and (pygame.mouse.get_pos()[1] > 100 and pygame.mouse.get_pos()[1] < 25 + 100):
                    if showTime[2] == 59:
                        showTime[2] = 50
                    elif showTime[2] % 10 == 9:
                        showTime[2] -= 9
                    else:
                        showTime[2] += 1
############################################################################################################################################################################
############################################################################################################################################################################
                #10H
                elif (pygame.mouse.get_pos()[0] > 20 and pygame.mouse.get_pos()[0] < 25 + 20) and (pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 25 + 200):
                    if showTime[0] == 0:
                        showTime[0] = 50
                    elif showTime[0] > 0 and showTime[0] < 10:
                        showTime[0] = showTime[0] + 40
                    else:
                        showTime[0] -= 10
                elif (pygame.mouse.get_pos()[0] > 70 and pygame.mouse.get_pos()[0] < 25 + 70) and (pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 25 + 200):
                    if showTime[0] % 10 == 0:
                        showTime[0] = floor(showTime[0] / 10) * 10 + 9
                    else:
                        showTime[0] -= 1
                elif (pygame.mouse.get_pos()[0] > 190 and pygame.mouse.get_pos()[0] < 25 + 190) and (pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 25 + 200):
                    if showTime[1] == 0:
                        showTime[1] = 60
                    elif showTime[1] > 0 and showTime[0] < 10:
                        showTime[1] = showTime[0] + 50
                    else:
                        showTime[1] -= 10
                
                elif (pygame.mouse.get_pos()[0] > 240 and pygame.mouse.get_pos()[0] < 25 + 240) and (pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 25 + 200):
                    if showTime[1] % 10 == 0:
                        showTime[1] = floor(showTime[0] / 10) * 10 + 9
                    else:
                        showTime[1] -= 1
                
                elif (pygame.mouse.get_pos()[0] > 360 and pygame.mouse.get_pos()[0] < 25 + 360) and (pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 25 + 200):
                    if showTime[2] == 0:
                        showTime[2] = 60
                    elif showTime[2] > 0 and showTime[0] < 10:
                        showTime[2] = showTime[0] + 50
                    else:
                        showTime[2] -= 10
                
                elif (pygame.mouse.get_pos()[0] > 410 and pygame.mouse.get_pos()[0] < 25 + 410) and (pygame.mouse.get_pos()[1] > 200 and pygame.mouse.get_pos()[1] < 25 + 200):
                    if showTime[2] % 10 == 0:
                        showTime[2] = floor(showTime[0] / 10) * 10 + 9
                    else:
                        showTime[2] -= 1
            if (pygame.mouse.get_pos()[0] > 240 and pygame.mouse.get_pos()[0] < 230 + 240) and (pygame.mouse.get_pos()[1] > 10 and pygame.mouse.get_pos()[1] < 60 + 10):
                count = False
            elif (pygame.mouse.get_pos()[0] > 20 and pygame.mouse.get_pos()[0] < 190 + 20) and (pygame.mouse.get_pos()[1] > 10 and pygame.mouse.get_pos()[1] < 60 + 10):
                count = True


    if state == 1:
        load += 1
        if load == 2:
            load = 0
            frame += 1
        if frame == 21:
            frame = 0
        screen.blit(imgs[frame], [pygame.mouse.get_pos()[0]-16,pygame.mouse.get_pos()[1]-16])
        
        if not count:
            if time() > timenow + 1:
                showTime[2] -= 1
                timenow = time()
            if showTime[2] == -1:
                showTime[2] = 59
                showTime[1] -= 1
            if showTime[1] == -1:
                showTime[1] = 59
                showTime[0] -= 1
            if showTime[0] == -1:
                pygame.mixer.music.load('alarmSound.mp3')
                pygame.mixer.music.play()
                state = 0
                showTime = [0,0,0]

        elif count:
            if time() > timenow + 1:
                timenow = time()
                showTime[2] += 1
            if showTime[2] == 60:
                showTime[2] = 0
                showTime[1] += 1
            if showTime[1] == 60:
                showTime[1] = 0
                showTime[0] += 1

    

    ### START BUTTON ###
    pygame.draw.rect(screen,green,[50,400,100,50])
    typetext("font.TTF", 40, "START", 49, 405, True, black, False)

    ### RESET BUTTON ###
    pygame.draw.rect(screen,yellow,[200,400,100,50])
    typetext("font.TTF", 40, "RESET", 199, 405, True, black, False)

    ### STOP BUTTON ###
    pygame.draw.rect(screen,red,[350,400,100,50])
    typetext("font.TTF", 40, "STOP", 360, 405, True, black, False)
    '''
    \####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\####/\##
    #\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\##/##\#
    ##\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\/####\
    '''
    ### UP HOUR10 BUTTON ###
    pygame.draw.rect(screen,green,[20,100,25,25])
    typetext("font.TTF", 40, "^", 21, 100, True, black, False)
    ### DOWN HOUR10 BUTTON ###
    pygame.draw.rect(screen,red,[20,200,25,25])
    typetext("font.TTF", 40, "^", 21, 185, True, black, True)

    ### UP HOUR1 BUTTON ###
    pygame.draw.rect(screen,green,[70,100,25,25])
    typetext("font.TTF", 40, "^", 71, 100, True, black, False)
    ### DOWN HOUR1 BUTTON ###
    pygame.draw.rect(screen,red,[70,200,25,25])
    typetext("font.TTF", 40, "^", 71, 185, True, black, True)

    '''#########################################################'''
    typetext("font.TTF", 90, ":", 140, 115, True, black, False)
    '''#########################################################'''

    ### UP MINUTE10 BUTTON ###
    pygame.draw.rect(screen,green,[190,100,25,25])
    typetext("font.TTF", 40, "^", 191, 100, True, black, False)
    ### DOWN MINUTE10 BUTTON ###
    pygame.draw.rect(screen,red,[190,200,25,25])
    typetext("font.TTF", 40, "^", 191, 185, True, black, True)

    ### UP MINUTE1 BUTTON ###
    pygame.draw.rect(screen,green,[240,100,25,25])
    typetext("font.TTF", 40, "^", 241, 100, True, black, False)
    ### DOWN MINUTE1 BUTTON ###
    pygame.draw.rect(screen,red,[240,200,25,25])
    typetext("font.TTF", 40, "^", 241, 185, True, black, True)

    '''#########################################################'''
    typetext("font.TTF", 90, ":", 310, 115, True, black, False)
    '''#########################################################'''

    ### UP SECOND10 BUTTON ###
    pygame.draw.rect(screen,green,[360,100,25,25])
    typetext("font.TTF", 40, "^", 361, 100, True, black, False)
    ### DOWN SECOND10 BUTTON ###
    pygame.draw.rect(screen,red,[360,200,25,25])
    typetext("font.TTF", 40, "^", 361, 185, True, black, True)

    ### UP SECOND1 BUTTON ###
    pygame.draw.rect(screen,green,[410,100,25,25])
    typetext("font.TTF", 40, "^", 411, 100, True, black, False)
    ### DOWN SECOND BUTTON ###
    pygame.draw.rect(screen,red,[410,200,25,25])
    typetext("font.TTF", 40, "^", 411, 185, True, black, True)

    typetext("font.TTF", 90, padZero(showTime[0],0), 10, 115, True, black, False)
    typetext("font.TTF", 90, padZero(showTime[0],1), 55, 115, True, black, False)

    typetext("font.TTF", 90, padZero(showTime[1],0), 180, 115, True, black, False)
    typetext("font.TTF", 90, padZero(showTime[1],1), 225, 115, True, black, False)

    typetext("font.TTF", 90, padZero(showTime[2],0), 350, 115, True, black, False)
    typetext("font.TTF", 90, padZero(showTime[2],1), 395, 115, True, black, False)

    if count:
        pygame.draw.rect(screen,blue,[20,10,190,60])
        pygame.draw.rect(screen,black,[240,10,230,60])
    elif not count:
        pygame.draw.rect(screen,black,[20,10,190,60])
        pygame.draw.rect(screen,blue,[240,10,230,60])
    typetext("font.TTF", 40, "COUNT UP", 40, 20, True, (0, 200, 0), False)
    typetext("font.TTF", 40, "COUNT DOWN", 260, 20, True, (0, 200, 0), False)

    if state == 0:
        screen.blit(cursor, pygame.mouse.get_pos())
    else:
        screen.blit(imgs[frame], [pygame.mouse.get_pos()[0]-16,pygame.mouse.get_pos()[1]-16])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
    # --- Limit to 60 frames per second
    clock.tick(100)
