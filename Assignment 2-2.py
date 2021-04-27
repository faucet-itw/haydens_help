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

class projectile:
    def __init__(self, theta, given_velocity):
        self.given_velocity = given_velocity
        self.theta = theta
    
    def get_yintial_velocity(self):
        return (self.given_velocity*math.sin*self.theta)
s = projectile(30, 60)
print("The y component of the velocity is: m/s") % (s.get_yintial_velocity())



