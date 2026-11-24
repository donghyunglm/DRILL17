from pico2d import *
import random
import game_world
import game_framework
from boy import Boy
from grass import Grass
from ball import Ball
from zombie import Zombie


boy = None
balls = []
zombies = []


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
            return

        else:
            boy.handle_event(event)


def init():
    global boy, balls, zombies

    game_world.clear()

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)

    # 바닥에 정지된 공 30개 배치
    balls = [
        Ball(random.randint(100, 1600 - 100), 60, 0)
        for _ in range(30)
    ]

    game_world.add_objects(balls, 1)

    # 소년과 공 충돌 그룹 등록
    game_world.add_collision_pair('boy:ball', boy, None)

    for ball in balls:
        game_world.add_collision_pair(
            'boy:ball', None, ball
        )

    # 바닥과 공 충돌 그룹 등록
    game_world.add_collision_pair(
        'grass:ball', grass, None
    )

    # 좀비 4마리 추가
    zombies = [Zombie() for _ in range(4)]
    game_world.add_objects(zombies, 1)

    game_world.add_collision_pair('boy:zombie', boy, None)


def pause():
    boy.pause()


def resume():
    pass


def finish():
    global boy, balls, zombies

    game_world.clear()

    boy = None
    balls = []
    zombies = []


def update():
    game_world.update()
    game_world.handle_collisions()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()
