import math
import numpy as np




class Projectile:
   def __init__(self, intial_velocity, acceleration, time):
       self.intial_velocity = intial_velocity
       self.acceleration = acceleration
       self.time = time
   
   def get_distance(self):
       return ((self.intial_velocity*self.time) + (0.5*self.acceleration*(self.time**2)))
 
p = Projectile(13, -9.8, 1.5)
print("Horizontal distance of Projectile: %s m" % (p.get_distance()))

'''
This is good, now use a for loop to iterate this calculation every .1 second, write it to an array, and then plot it.
'''


'''
Classes should all be at the top of the file, under importing the libraries.
'''
class projectile:   
    def __init__(self, theta, given_velocity):
        self.given_velocity = given_velocity
        self.theta = theta
    
    def get_yintial_velocity(self):
        return (self.given_velocity*math.sin*self.theta)
    
    
s = projectile(30, 60)
print("The y component of the velocity is: m/s") % (s.get_yintial_velocity())
# your print function has a close brackets after 'm/s' this is why its not printing
# however, when you fix this you'll probably find that your print function is only printing out an integer, and not the float

'''
here's some fixed code for you to look at and modify and re-write

s = projectile(30, 60)

V_y = "{:.3f}".format(s.get_yintial_velocity())  # https://www.kite.com/python/answers/how-to-print-a-float-with-two-decimal-places-in-python#:~:text=Use%20str.,string%20to%20print%20the%20float.


print("The y component of the velocity is: %d m/s" % float(s.get_yintial_velocity()))  #this will print out an integer
 
print("The y component of the velocity is:", V_y, "m/s") # this will print the float to 3 decimal places


'''


