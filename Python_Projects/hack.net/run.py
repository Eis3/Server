# PyGame template.

# Import standard modules.
import sys

# Import non-standard modules.
import pygame
from pygame.locals import *


def load():
    global wallpaper, cursor
    pygame.mouse.set_visible(False)
    wallpaper = pygame.image.load("wallpaper.png")
    cursor = pygame.image.load("cursor.png")


def update(dt):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
        if event.type == QUIT:
            pygame.quit()  # Opposite of pygame.init
            sys.exit()  # Not including this line crashes the script on Windows. Possibly
        if event.type == KEYDOWN:
            pygame.quit()
            sys.exit()
        # on other operating systems too, but I don't know for sure.
        # Handle other events as you wish.


def draw(screen):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0))  # Fill the screen with black.
    screen.blit(wallpaper, (0, 0))
    screen.blit(cursor, pygame.mouse.get_pos())

    # Redraw screen here.

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()


def runPyGame():
    # Initialise PyGame.
    pygame.init()

    # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
    fps = 30.0
    fpsClock = pygame.time.Clock()

    # Set up the window.
    width, height = 1920, 1080
    screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
    # screen is the surface representing the window.
    # PyGame surfaces can be thought of as screen sections that you can draw onto.
    # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.

    # Main game loop.
    dt = 1 / fps  # dt is the time since last frame.
    load()
    while True:  # Loop forever!
        update(dt)  # You can update/draw here, I've just moved the code for neatness.
        draw(screen)
        print(dt)
        dt = fpsClock.tick(fps)


if __name__ == "__main__":
    runPyGame()