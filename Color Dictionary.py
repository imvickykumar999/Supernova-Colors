import pygame, time
import pandas as pd

pygame.init()
h, w = 600, 1000
screen = pygame.display.set_mode((w,h))

# df = pd.read_csv('https://raw.githubusercontent.com/codebrainz/color-names/master/output/colors.csv') 
df = pd.read_csv('./colors.csv')
dbox, rbox = {}, []

for i in range(df.shape[0]):
    row = list(df.iloc[i])
    crgb = c, rgb = row[0], (row[3], row[4], row[5])
    rbox.append(rgb)
    dbox.update({rgb : c})
rbox.sort()

cbox = []
for m in range(len(rbox)):
    cbox.append(dbox.get(rbox[m]))

fdict = {}
for n in range(len(rbox)):
    fdict.update({cbox[n] : rbox[n]})
    
rdict = dict(reversed(list(fdict.items()))) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    for key in fdict:
        time.sleep(.1)
        screen.fill(fdict[key])
        pygame.display.set_caption(str(fdict[key]) + ' = ' + key)
        pygame.display.flip()
        
pygame.quit()
quit()