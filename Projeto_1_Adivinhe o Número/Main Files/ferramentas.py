def aleatorio(a, b):
    from random import randint
    ale = randint(a, b)
    return ale


def titulo(msg):
    l = len(msg) + 8
    print("-" * l)
    print(f"    {msg}")
    print("-" * l)


def linha(msg):
    l = len(msg) + 4
    print("-" * l)
    print(f"  {msg}")
    print("-" * l)


def prin(msg):
    l = len(msg) + 50
    print("\033[1;32m")
    print("-" * l)
    print(f"                         {msg}")
    print("-" * l)
    print("\033[m")


def musica():
    import pygame
    pygame.mixer.init()
    pygame.mixer.music.load("Lofi.mp3")
    pygame.mixer.music.play()
    
