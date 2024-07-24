"""
    Draws a Boolean lattice of size 2^n, given an integer n.
    Can also draw Hasse diagrams of some Boolean functions. 
"""
import itertools
import math
from PIL import Image, ImageDraw

########### GLOBAL CONSTANTS
N         = 7
R         = 4     #circle diameter to draw points
X_STEP    = 16+R  #number of pixels between each point, horizontally
Y_STEP    = 64    #number of pixels between each point, vertically
MAXWIDTH  = X_STEP * (math.comb(N, int(N/2))+1) #largest part of the lattice: at the middle, with C(n,n/2) points of weight n/2
MAXHEIGHT = Y_STEP * (N+1)
OUTPUT    = Image.new('RGB', (MAXWIDTH+R+1, MAXHEIGHT+R+1), (0, 0, 0))
DRAW      = ImageDraw.Draw(OUTPUT)


########### GENERAL LATTICE FUNCTIONS
def bitDistance(b1, b2):
    return abs(int(b1) - int(b2))
def bitFlip(b):
    if b=="1":
        return "0"
    return "1"
def distance(s1, s2):
    return sum([bitDistance(s1[i], s2[i]) for i in range(min(len(s1), len(s2)))])
def weight(s):
    return distance(s, '0'*len(s))
def linked(s1, s2):
    #returns True if two points in the lattice are linked
    return distance(s1, s2) == 1
def lineSize(n, i):
    #returns the number of points at line i in a Boolean lattice of size 2^n
    if i<0 or i>n:
        return 0
    return math.comb(n, i)
def pointCodes(n):
    #returns a list of all binary points of size n
    return ["".join(point) for point in itertools.product(['0', '1'], repeat=n)]
def sortedPointCodes(n):
    return sorted(pointCodes(n), key=weight)

########### BOOLEAN FUNCTIONS
def conjunction_n(l):
    return weight(l)==len(l)
def disjunction_n(l):
    return weight(l)>0
def sum_n(l):
    return weight(l)%2==0

########### LATTICE DRAWING

points = sortedPointCodes(N)
coordinates = {}
#initialize point coordinates
for point in points:
    coordinates[point] = [0,0]
#add Y coordinates to the points
for point in points:
    coordinates[point][1] = Y_STEP * weight(point) + int(Y_STEP/2)
#prepare X coordinates
x_coordinates = []
for i in [lineSize(N,j) for j in range(0,N+1)]:
    for k in range(1,i+1):
        x_coordinates.append(k)
#add X coordinates to the points
counter = 0
for point in points:
    center_step = MAXWIDTH/(lineSize(N, weight(point))+1)
    coordinates[point][0] = center_step * int(x_coordinates[counter])
    counter+=1
#add lines
for point1 in points:
    for point2 in points: #not efficient, but it's fine.
        if linked(point1, point2):
            DRAW.line([*coordinates[point1], *coordinates[point2]], fill =(100, 100, 100), width = 0)
#add points
for point in points:
#   OUTPUT.putpixel(coordinates[point], (255,0,0))
    x = coordinates[point][0]
    y = coordinates[point][1]
    DRAW.ellipse((x-R, y-R, x+R, y+R), fill = (200,0,0), outline =(200,0,0))
#    if sum_n(point):
#        DRAW.ellipse((x-R, y-R, x+R, y+R), fill = (0,0,0), outline =(200,0,0))
#OUTPUT.show()
OUTPUT.save("N={}".format(N)+".png")


