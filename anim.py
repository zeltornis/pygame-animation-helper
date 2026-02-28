import pygame
from constants import FPS

class Animation:
    def __init__(self, frames, fps = FPS):
        self.frames = frames
        self.length = len(frames)
        self.fps = fps


class Animator:
    def __init__(self, default_anim: Animation):
        self.frame = 0
        self.default_anim = default_anim
        self.anim = default_anim
        self.looping = True
        self.anim_finished = False
        self.start(self.default_anim)
    
    def get_frame(self) -> pygame.Surface:
        self.frame += self.anim.fps / FPS
        if self.frame >= self.anim.length:
            if self.looping:
                self.frame = 0
            else:
                self.anim_finished = True
                self.stop()
        return self.anim.frames[int(self.frame)]

    def start(self, animation: Animation, loop = True):
        self.anim = animation
        self.frame = 0
        self.looping = loop
        if not loop:
            self.anim_finished = False

    def stop(self):
        self.start(self.default_anim, True)
