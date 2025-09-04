# List to hold all snowflake objects
Snowflakes = []

# Define the Snowflake class
class Snowflake:
    def __init__(self, tempimg):
        # Assign random properties to each snowflake
        self.img = tempimg                          # Snowflake image (one of the 3 loaded images)
        self.x = random(0, width)                   # Random x-position on the screen
        self.y = random(-100, float(height))        # Start above the screen at random height
        self.z = random(0, 20)                      # Depth value (used to control size, speed, opacity)

        # Map z to snowflake size: closer flakes (z small) look bigger, farther ones smaller
        self.Size = int(map(self.z, 0, 20, 50, 2))

        # Map z to fall speed: closer flakes fall faster, farther flakes slower
        self.speed = map(self.z, 0, 20, 3, 0.5)

        # Map size to opacity: bigger flakes = lighter opacity, smaller flakes = more visible
        self.opacity = map(self.Size, 50, 2, 10, 120)

    def show(self):
        """Display the snowflake on screen"""
        if self.Size > 30:
            # For bigger snowflakes, draw them using the snowflake image (semi-transparent)
            tint(255, 180)  # RGBA: white with alpha=180
            image(self.img, self.x, self.y, self.Size, self.Size)
        else:
            # For smaller snowflakes, draw as white ellipses (circles)
            noStroke()
            fill(255, self.opacity)  # white with given opacity
            ellipse(self.x, self.y, self.Size, self.Size)

    def drop_down(self):
        """Make the snowflake fall down and reset when it reaches bottom"""
        self.y += self.speed  # Move snowflake down by its speed

        # Reset flake to top once it moves out of screen
        if self.y > height:
            self.y = random(-100, -10)              # Respawn above the screen
            self.x = random(0, width)               # Random new x-position
            self.z = random(0, 20)                  # Assign new depth
            self.Size = int(map(self.z, 0, 20, 50, 2))  # Recalculate size
            self.speed = map(self.z, 0, 20, 3, 0.5)     # Recalculate speed
            self.opacity = map(self.Size, 50, 2, 10, 120)  # Recalculate opacity


def setup():
    """Setup runs once at start"""
    fullScreen()  # Fullscreen canvas

    # Load snowflake images (must be present in project folder)
    global img1, img2, img3
    img1 = loadImage("snow1.png")
    img2 = loadImage("snow2.png")
    img3 = loadImage("snow3.png")
    
    # Create 400 snowflakes with random images
    for i in range(400):
        n = int(random(0, 3))  # Randomly pick which snowflake image to use
        if n == 0:
            Snowflakes.append(Snowflake(img1))
        elif n == 1:
            Snowflakes.append(Snowflake(img2))
        else:
            Snowflakes.append(Snowflake(img3))

    frameRate(60)  # Run at 60 frames per second


def draw():
    """Draw runs continuously at given framerate"""
    background(0, 0, 80)  # Dark blue background (night sky)
    
    # Show and update all snowflakes
    for flake in Snowflakes:
        flake.show()       # Draw snowflake
        flake.drop_down()  # Update its position
