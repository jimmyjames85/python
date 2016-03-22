from build.utils import *


#
# Blender's red +X axis =>> Obj +X axis
# Blender's green +Y axis =>> Obj -Z axis
# Blender's blue +Z axis =>> Obj +Y axis
#


__createCylinder_new_name = 0
def createCylinder(radius, height, vertCount, objName="", offsetX=0, offsetY=0, offsetZ=0, material=None):
    global __createCylinder_new_name

    objName = "%s.%04d" % (objName, __createCylinder_new_name)
    __createCylinder_new_name +=1

    ret = ""

    return ret