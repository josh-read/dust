from particle import Particle

DT = 1  # Our timestep


class Environment:

    def __init__(self, particles: list):
        self.particles = particles

    def collisions(self):
        """Function checks for collisions between particles and merges
        colliding particles."""
        for i, current in enumerate(self.particles):
            for j, other in enumerate(self.particles):
                if i == j:
                    pass
                else:
                    if current % other:
                        # add other particle to current
                        self.particles[i] = current + other
                        # delete other particle from list
                        del self.particles[j]
                    else:
                        pass

    def move(self):
        for particle in self.particles:
            particle.update(self.particles, DT)

    @classmethod
    def random_static(cls, n: int):
        particles = []
        for i in range(n):
            particles.append(Particle.random_static())
        return cls(particles)
