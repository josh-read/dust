import argparse

from environment import Environment
from runner import runner


def get_parser():
    """Returns parser object to retrieve command line argunents."""

    parser = argparse.ArgumentParser(description="Run dust simulation.")
    parser.add_argument(
            '-n',
            '--number',
            type=int,
            default=5,
            help="number of particles to be simulated",
            )
    parser.add_argument(
            '-l',
            '--ang-mom',
            type=float,
            default=0,
            help="total angular momentum of the system",
            )
    parser.add_argument(
            '-g',
            '--gravity',
            type=float,
            default=0.1,
            help="set the strength of attractive force between particles",
            )
    parser.add_argument(
            '-rho',
            '--density',
            type=float,
            default=0.2,
            help="set the particle density",
            )
    return parser


def main():
    """Parse command line arguments and run simulation."""

    # Set up parser and get arguments
    parser = get_parser()
    args = vars(parser.parse_args())

    # Retrieve number of particles and angular momentum
    n = args.pop('number')
    l = args.pop('ang_mom')

    # Assign the rest to kwargs
    kwargs = args

    # Create environment and run simulation
    env = Environment.rotating(n, l, **kwargs)
    runner(env)


if __name__ == '__main__':
    main()
