
from pygame import*
from mixer import mixer



window = display.set_mode((700,500))
display.set_caption("joggin")
background = transform.scale(image.load("ук.avif"),(700,500))
mixer.init()
mixer_music.load("")

clock=time.Clock()
FPS=60

game=True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)

        


