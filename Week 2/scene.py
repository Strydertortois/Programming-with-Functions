# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_ground(canvas, scene_width, scene_height)

    draw_sky(canvas, scene_width, scene_height)
    
    #draw_grid(canvas, scene_width, scene_height, 50)
                    #...L....T....R....B
    draw_cloud(canvas, 100, 400, 300, 300)
    draw_cloud(canvas, 225, 450, 350, 350)
    draw_cloud(canvas, 175, 475, 300, 425)
    draw_cloud(canvas, 450, 450, 600, 375)
    draw_cloud(canvas, 550, 475, 675, 400)
    draw_cloud(canvas, 525, 450, 715, 350)
    draw_cloud(canvas, 300, 335, 475, 250)
    draw_cloud(canvas, 400, 290, 550, 210)
    draw_pine_tree(canvas, 550, 125, 250)
    draw_pine_tree(canvas, 400, 83, 300)
    draw_pine_tree(canvas, 275, 115, 100)
    draw_pine_tree(canvas, 110, 100, 220)
                       #R...T...L...B
    draw_river(canvas, 850, 200, -50, 65)
    draw_pine_tree(canvas, 170, 25, 200)
    draw_pine_tree(canvas, 650, 30, 250)
    draw_pine_tree(canvas, 475, 20, 175)
 

   


    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas,)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_pine_tree(canvas, center_x, bottom, height,):

        #draw trunk 
        trunk_width = height / 10
        trunk_height = height / 6
        left_trunk = center_x - trunk_width / 2
        bottom_trunk = bottom
        right_trunk = center_x + trunk_width / 2
        trunk_top = bottom + trunk_height
        draw_rectangle(canvas, left_trunk, bottom_trunk, right_trunk, 
        trunk_top, fill="tan4")
        #draw skirt
        skirt_width = height / 2
        skirt_bottom = trunk_top 
        skirt_left = center_x - skirt_width / 2
        skirt_right = center_x + skirt_width / 2
        peak_x = center_x
        peak_y = bottom + height
        draw_polygon(canvas, skirt_left, skirt_bottom, 
        peak_x, peak_y, skirt_right, skirt_bottom, fill="ForestGreen")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
    scene_width, scene_height - 350, width=0, fill="tan3")
    #draws ground
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 150,
    scene_width, scene_height, width=0, fill="skyBlue")
    #draws sky

def draw_cloud(canvas, left, top, right, bottom):
    draw_oval(canvas, left, top, right, bottom,
    width=0, fill="snow1")

def draw_river(canvas, right, top, left, bottom):
    draw_arc(canvas, right, top, left, bottom, start=180, extent=180,
        width=25, outline="royalBlue1", fill="")

def draw_grid(canvas, width, height, interval):
    #draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f"{x}")
    #draw horizontal lines
    label_x = 15
    for y  in range(interval, width, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f"{y}")

# Call the main function so that
# this program will start executing.
main()