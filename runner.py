import argparse
import contextlib

from environment import Environment
with contextlib.redirect_stdout(None):
    from graphics import Graphics


def run_sim(env: Environment):
    """Opens a pygame window and runs simulation.

    Pygame window is initialised and updated once every 50 iterations that the
    simulation runs. After 20000 iterations close the window closes again."""

    g = Graphics()
    for i in range(20000):
        env.move()
        env.collisions()
        if i % 50 == 0:
            g.update(env.particles)
    g.close()


def main():
    """Parse command line arguments and run simulation."""

    # Set up parser
    parser = argparse.ArgumentParser(description="Run dust simulation.")
    parser.add_argument(
            '-n',
            type=int,
            default=5,
            help="number of particles to be simulated",
            )

    # Parse arguments
    args = parser.parse_args()

    # Create environment and run simulation
    env = Environment.random_static(args.n)
    run_sim(env)


if __name__ == '__main__':
    main()
