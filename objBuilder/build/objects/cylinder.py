from build.utils import *
from math import sin
from math import cos
from math import radians
from build.types.vertex import Vertex

#
# Blender's red +X axis =>> Obj +X axis
# Blender's green +Y axis =>> Obj -Z axis
# Blender's blue +Z axis =>> Obj +Y axis
#


__createCylinder_new_name = 0


def createCylinder(radius, height, vertCount, objName="cylinder", offsetX=0, offsetY=0, offsetZ=0, material=None):
    global __createCylinder_new_name

    objName = "%s.%04d" % (objName, __createCylinder_new_name)
    __createCylinder_new_name += 1

    verts = []

    ret = "### Cylinder Generate %s \n\n" % localtimeString()

    ret +='# %s\n' % (objName)
    ret += 'g %s\n' % (objName)
    if(material!=None):
        ret +='usemtl %s\n' % material


    # TODO
    # Blender's red +X axis =>> Obj +X axis
    # Blender's green +Y axis =>> Obj -Z axis
    # Blender's blue +Z axis =>> Obj +Y axis
    #



    height /= 2  # divided in half for top and bottom ....see 'h' below for  sign

    # create the vertices
    for h in [-1, 1]:
        for step in range(0, vertCount):
            deg = step * 360 / vertCount
            x = radius * cos(radians(deg))
            y = radius * sin(radians(deg))
            z = height * h
            verts.append(Vertex(x, y, z))

    for v in verts:
        ret += 'v %f %f %f\n' % (v.x + offsetX, v.y + offsetY, v.z + offsetZ)

    # create the bottom circle
    ret += 'f '
    for c in range(0, vertCount):
        ret += '%d ' % -(c + 1)
    ret += '\n'

    # create the top circle
    ret += 'f '
    for c in range(vertCount, 2 * vertCount):
        ret += '%d ' % -(c + 1)
    ret += '\n'



    #connect top and bottom
    for c in range(1, vertCount):
        ret +="f %d %d %d %d\n" % (-c, -(c+vertCount),  -(c+vertCount+1), -(c+1))

    #TODO add last side beam...
    ret +="f %d %d %d %d\n" % (-32, -64, -32, -1)




    return ret


print(createCylinder(5, 4, 4))
