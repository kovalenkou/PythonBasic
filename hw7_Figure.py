# 1. Draw the square - horizontal
from ctb import place

size = 5
for x in range(0, size, 1):
    for z in range(0, size, 1):
	    place(x, 0, z)

# 1. Draw the square - vertical
from ctb import place

size = 7
for x in range(0, size, 1):
    for y in range(0, size, 1):
	    place(x, y, 0)

# 2. Draw the circle
import math
from ctb import place, colors

radius = 5
segments = 20
for position in range(2 * segments):
    radians = 2 * math.pi * position / segments
    x = radius * math.cos(radians)
    y = radius * math.sin(radians)
    place(x, y, 0, colors.GREEN)

# 2. Draw the three circle
import math
from ctb import place, colors
 
radius = 8
segments = 30

for position in range(segments):
    radians = 2 * math.pi * position / segments
    x = radius * math.cos(radians)
    y = radius * math.sin(radians)
    place(x, y, 0, colors.BLUE)
    place(x, 0, y, colors.GREEN)
    place(0, x, y, colors.RED)

# 3. Draw painted cube 
from ctb import place

size = 5
for x in range(0, size, 1):
    for y in range(0, size, 1):
        for z in range(0, size, 1):
            place(x, y, z)

# 3. Draw blank cube 
#Draw painted cub 
from ctb import place, colors

size = 7
for x in range(0,size,1):
  for y in range(0,size,1):
    for z in range(0,size,1):
      if ((x == 0) or (x == size - 1)) \
        and ((y != 0) or (y != size - 1)) \
        and ((z == 0) or (z == size -1)):
        place(x,y,z, colors.GREEN)
      elif ((y == 0) or (y == size - 1)) \
        and ((x != 0) or (x != size - 1)) \
        and ((z == 0) or (z == size -1)):
        place(x,y,z, colors.BLUE)
      elif ((z != 0) or (z != size - 1)) \
        and ((y == 0) or (y == size - 1)) \
        and ((x == 0) or (x == size -1)):
        place(x,y,z, colors.YELLOW)
#      else:
#        place(x,y,z, colors.RED)

 