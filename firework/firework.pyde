# Fireworks simulation — Processing (Python mode)
# Paste this into Processing (choose Python mode) and run.

fireworks = []          # list of active Firework objects
gravity = 0.18          # gravity applied to every particle

# -------------------------
# Particle: single spark (or the rocket)
# -------------------------
class Particle:
    def __init__(self, x, y, col, vx=None, vy=None, firework=False):
        self.x = x
        self.y = y
        self.col = col              # tuple (r,g,b)
        self.firework = firework    # True = rocket (not a spark)
        # velocity: use provided or random
        if vx is not None:
            self.vx = vx
        else:
            self.vx = random(-2, 2)
        if vy is not None:
            self.vy = vy
        else:
            self.vy = random(-2, 2)
        # if this is the main rocket, force strong upward velocity
        if self.firework:
            self.vx = 0
            self.vy = random(-11, -8)
        self.lifespan = 255         # alpha for fading sparks

    def update(self):
        # gravity affects vertical velocity
        self.vy += gravity
        # update position
        self.x += self.vx
        self.y += self.vy
        # sparks fade, rocket does not fade quickly
        if not self.firework:
            self.lifespan -= 4

    def show(self):
        noStroke()
        # Use RGBA (alpha = lifespan) for fading
        fill(self.col[0], self.col[1], self.col[2], max(0, self.lifespan))
        ellipse(self.x, self.y, 4, 4)

    def is_dead(self):
        return self.lifespan <= 0

# -------------------------
# Firework: one rocket + its explosion sparks
# -------------------------
class Firework:
    def __init__(self, x=None):
        # random color for the explosion
        self.col = (random(255), random(255), random(255))
        self.x = x if x is not None else random(width)
        # the rocket particle that goes up
        self.rocket = Particle(self.x, height, self.col, firework=True)
        self.exploded = False
        self.particles = []   # holds post-explosion sparks

    def update(self):
        if not self.exploded:
            # update rocket until it slows and begins to fall
            self.rocket.update()
            # when rocket's vertical velocity becomes >= 0 => it peaked -> explode
            if self.rocket.vy >= 0:
                self.explode()
        else:
            # update all sparks and remove dead ones
            for p in self.particles:
                p.update()
            self.particles = [p for p in self.particles if not p.is_dead()]

    def explode(self):
        self.exploded = True
        n = 80  # number of sparks (reduce this to improve performance)
        for i in range(n):
            angle = random(TWO_PI)           # direction
            speed = random(1.5, 6.0)         # initial speed
            vx = cos(angle) * speed
            vy = sin(angle) * speed
            # create spark at rocket position with computed velocity
            self.particles.append(Particle(self.rocket.x, self.rocket.y, self.col, vx, vy, firework=False))

    def show(self):
        if not self.exploded:
            self.rocket.show()
        else:
            for p in self.particles:
                p.show()

    def is_dead(self):
        # dead when exploded and no sparks remain
        return self.exploded and len(self.particles) == 0

# -------------------------
# Processing setup & draw
# -------------------------
def setup():
    size(900, 600)
    colorMode(RGB, 255, 255, 255, 255)  # allow alpha in fill/background
    background(0)
    smooth()

def draw():
    # draw a translucent black rectangle for trailing effect (gives glowing trails)
    noStroke()
    fill(0, 0, 0, 25)
    rect(0, 0, width, height)

    # occasionally launch a new random firework
    if random(1) < 0.03:
        fireworks.append(Firework())

    # update & draw fireworks (iterate over a shallow copy so we can remove safely)
    for fw in fireworks[:]:
        fw.update()
        fw.show()
        if fw.is_dead():
            fireworks.remove(fw)

# optional: click to launch at mouseX
def mousePressed():
    fireworks.append(Firework(mouseX))
