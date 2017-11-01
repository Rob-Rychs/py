# CODESKULPTOR
# Demonstration of a magnifier on a map

import simplegui

# 1521x1818 pixel map of native American language
# source - Gutenberg project

image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/gutenberg.jpg")

# Image dimensions
MAP_WIDTH = 1521
MAP_HEIGHT = 1818

# Scaling factor
SCALE = 3

# Canvas size
CAN_WIDTH = 920
CAN_HEIGHT = 1818//SCALE

# Size of magnifier pane and initial center
MAG_SIZE = 100
mag_pos = [MAP_WIDTH//SCALE, MAP_HEIGHT//SCALE]


# Event handlers
# Move magnifier to clicked position
def click(pos):
    global mag_pos
    print pos
    mag_pos = list(pos)

# Draw map and magnified region
def draw(canvas):
    # Draw map
    canvas.draw_image(image, 
            [MAP_WIDTH // 2, MAP_HEIGHT // 2], [MAP_WIDTH, MAP_HEIGHT], 
            [250, CAN_HEIGHT // 2], [MAP_WIDTH//SCALE, MAP_HEIGHT//SCALE])

    # Draw magnifier    
    map_center = [SCALE * mag_pos[0], SCALE * mag_pos[1]]
    
    map_rectangle = [MAG_SIZE, MAG_SIZE]
    mag_center = [720,CAN_HEIGHT // 2]
    mag_rectangle = [MAG_SIZE*3, MAG_SIZE*3]
    canvas.draw_image(image, map_center, map_rectangle, mag_center, mag_rectangle)
    
# Create frame for scaled map
frame = simplegui.create_frame("Map magnifier",CAN_WIDTH,CAN_HEIGHT)

# register even handlers
frame.set_mouseclick_handler(click)    
frame.set_draw_handler(draw)

# Start frame
frame.start()
