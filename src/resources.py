import pygame
import os

def load_images():
    paths = os.walk(os.path.join("data", "images"))
    
    images = {}


    for i in paths:
        for j in i[2]:
            if j[-4:] == ".png":
                images[os.path.join(i[0], j)] = pygame.image.load(os.path.join(i[0], j))
    
    return images

IMAGES = load_images()
