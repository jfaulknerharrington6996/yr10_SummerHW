#space invaders sprite
#by josiah

###imports###
import pygame, sys #this code is importing the 'pygame' plugin to my code

###pygame essentials###
pygame.init() #loading in the pygame plug-in for the code

Display = pygame.display.set_mode([225, 150]) #setting the size of the screen being displaed to the user (resolution)

###colours###

b = pygame.Color("blue") #setting the variable of 'b' to the color blue when useing it to write  a pixel
w = pygame.Color("white")#setting the variable of 'w' to the color white when useing it to leave a gap in the picture

###sprite picture###

SpaceInvader1 = [ #this is the space invader map of the built up pixels in the variables made in 'colours'
    [ w, w, w, b, b, b, w, w, w,], #it is set out into rows and colums for the pixels to be written in
    [ w, w, b, w, b, w, b, w, w,], #in this case a 9x6 table
    [ w, b, w, w, b, w, w, b, w,],
    [ w, b, b, w, w, w, b, b, w,],
    [ w, w, b, b, w, b, b, w, w,],
    [ w, w, w, b, w, b, w, w, w,],
    ]


SpaceInvader2 = [ #this is the space invader map of the built up pixels in the variables made in 'colours'
    [ w, w, w, b, b, b, w, w, w,], 
    [ w, w, b, w, b, w, b, w, w,], 
    [ w, b, w, w, b, w, w, b, w,],
    [ w, b, w, w, w, w, w, b, w,],
    [ w, b, w, w, w, w, w, b, w,],
    [ w, b, w, w, w, w, w, b, w,],
    ]

###changing propities of the sprite###
def draw_SpaceInvader(surface, data):
    for y,row in enumerate(data): #this loop is arranging the SpaceInvader variavble into its rows
        for x, colour in enumerate(row): #this is setting the propites of each pixel, and saying how big one square should be
            rect = pygame.Rect(x*25, y*25, 25, 25) #setting the squares for the pixels as 25 by 25 by 25
            Display.fill(colour, rect = rect) #this displays the picture with the colors

pygame.display.update() #update the game to its screen so it doesnt get stuck when animating

while True: #this loop makes it so the application doesnt end straight away and waits for a user input to close it
    for event in pygame.event.get(): #a loop created so that the game doesnt crash and not let the user to exit 
        if event.type == pygame.QUIT: #this allows the game to be killed if the user uses the 'exit()' code
            sys.exit()
        draw_SpaceInvader(Display, SpaceInvader1) #using the funtion to draw out the first space invader
        pygame.display.update() #this is a code to update the display of the drawing so that it doesnt get stuck
        pygame.time.wait(500) #sets the time for the drawing
        draw_SpaceInvader(Display, SpaceInvader2)#using the draw_spaceinvader funtion to draw out the second space invader
        pygame.display.update() #update the screen display
        pygame.time.wait(500) #sets the timer for the seond drawing
