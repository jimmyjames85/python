from build.materials import *
from build.objects.hexahedron import *
from build.objects.cylinder import *

myBlenderDir = "/home/jim/blenderFiles/"

# myBlenderDir = "C:\\Users\\jim\\blenderFiles\\"

materialFileName = "materialLib.mtl"
objectFileName = "myTest.obj"

materialLib = [createRedMaterial(), createWoodMaterial()]

with open("%s%s" % (myBlenderDir, materialFileName), "w") as mtlFile:
    matlibText = createMaterialLibraryFileText(materialLib)
    output("%s" % matlibText, mtlFile)
    mtlFile.close()

with open("%s%s" % (myBlenderDir, objectFileName), "w") as objFile:
    output("mtllib %s\n" % materialFileName, objFile)
    for i in range(0, 6):
        hexStr = createHexahedron(5.5, 144, 1.5, "12ft 2x6", 0 + i * 5.6, 0, 36, "wood")
        output("%s" % hexStr, objFile)

    for i in range(0, 4):
        hexStr = createHexahedron(1.5, 3.5, 36, "8ft 2x4", i * 4, 0, 0, "red")
        output("%s" % hexStr, objFile)



    cylStr = createCylinder(6, 4, 32,"cylinder", 0,0,0,"wood")
    output("%s" % cylStr, objFile)
    # createHexahedron(1.5, 3.5, 96, objFile, "8ft 2x4", 0, 0, 0, "wood")
    # createHexahedron(1.5, 3.5, 96, objFile, "8ft 2x4", 0, 0, -12)
    # createHexahedron(48, 96, 0.75, objFile, "4x8 ply")
    objFile.close()


# with open("%s%s" % (myBlenderDir, objectFileName), "r") as objFile:
#     lineNum = 0
#     for line in objFile:
#         printf("%d: %s" % (lineNum, line));
#         lineNum +=1
#
#     objFile.close()
