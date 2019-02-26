from math import *

def get_distance(alpha, beta, r):
  alpha, beta = alpha*pi/180, beta*pi/180
  z = r  * cos(beta)
  x = r * sin(beta) * sin(alpha)
  y = r * sin(beta) * cos(alpha)

  return x, y, z

def calc_magnitude(x, y, z):
  return sqrt(x**2 + y**2 + z**2)

def get_vector_dist(b, n):
  factor = sum(map(lambda x: x[0]*x[1], zip(b, n))) / calc_magnitude(n[0], n[1], n[2])**2

  ret_vect = tuple(map(lambda x: x * factor, n))

  return ret_vect


#blazar_coords = get_distance(lat, lon, r)
#neut_coords = get_distance(lat, lon, 1)
