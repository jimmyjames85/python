import time
from build.utils import localtimeString
from build.types.material import *

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

def createMaterialLibraryFileText(materialList : list):
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



