from build.materials import *
from build.objects.hexahedron import *
from build.objects.cylinder import *

myBlenderDir = "/home/jim/blenderFiles/"
materialFileName = "materialLib.mtl"
objectFileName = "myTest.obj"

materialLib = [createRedMaterial(),
               createGreenMaterial(),
               createBlueMaterial(),
               createWoodMaterial(),
               createPlywoodMaterial()]

with open("%s%s" % (myBlenderDir, materialFileName), "w") as mtlFile:
    matlibText = createMaterialLibraryFileText(materialLib)
    output("%s" % matlibText, mtlFile)
    mtlFile.close()

with open("%s%s" % (myBlenderDir, objectFileName), "w") as objFile:
    output("mtllib %s\n" % materialFileName, objFile)

    objs = []
    
    # # balcony
    # objs.append(createHexahedron(110, 81, 0.25, "Balcony", 0, 0, -0.25, "plywood"))    
    # # door jam
    # objs.append(createHexahedron(3, 33, 95, "Door", 56.5, 0, 47.5, "plywood"))     

    depth = 24 #26.75
    width = 5*12 # 42.5 
    height = 36 #27.5 

    topThickness = 0.75
    wheelHeight = 5
    
    frontX = (depth-3.5)/2
    backX = -1*frontX
    topBeamZ = (height - topThickness - 0.75)
    btmBeamZ = (wheelHeight + 0.75)
    
    objs.append(createHexahedron(3.5, width, 1.5, "A: [%s\" 2x4]" % width, frontX, 0, btmBeamZ, "green"))
    objs.append(createHexahedron(3.5, width, 1.5, "B: [%s\" 2x4]" % width, frontX, 0, topBeamZ, "green"))
    objs.append(createHexahedron(3.5, width, 1.5, "C: [%s\" 2x4]" % width, backX, 0, topBeamZ, "green"))
    objs.append(createHexahedron(3.5, width, 1.5, "D: [%s\" 2x4]" % width, backX, 0, btmBeamZ, "green"))

    # vertical support posts
    rightY =(width-1.5)/2
    leftY = -1 * rightY
    supportHeight = (height - wheelHeight - 3 -topThickness)
    supportZ = wheelHeight + 1.5 + (supportHeight/2)
    objs.append(createHexahedron(3.5, 1.5, supportHeight, "E: [%s\" 2x4]" % supportHeight, frontX, leftY, supportZ, "blue"))
    objs.append(createHexahedron(3.5, 1.5, supportHeight, "F: [%s\" 2x4]" % supportHeight, frontX, 0, supportZ, "blue"))
    objs.append(createHexahedron(3.5, 1.5, supportHeight, "G: [%s\" 2x4]" % supportHeight, frontX, rightY, supportZ, "blue"))
    objs.append(createHexahedron(3.5, 1.5, supportHeight, "H: [%s\" 2x4]" % supportHeight, backX, rightY, supportZ, "blue"))
    objs.append(createHexahedron(3.5, 1.5, supportHeight, "I: [%s\" 2x4]" % supportHeight, backX, 0, supportZ, "blue"))
    objs.append(createHexahedron(3.5, 1.5, supportHeight, "J: [%s\" 2x4]" % supportHeight, backX, leftY, supportZ, "blue"))


    # rails that connect the front and back
    railLength = (depth - 7)

    objs.append(createHexahedron(railLength, 1.5, 3.5, "K: [%s\" 2x4]" % railLength, 0, leftY, wheelHeight+1.75, "red"))
    objs.append(createHexahedron(railLength, 1.5, 3.5, "L: [%s\" 2x4]" % railLength, 0, 0, wheelHeight+1.75, "red"))
    objs.append(createHexahedron(railLength, 1.5, 3.5, "M: [%s\" 2x4]" % railLength, 0, rightY, wheelHeight+1.75, "red"))

    topRailZ = wheelHeight+3+supportHeight-1.75
    objs.append(createHexahedron(railLength, 1.5, 3.5, "N: [%s\" 2x4]" % railLength, 0, rightY, topRailZ, "red"))
    objs.append(createHexahedron(railLength, 1.5, 3.5, "O: [%s\" 2x4]" % railLength, 0, 0, topRailZ, "red"))
    objs.append(createHexahedron(railLength, 1.5, 3.5, "P: [%s\" 2x4]" % railLength, 0, leftY, topRailZ, "red"))


#    (+ 36 (/ -1.5 2))
    # for i in range(1,4):
    #     objs.append(createHexahedron(2*12, 6*12, 0.25, "1/4\" 2x6' Benchtop", 0, 0, 36.125 - (i/4.0), "plywood"))
    # objs.append(createHexahedron(2*12, 6*12, 0.75, "3/4\" 2x6' Middle Shelf", 0, 0, 18, "wood"))
    # objs.append(createHexahedron(2*12, 6*12, 0.75, "3/4\" 2x6' Bottom Shelf", 0, 0, 4.375, "wood"))

    # objs.append(createHexahedron(1.5, 3.5, 36, "3ft 2x4", -12+(1.5/2), -24+(3.5/2), 1.5*12, "red"))
    # objs.append(createHexahedron(1.5, 3.5, 36, "3ft 2x4", -12+(1.5/2)+1.5, -24+(3.5/2), 1.5*12, "red"))
    
    # objs.append(createHexahedron(1.5, 6*12, 5.5, "6ft 2x6", -12+(1.5/2)+1.5, 0, 1.5*12, "red"))

    # objs.append(createCylinder(5/16, 4, 32,"5/8 \"dowel", 0,0,0,"green"))
    
    # for i in range(0, 6):
    #     hexStr = createHexahedron(5.5, 144, 1.5, "12ft 2x6", 0 + i * 5.6, 0, 36, "wood")
    #     output("%s" % hexStr, objFile)

    # for i in range(0, 4):
    #     hexStr = createHexahedron(1.5, 3.5, 36, "8ft 2x4", i * 4, 0, 0, "red")
    #     output("%s" % hexStr, objFile)

    # cylStr = createCylinder(6, 4, 32,"cylinder", 0,0,0,"wood")
    # output("%s" % cylStr, objFile)
    # createHexahedron(1.5, 3.5, 96, objFile, "8ft 2x4", 0, 0, 0, "wood")
    # createHexahedron(1.5, 3.5, 96, objFile, "8ft 2x4", 0, 0, -12)
    # createHexahedron(48, 96, 0.75, objFile, "4x8 ply")
    
    for obj in objs:
        output("%s" % obj, objFile)
    objFile.close()

