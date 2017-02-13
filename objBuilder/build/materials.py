import time
from build.utils import localtimeString
from build.types.material import *

def createPlywoodMaterial():
    plywood = Material()
    plywood.ambientReflectivity = RGB(1, 0.3, 0.3)
    plywood.diffuseReflectivity = RGB(1, 0.611, 0.417)
    plywood.specularReflectivity = RGB(1, 0.649, 0.353)
    plywood.specularExp = 1000
    plywood.illumNo = 2
    plywood.name="plywood"
    return plywood


def createWoodMaterial():
    wood = Material()
    wood.ambientReflectivity = RGB(1, 0.2, 0.2)
    wood.diffuseReflectivity = RGB(1, 0.511, 0.317)
    wood.specularReflectivity = RGB(1, 0.549, 0.253)
    wood.specularExp = 1000
    wood.illumNo = 2
    wood.name="wood"
    return wood

def createRedMaterial():
    red = Material()
    red.ambientReflectivity = RGB(1, 0.0, 0.0)
    red.diffuseReflectivity = RGB(1, 0.0, 0.0)
    red.specularReflectivity = RGB(1, 0.0, 0.0)
    red.specularExp = 500
    red.illumNo = 1
    red.name="red"
    return red

def createGreenMaterial():
    green = Material()
    green.ambientReflectivity = RGB(0.0, 1, 0.0)
    green.diffuseReflectivity = RGB(0.0, 1, 0.0)
    green.specularReflectivity = RGB(0.0, 1, 0.0)
    green.specularExp = 500
    green.illumNo = 1
    green.name="green"
    return green

def createBlueMaterial():
    blue = Material()
    blue.ambientReflectivity = RGB(0.0, 0.0, 1)
    blue.diffuseReflectivity = RGB(0.0, 0.0, 1)
    blue.specularReflectivity = RGB(0.0, 0.0, 1)
    blue.specularExp = 500
    blue.illumNo = 1
    blue.name="blue"
    return blue


def createMaterialLibraryFileText(materialList):
    ret = "### Material Library Generated %s\n\n" % localtimeString()
    for mat in materialList:
        ret += "newmtl %s\n" % mat.name
        ret += "illum %d\n" % mat.illumNo
        ret += "Ka %s\n" % mat.ambientReflectivity #Blenders mirror options must be turned on
        ret += "Kd %s\n" % mat.diffuseReflectivity
        ret += "Ks %s\n" % mat.specularReflectivity
        ret += "Ns %s\n\n" % mat.specularExp
        #ret += "map_Kd wood.png\n" TODO
    ret += "### End Material Library \n\n"
    return ret



