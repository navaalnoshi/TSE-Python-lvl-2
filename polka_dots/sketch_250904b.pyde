dotslist = []                     # Empty list to store all dot objects
maxdotsize = 70                   # Maximum size of the dots (used later with mouse control)

class dots:                       # Class definition for each dot
    def __init__(self):           # Constructor: runs when a new dot is created
        self.x = random(width)    # Random x-coordinate within window
        self.y = random(height)   # Random y-coordinate within window
        self.xspeed = random(1,3) # Random horizontal speed between 1–3 pixels per frame
        self.yspeed = random(1,3) # Random vertical speed between 1–3 pixels per frame

        # Randomize horizontal direction (left or right)
        if int(random(0,2)) == 1: 
            self.xspeed *= 1      # Keep direction as positive (move right)
        else:
            self.xspeed *= -1     # Flip to negative (move left)

        # Randomize vertical direction (up or down)
        if int(random(0,2)) == 1: 
            self.yspeed *= -1     # Flip to negative (move up)
        else:
            self.yspeed *= 1      # Keep positive (move down)

        # Assign random RGB color
        self.rcol = random(255)   # Red value (0–255)
        self.gcol = random(255)   # Green value (0–255)
        self.bcol = random(255)   # Blue value (0–255)

    def show(self, sizeValue):    # Draw the dot on screen
        fill(self.rcol, self.gcol, self.bcol)   # Set fill color to the dot’s random color
        circle(self.x, self.y, sizeValue)       # Draw circle at (x,y) with diameter = sizeValue

    def move(self, sizeValue):    # Update position + check for bouncing
        self.x += self.xspeed     # Move horizontally by xspeed
        self.y += self.yspeed     # Move vertically by yspeed

        # --- Check left/right boundaries ---
        if (self.x > width - sizeValue/2):    # If dot goes past right edge
            self.x = width - sizeValue/2      # Place it exactly at edge
            self.xspeed *= -1                 # Reverse direction (bounce left)
        elif (self.x < 0 + sizeValue/2):      # If dot goes past left edge
            self.x = 0 + sizeValue/2          # Place at left edge
            self.xspeed *= -1                 # Reverse direction (bounce right)

        # --- Check top/bottom boundaries ---
        if (self.y > height - sizeValue/2):   # If dot goes past bottom
            self.y = height - sizeValue/2     # Place at bottom edge
            self.yspeed *= -1                 # Reverse direction (bounce up)
        elif (self.y < 0 + sizeValue/2):      # If dot goes past top
            self.y = 0 + sizeValue/2          # Place at top edge
            self.yspeed *= -1                 # Reverse direction (bounce down)

def setup():                       
    size(800,700)                  # Create window of 800x700 pixels
    for x in range(50):            # Repeat 50 times
        dotslist.append(dots())    # Create a new dot object and add it to list

def draw():
    global maxdotsize
    background(255,255,0)          # Clear screen with yellow background each frame
    dotsize = int(map(mouseX,0,width,10,maxdotsize))  
    # Map mouse position (left → right) to dot size (10 → 70 pixels)

    print(dotsize)                 # Print current size (debugging, optional)

    for one in dotslist:           # Loop over all 50 dots
        one.show(dotsize)          # Draw the dot with current size
        one.move(dotsize)          # Move the dot and check for bouncing
