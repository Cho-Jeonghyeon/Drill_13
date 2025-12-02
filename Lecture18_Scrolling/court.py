from pico2d import load_image, get_canvas_width, get_canvas_height, clamp
import common
import random
import game_world

class Court:
    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        # fiil here
        self.w=self.image.w
        self.h=self.image.h

        #공 랜덤 배치
        self.balls = [Ball(random.randint(0, self.w - 1), random.randint(0, self.h - 1)) for _ in range(100)]

    def update(self):

        self.window_left = clamp(0, int(common.boy.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(common.boy.y) - self.ch // 2, self.h - self.ch - 1)
        pass

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)


class TileCourt:
    def __init__(self):
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()

        # fill here


    def update(self):
        self.window_left = clamp(0, int(common.boy.x) - self.cw // 2, self.w - self.cw - 1)
        self.window_bottom = clamp(0, int(common.boy.y) - self.ch // 2, self.h - self.ch - 1)

    def draw(self):
        self.image.clip_draw_to_origin(self.window_left, self.window_bottom, self.cw, self.ch, 0, 0)
        # fill here


class InfiniteCourt:

    def __init__(self):
        self.image = load_image('futsal_court.png')
        self.cw = get_canvas_width()
        self.ch = get_canvas_height()
        self.w = self.image.w
        self.h = self.image.h

    def draw(self):
        self.image.clip_draw_to_origin(self.q3l, self.q3b, self.q3w, self.q3h, 0, 0)                        # quadrant 3
        # fill here

    def update(self):
        # quadrant 3
        self.q3l = (int(common.boy.x) - self.cw // 2) % self.w
        self.q3b = (int(common.boy.y) - self.ch // 2) % self.h
        self.q3w = clamp(0, self.w - self.q3l, self.w)
        self.q3h = clamp(0, self.h - self.q3b, self.h)
        # quadrant 2
        self.q2l = 0
        self.q2b = 0
        self.q2w = 0
        self.q2h = 0
        # quadrand 4
        self.q4l = 0
        self.q4b = 0
        self.q4w = 0
        self.q4h = 0
        # quadrand 1
        self.q1l = 0
        self.q1b = 0
        self.q1w = 0
        self.q1h = 0


    def handle_event(self, event):
        pass

class Ball:
    image = None

    def __init__(self, x, y):
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')
        self.x = x
        self.y = y

    def draw(self):
        # court의 현재 창 좌표를 사용해 화면 위치 계산
        sx = self.x - common.court.window_left
        sy = self.y - common.court.window_bottom
        Ball.image.draw(sx, sy)

    def update(self):
        pass


    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def handle_collision(self, group, other):
        # boy와 충돌하면 게임 월드에서 제거
        if group == 'boy:ball':
            game_world.remove_object(self)
            common.court.balls.remove(self)

