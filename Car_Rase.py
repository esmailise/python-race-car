import pygame

# for time
import time

# for random
import random

# start majol
pygame.init()

#crashed_sound
crashed_sound = pygame.mixer.Sound('sounds/crashe.wav')

#car images
carimg = pygame.image.load('images/Cars.png')
car_hostile = pygame.image.load('images/hostile.png')
Truck_hostile = pygame.image.load('images/Truck.png')
cr_width = 60




# width and high for game window
display_width = 800
display_high = 600
gameDisplay = pygame.display.set_mode((display_width, display_high))
pygame.display.set_icon(pygame.image.load('images/logo.png'))


#background_image
bg_img = pygame.image.load('images/Road.png')
bg = pygame.transform.scale(bg_img,(display_width,display_high))

# colors
white = (255, 255, 255)
red = (255, 0, 0)
bright_red = (200, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
yellow = (216, 141, 31)

# title for game window
pygame.display.set_caption('Race Car')

# frame game
clock = pygame.time.Clock()

#button
def button(msg,x,y,w,h,ic,ac,action):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click [0] == 1:
            if action == "Play":
                game_loop()
            elif action == "Quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_object(msg, smallText,white)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextRect)

# login
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(bg,(0,0))
        largeText = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_object("Let's Play Game", largeText, white)
        TextRect.center = ((display_width / 2), (display_high / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("Play", 150, 450, 100, 50, green, bright_green,"Play")
        button("Quit", 550, 450, 100, 50, bright_red,red,"Quit")

        pygame.display.update()

# Score
def stuff_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("score : " + str(count), True, white)
    gameDisplay.blit(text, (70, 25))

def car(x, y):
    gameDisplay.blit(carimg, (x, y))

# for text
def text_object(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# for text crash
def crash(dodged):

    pygame.mixer.Sound.play(crashed_sound)
    stuff_dodged(dodged)
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_object('You Crashed', largeText,yellow)
    TextRect.center = ((display_width / 2), (display_high / 2))
    gameDisplay.blit(TextSurf, TextRect)
    
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Try Again", 150, 450, 100, 50, green, bright_green,"Play")
        button("Quit", 550, 450, 100, 50, bright_red,red,"Quit")

        pygame.display.update()

#crash to car
def crash_to_car(hostile_starty,hostile_height,hostile_startx,x,y,cr_width,hostile_width,dodged):
    if y <= hostile_starty + hostile_height:
        if x >= hostile_startx and x < hostile_startx + hostile_width or x + cr_width > hostile_startx and x + cr_width <= hostile_startx + hostile_width:
            crash(dodged)

def game_loop():

    def hostile(hostilex, hostiley, image):
        gameDisplay.blit(image,(hostilex,hostiley))

    def hostile_hard(hostilex1, hostilex2, hostiley, image1, image2, x, y, cr_width, hostile_width, hostile_height, hostile_h_truck, hostile_w_truck):
        gameDisplay.blit(image1,(hostilex1,hostiley))
        crash_to_car(hostiley, hostile_height, hostilex1, x, y, cr_width, hostile_width,dodged)
        gameDisplay.blit(image2,(hostilex2,hostiley))
        crash_to_car(hostiley, hostile_h_truck, hostilex2, x, y, cr_width, hostile_w_truck,dodged)

    def hostile_very_hard(hostilex1, hostilex2, hostilex3 , hostiley, image1, image2, x, y, car_width, hostile_width, hostile_height, hostile_h_truck, hostile_w_truck):
        #hard
        hostile_hard(hostilex1, hostilex2, hostiley, image1, image2, x, y, car_width, hostile_width, hostile_height, hostile_h_truck, hostile_w_truck) 
        #very Hard
        gameDisplay.blit(image1,(hostilex3,hostiley))
        crash_to_car(hostiley, hostile_height, hostilex3, x, y, car_width, hostile_width,dodged)
        

    x = (display_width * 0.45)
    y = (display_high * 0.8)

    x_change = 0
    i = 0
    dodged = 0
    
    hostile_starty = -600
    hostile_speed = 7

    hostile_height = 134
    hostile_width = 60

    hostile_h_truck = 210
    hostile_w_truck = 100
    height_bg = -600

    random_width = display_width - 85
    random_width_t  = display_width - 215
    # X and Y for level normal
    hostile_startx = random.randrange(25, random_width)
    hostile_startx_t = random.randrange(25, random_width_t)

    # X and Y for level hard 
    hostile_startx1 = random.randrange(25, 320)
    hostile_startx2 = random.randrange(405, 685)

    # X and Y for level very hard
    hostile_startx_vh1 = random.randrange(20, 95)
    hostile_startx_vh2 = random.randrange(180, 370)
    hostile_startx_vh3 = random.randrange(565, 720)

    #crashed
    gameExit = False

    while not gameExit:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            print(event)

            # move car
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change

        # color Background
        gameDisplay.fill(white)    

        #Move Bg
        gameDisplay.blit(bg, (0,i))
        gameDisplay.blit(bg, (0, height_bg+i))

        if i > -height_bg:
            gameDisplay.blit(bg,(0,height_bg+i))
            i = 0

        i += 1

        car(x, y)

        # show hostiles car on display
        if dodged > 19 : 
            hostile_very_hard(hostile_startx_vh1, hostile_startx_vh2, hostile_startx_vh3 , hostile_starty, car_hostile, Truck_hostile, x, y, cr_width, hostile_width,hostile_height,hostile_h_truck,hostile_w_truck)

        if dodged > 9 and dodged < 20 :
             hostile_hard(hostile_startx1, hostile_startx2, hostile_starty, car_hostile, Truck_hostile, x, y, cr_width, hostile_width,hostile_height,hostile_h_truck, hostile_w_truck) 

        if dodged > 4 and dodged < 10 :  
            hostile(hostile_startx_t, hostile_starty, Truck_hostile)
            crash_to_car(hostile_starty, hostile_h_truck, hostile_startx_t, x, y, cr_width, hostile_w_truck,dodged)

        if dodged < 5:
            hostile(hostile_startx, hostile_starty, car_hostile)
            crash_to_car(hostile_starty, hostile_height, hostile_startx, x, y, cr_width, hostile_width,dodged)

        # For up speed
        hostile_starty +=  hostile_speed

        #show_score
        stuff_dodged(dodged)

        # car crashed
        if x > display_width - cr_width - 22 or x < 22:
            crash(dodged)

        # check car hostile passed road
        if hostile_starty > display_high:

            if dodged > 19 : 
                hostile_starty = 0 - hostile_height
                hostile_startx_vh1 = random.randrange(25, 165)
                hostile_startx_vh2 = random.randrange(180, 490)
                hostile_startx_vh3 = random.randrange(510, 720)
                if hostile_startx_vh1+ hostile_width >= hostile_startx_vh2:
                    hostile_startx_vh1  -=65 
                if hostile_startx_vh2 + hostile_w_truck  >= hostile_startx_vh3: 
                    hostile_startx_vh2 -= 80

            if dodged > 9 and dodged < 20:
                hostile_starty = 0 - hostile_height
                hostile_startx1 = random.randrange(20, 335)
                hostile_startx2 = random.randrange(400, 695)

            if dodged > 4 and dodged < 10 : 
                hostile_starty = 0 - hostile_h_truck
                hostile_startx_t = random.randrange(80, random_width_t)

            if dodged < 5 : 
                hostile_starty = 0 - hostile_height
                hostile_startx = random.randrange(80, random_width)
            #level
            dodged = dodged + 1
            if (dodged % 5 == 0):
                hostile_speed = hostile_speed + 1
 
            
        # frame display 
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()

