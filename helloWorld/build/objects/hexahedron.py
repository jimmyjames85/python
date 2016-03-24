from build.utils import *


#
# Blender's red +X axis =>> Obj +X axis
# Blender's green +Y axis =>> Obj -Z axis
# Blender's blue +Z axis =>> Obj +Y axis
#


###### helper functions ######
def __findSignChanges(faceVerts):
    signChange = [False, False, False]

    listLen = len(faceVerts)
    if (listLen) == 0:
        return []  # Error
    elif (listLen) == 1:
        return signChange  # no sign change along all axis if there is just one vertex

    for i in range(1, len(faceVerts)):
        signChange = [signChange[0] or (signOf(faceVerts[i][0]) != signOf(faceVerts[i - 1][0])), \
                      signChange[1] or (signOf(faceVerts[i][1]) != signOf(faceVerts[i - 1][1])), \
                      signChange[2] or (signOf(faceVerts[i][2]) != signOf(faceVerts[i - 1][2]))]

    return signChange


def __findPath(faceVerts, commonSignAxis):
    path = []
    if len(faceVerts) == 0:
        return path

    compareAxis = list(range(0, 3))
    compareAxis.remove(commonSignAxis)

    verts = []
    for i in range(len(faceVerts)):
        newVert = [faceVerts[i], i]
        verts.append(newVert)

    path.append(verts.pop(0))

    while len(verts) > 0:
        prevVertTup = path[len(path) - 1]
        nextVertTup = verts.pop(0)
        prevVert = prevVertTup[0]
        nextVert = nextVertTup[0]

        firstAxisChange = (signOf(prevVert[compareAxis[0]]) != signOf(nextVert[compareAxis[0]]))
        secondAxisChange = (signOf(prevVert[compareAxis[1]]) != signOf(nextVert[compareAxis[1]]))
        if (firstAxisChange != secondAxisChange):
            path.append(nextVertTup)
        else:
            verts.append(nextVertTup)

    ret = []
    for vert in path:
        ret.append(vert[1])

    return ret




__createHexahedron_new_name = 0


def createHexahedron(width, height, depth, objName="hexaheron", offsetX=0, offsetY=0, offsetZ=0, material=None):

    global __createHexahedron_new_name

    objName = "%s.%04d" % (objName, __createHexahedron_new_name)
    __createHexahedron_new_name += 1

    ret = "### Hexahedron Generated %s \n\n" % localtimeString()

    #
    # Blender's red +X axis =>> Obj +X axis
    # Blender's green +Y axis =>> Obj -Z axis
    # Blender's blue +Z axis =>> Obj +Y axis
    #

    vertices = []
    for x in [-width / 2, width / 2]:
        for y in [-height / 2, height / 2]:
            for z in [-depth / 2, depth / 2]:
                vertices.append([x, -z, y])

    ret +='# %s\n' % (objName)
    ret += 'g %s\n' % (objName)

    if(material!=None):
        ret +='usemtl %s\n' % material

    #TODO remove scale...The Blender options allow us to use any metric we like e.g. inches, mm etc
    # we need to scale everything down so our objects will fit in the blender viewport
    # both the offsets and the the vertices below
    scaleAmount = 1
    offsetX /= scaleAmount
    tmpOldY = offsetY
    offsetY = offsetZ / scaleAmount
    offsetZ = tmpOldY / scaleAmount

    # we are using a reversed list of vertices so we can use negative
    # vertex references
    for v in reversed(vertices):
        v[0] /= scaleAmount
        v[1] /= scaleAmount
        v[2] /= scaleAmount
        ret +='v %f %f %f\n' % (v[0] + offsetX, v[1] + offsetY, v[2] + offsetZ)

    # curAxis represents x=0, y=1 or z=2
    for curAxis in range(0, 3):

        # Because we center/build our object around (0, 0, 0), each
        # face shares the same sign along exactly one axis
        # (NOTE: offsets are only recognized in the file, not in our vertex list)
        #
        # s stands for sign...
        # each sign is either neg or pos
        # 2 options for sign , 3 options for the axis
        # This gives us 6 sides
        #
        # we collect faces that have the same
        # sign along the x's, the y's and then the z's (though in no particular order)
        #

        # faceVerts represents the list of vertices that make up a face

        for s in [-1, 1]:
            faceVertNames = []  # e.g. index or name of vertex
            faceVerts = []  # actual vertices

            # collect verts to put into faceVert
            for v in range(0, len(vertices)):
                if (s < 0 and vertices[v][curAxis] < 0):
                    faceVerts.append(vertices[v])
                    faceVertNames.append(v)
                elif (s > 0 and vertices[v][curAxis] > 0):
                    faceVerts.append(vertices[v])
                    faceVertNames.append(v)

            # now we need to arange the verts in order
            # because we center our cube object at (0, 0, 0)
            # any step along an edge from one vertex to another
            # means we will have a sign change in exactly one axis
            #
            # so for each face (group of 4 vertices)
            # we find the axis that has a common sign (there can only be one)
            # then we find a path were each subsequent vertex has a change in sign
            # in only one of the remaining two axis


            commonSignAxis = __findSignChanges(faceVerts).index(False)

            path = __findPath(faceVerts, commonSignAxis)

            ret +='f '

            # we are using a reversed list of vertices so we can use negative
            # vertex references hence we must multiply by negative one
            # (we add on because the vertices are not zero-indexed)
            for i in path:
                ret +="%d " % (-1 * (faceVertNames[i] + 1))

            ret +="\n"
    return ret