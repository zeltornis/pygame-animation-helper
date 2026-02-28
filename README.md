# Simple Pygame Animation Helper

This is a minimal animation system built on top of [pygame](https://www.pygame.org/).  
It’s designed for students who want a simple way to add sprite animations to their games.

## Features
- Define animations as lists of frames (`pygame.Surface` objects).
- Play animations with custom FPS.
- Support for looping and one-shot animations.
- Easy to integrate into the game loop.

## Example Usage

```python
import pygame
from animation import Animation, Animator

# Load frames (replace with your own images)
frames = [pygame.image.load(f"frame_{i}.png") for i in range(4)]

# Create an animation
walk_anim = Animation(frames, fps=10)

# Create an animator
animator = Animator(walk_anim)

# In your game loop:
screen.blit(animator.get_frame(), (100, 100))
```

## Classes

### Animation
Represents a sequence of frames.
- frames: list of pygame.Surface objects
- fps: playback speed (frames per second)

### Animator
Controls playback of an Animation.

- get_frame(): returns the current frame and advances the animation
- start(animation, loop=True): starts a new animation
- stop(): resets to the default animation
- anim_finished: flag indicating if a non-looping animation has ended

## Notes
Relies on a constants.py file where global project constants are declared.
It expects there to be an FPS constant defined in constants.py.

Also, in the current state, doesn't handle delta-time. 

Great for learning, prototyping, or small projects.

Feel free to extend it with features like time-based updates, reverse playback, event callbacks when animations finish.

## License
MIT License – free to use, modify, and share.