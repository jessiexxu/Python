# Write a function that computes the volume of a sphere given its radius.
import math

def vol(rad):
    volume = 4/3 * math.pi * rad**3
    return volume

print vol(4)
