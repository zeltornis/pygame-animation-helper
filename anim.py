import pygame
from constants import FPS

class Animation:
    def __init__(self, frames, fps=FPS):
        """
        frames: list of pygame.Surface objects
        fps: playback speed (frames per second)
        """
        self.frames = frames
        self.length = len(frames)
        self.fps = fps


class Animator:
    def __init__(self, default_anim: Animation):
        """
        default_anim: the animation to fall back to when stopped
        """
        self.frame_index = 0
        self.default_anim = default_anim
        self.anim = default_anim
        self.looping = True
        self.anim_finished = False
        self.last_frame_time = pygame.time.get_ticks()
        self.start(self.default_anim)
    
    def get_frame(self) -> pygame.Surface:
        """
        Returns the current frame, advancing based on elapsed time.
        """
        now = pygame.time.get_ticks()
        elapsed = now - self.last_frame_time
        frame_duration = 1000 / self.anim.fps # ms per frame

        if elapsed >= frame_duration:
            self.last_frame_time = now
            self.frame_index += 1
            if self.frame_index >= self.anim.length:
                if self.looping:
                    self.frame_index = 0
                else:
                    self.anim_finished = True
                    self.stop()
        
        return self.anim.frames[self.frame_index]

    def start(self, animation: Animation, loop=True):
        self.anim = animation
        self.frame_index = 0
        self.looping = loop
        self.last_frame_time = pygame.time.get_ticks()
        if not loop:
            self.anim_finished = False

    def stop(self):
        self.start(self.default_anim, True)
