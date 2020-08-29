import pygame, time
import pandas as pd
pygame.init()

h, w = 600, 1000
screen = pygame.display.set_mode((w,h))
df = pd.read_csv('https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv') 
# df = pd.read_csv('colors.csv')

box=[]
for i in range(df.shape[0]):
    row = list(df.iloc[i])
    crgb = row[0], (row[3], row[4], row[5])
    box.append(crgb)
    
running = True
while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    for j in box:
        screen.fill(j[1])
        pygame.display.set_caption(str((j[1])) + ' = ' + j[0])
        pygame.display.flip()
        time.sleep(.5)

pygame.quit()
quit()
