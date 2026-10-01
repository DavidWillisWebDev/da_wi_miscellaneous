"""
In this challenge, you have to convert a weight weighed on a planet of the Solar System to the corresponding weight on another planet.

To convert the weight, you have to divide it by the gravitational force of the planet on which is weighed and multiply the result (the mass) for the gravitational force of the other planet. See the table below for a list of gravitational forces:

weight on planet_a / gravitational force of planet_a * gravitational force of planet_b

Planet	m/s²

Given a weight weighed on planet_a, return the converted value for planet_b rounded to the nearest hundredth.

Examples
space_weights("Earth", 1, "Mars") ➞ 0.38

space_weights("Earth", 1, "Jupiter") ➞ 2.53

space_weights("Earth", 1, "Neptune") ➞ 1.14
"""

mercury =	3.7
venus =	8.87
earth =	9.81
mars =	3.711
jupiter =	24.79
saturn =	10.44
uranus =	8.69
neptune =	11.15

def space_weights(planet_a, weight, planet_b):
  # weight on planet_a / gravitational force of planet_a * gravitational force of planet_b
  weight / planet_a * planet_b
  if planet_a == earth:
    
  if planet_a == mercury:
    
  if planet_a == venus:
    
  if planet_a == mars:
    
  if planet_a == jupiter:
    
  if planet_a == saturn:
    
  if planet_a == uranus:
    
  if planet_a == neptune:
    


print(earth, 1, venus)