from PIL import Image

img = Image.open('color.png')
pixels = img.load() 

width, height = img.size
# color_json={}
for x in range(width):
    for y in range(height):
        rgb = r, g, b = pixels[x, y]
        # color_json.update({ f'{x},{y}' : rgb })
        print(x,y,rgb)
