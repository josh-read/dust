from environment import Environment
from graphics import Graphics


def runner(env: Environment, f=50):
    """Opens a pygame window and runs simulation forever.

    Pygame window is initialised and updated once every 'f' iterations
    that the simulation runs. Simulation can be closed with ESC key or
    by clicking on the window close button."""

    g = Graphics()
    i = 0
    while True:
        i += 1
        env.step()
        if i % f == 0:
            i = 0
            g.update(env.particles)
