import world
import pygame as py
from constants import*
import graphic

# we generate a new world
newWorld = world.World()
#newWorld.test_automata()

FPS = 30

WIN = py.display.set_mode((WIDTH, HEIGHT))
newGraphic = graphic.Graphic(WIN)
py.display.set_caption("FLUID AUTOMATA")


def get_row_col_from_mouse(pos):
    # here we translate from pixels to board position
    x, y = pos
    row = y // ASIZE
    
    col = x // ASIZE
    return row, col

def main():
    run = True
    clock = py.time.Clock()
    running_simulation = False

    while run:
        clock.tick(FPS)

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_SPACE:
                    running_simulation = not(running_simulation) 
        
            if event.type == py.MOUSEBUTTONDOWN:
                particle_type = py.mouse.get_pressed()
                pos = py.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                newWorld.make_alive(row, col, particle_type)

        if running_simulation:
            newWorld.live_one_step()
            newGraphic.draw_automatas(newWorld.grid)
    py.quit()

main()
