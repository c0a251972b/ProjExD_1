import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習問題1

    kouka_img = pg.image.load("fig/3.png")#3
    kouka_img = pg.transform.flip(kouka_img, True, False)#4

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        t = tmr
        screen.blit(bg_img, [-t, 0])

        screen.blit(kouka_img, [300, 200])#3

        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()