import sys


###### helper functions ######
def printf(str):
    print( '%s' %(str), end="")
    return

def output(str, file=None):
    printf(str)
    if(file is not None):
        file.write(str)
    return


def signOf(num):
    if(num>0):
        return 1
    elif(num<0):
        return -1
    return 0
###### helper functions ######


'''
multi line comment???
'''

d=0.75000
h=96
w=48

objName= '4\'x8\' 3/4" plywood'
vertices = []

for z in [-h/2, h/2]:
    for x in [-w/2, w/2]:
        for y in [-d/2, d/2]:
                vertices.append([x,y,z])




'''def arrangeFaceVerts(faceVerts):
    ret = []
    return ret'''


#######   MAIN   #######
#######   MAIN   #######
#######   MAIN   #######

with open("C:\\Users\\jim\\blenderFiles\\myTest.obj", "w") as f:
    output('# %s\n' % (objName),f)
    output('o %s\n' % (objName),f)

    for v in vertices:
        output('v %f %f %f\n' % (v[0] / 10.0, v[1] / 10.0, v[2] / 10.0), f)

    #curAxis represents x, y or z
    for curAxis in range(0, 3):

        # Because we center/build our object around (0, 0, 0), each
        # face shares the same sign along exactly one axis
        #
        # s stands for sign...
        # each sign is either neg or pos
        # 2 options for sign , 3 options for the axis
        # This gives us 6 sides
        #
        # we collect faces that have the same
        # sign along the x's, the y's and then the z's (though in no particular order)
        #

        #faceVerts represents the list of vertices that make up a face
        faceVerts = []
        for s in [-1,1]:

            #collect verts to put into faceVert
            for v in range(0,len(vertices)):
                if(s<0 and vertices[v][curAxis] < 0):
                    faceVerts.append(v)
                elif(s>0 and vertices[v][curAxis] > 0):
                    faceVerts.append(v)

            #now we need to arange the verts in order

            #TODO create a findCommonAxis function for 4 verts
            #TODO Then travel along the path where each subsequent vertex
            #TODO has a change in sign in only one of the remaining two axis

            output('f ',f)
            while len(faceVerts)>0:
                face= faceVerts.pop() + 1
                output('%d ' % face, f)
            output("\n")
            f.write('\n')
    f.close()


#######   MAIN   #######
#######   MAIN   #######
#######   MAIN   #######








