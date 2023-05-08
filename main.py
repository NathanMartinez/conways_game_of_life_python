import sys
import pygame as pg
from settings import *
from board import Board

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 0
        self.running = True
        self.board = Board(self)
        self.font = pg.font.Font(None, 28)
        self.paused = True
        self.pause_text = self.font.render("Paused", True, FONT_COLOR)
        self.pause_text_rect = self.pause_text.get_rect(topright=(RES[0] - 10, 10))
        self.fps = 60
        self.previous_fps = STARTING_FPS
        self.min_fps = 1
        self.max_fps = 60
        pg.display.set_caption("Conway's Game of Life")
        
    def quit_game(self):
        self.running = False
        pg.quit()
        sys.exit()
        
    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit_game()

            elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                self.board.check_clicks(event)

            elif event.type == pg.KEYDOWN:
                self.handle_keydown_event(event)

        self.handle_key_presses()

    def handle_keydown_event(self, event):
        if event.key == pg.K_SPACE:
            self.toggle_pause()
        elif event.key == pg.K_r:
            self.board.generate_random_board()
        elif event.key == pg.K_c:
            self.board.generate_checker_board()
        elif event.key == pg.K_e:
            self.board.generate_empty_board()

    def handle_key_presses(self):
        if self.paused:
            return
        
        keys = pg.key.get_pressed()
        
        if keys[pg.K_LEFT]:
            self.decrease_fps()
        elif keys[pg.K_RIGHT]:
            self.increase_fps()

    def toggle_pause(self):
        if not self.paused:
            self.previous_fps = self.fps
            self.fps = 60
            self.paused = True
        else:
            self.fps = self.previous_fps
            self.paused = False

    def decrease_fps(self):
        self.fps = max(self.fps - 1, self.min_fps)

    def increase_fps(self):
        self.fps = min(self.fps + 1, self.max_fps)


    def run(self):
        while self.running:
            self.handle_events()
            
            self.screen.fill(pg.Color(BACKGROUND_COLOR))
            
            if not self.paused:
                self.board.update()

            self.board.display()
            
            if self.paused:
                self.screen.blit(self.pause_text, self.pause_text_rect)
            
            fps_text = self.font.render("FPS: {}".format(self.fps), True, FONT_COLOR)
            self.screen.blit(fps_text, (10, 10))

            pg.display.flip()

            self.delta_time = self.clock.tick(self.fps) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
