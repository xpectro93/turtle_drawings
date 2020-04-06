
import turtle 
import math 
  
  
# Create a new surface and window. 
surface_height = 800
surface_width =  600    


loadWindow = turtle.Screen()
loadWindow.setup(width=surface_width, height=surface_height)
turtle.bgcolor("black")
turtle.pencolor('white')
  
def draw_tree(order, theta, sz, posn, heading, depth=0): 
  
   # The relative ratio of the trunk to the whole tree   
   trunk_ratio = 0.29     
  
   # Length of the trunk   
   trunk = sz * trunk_ratio 
   delta_x = trunk * math.cos(heading) 
   delta_y = trunk * math.sin(heading) 
   (u, v) = posn 
   newpos = (u + delta_x, v + delta_y) 

   turtle.penup()
   turtle.goto(posn)
   turtle.pendown()
   turtle.goto(newpos) 
   
  
   if order > 0:   # Draw another layer of subtrees 
  
      # make the recursive calls to draw the two subtrees 
      newsz = sz*(1 - trunk_ratio) 
      draw_tree(order-1, theta, newsz, newpos, heading-theta,  depth+1) 
      draw_tree(order-1, theta, newsz, newpos, heading+theta,  depth+1) 
  
  
def main(): 
    theta = 0
  
    while True: 
  
        # Update the angle 
        theta += 0.01
  
        # This little part lets us draw the stuffs  
        # in the screen everything 
        draw_tree(9, theta, surface_height*0.9, (surface_width//2, surface_width-50), -math.pi/2) 
  
# Calling the main function 
main() 