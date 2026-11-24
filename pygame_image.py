import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg") #練習問題1

    bg_hanten_img = pg.transform.flip(bg_img, True, False)#8

    kouka_img = pg.image.load("fig/3.png")#3
    kouka_img = pg.transform.flip(kouka_img, True, False)#4
    kouka_rct = kouka_img.get_rect()#10
    kouka_rct.center = 300, 200#10

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        key_list = pg.key.get_pressed()

        kouka_rct.move_ip((-1, 0))

        if key_list[pg.K_UP]: #上矢印が押されていたら
            kouka_rct.move_ip((0, -1))#横が0、縦に―1
        if key_list[pg.K_DOWN]: 
            kouka_rct.move_ip((0, +1))
        if key_list[pg.K_LEFT]: 
             kouka_rct.move_ip((-1, 0))
        if key_list[pg.K_RIGHT]:
            kouka_rct.move_ip((2, 0))

        t = tmr%3200 
        screen.blit(bg_img, [-t, 0])#5
        screen.blit(bg_hanten_img, [-t+1600, 0])#7
        screen.blit(bg_img, [-t+3200, 0])#9

        # screen.blit(kouka_img, [-t, 0])
        # screen.blit(kouka_img, [-t+1600, 0])

        screen.blit(kouka_img, kouka_rct)#3
        
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()