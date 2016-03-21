import sys
sys.path.append('/home/jim/blender/blender-2.76b-linux-glibc211-x86_64/2.76/python/lib/python3.4')

#from Blender import *
from Tkinter import *
import tkMessageBox
'''
multi line comment???


'''
i=0

#def helloWorld():
#        global i
#        global b
#        msg="hello world %d" % (i)
#        print msg
#        b.configure(text=msg)
#        i+=1

#top = Tk()
#b= Button(text="click me now!!!!", command=helloWorld)
#b.pack()


#top.mainloop()

#
#C = Canvas(top, bg="blue", height=250, width=300)
#coord = 10, 50, 240 , 210
#arc = C.create_arc(coord, start=0, extent=150, fill="red")
#C.pack()




d=0.75000
h=96
w=48

objName= '4\'x8\' 3/4" plywood'



vertices = []

for z in [-h/2, h/2]:
    for x in [-w/2, w/2]:
        for y in [-d/2, d/2]:
                vertices.append([x,y,z])


def output(str,fmt)
print '%str'
    return

def arrangeFaceVerts(faceVerts):

    ret = []
    return ret




with open("/home/jim/blenderFiles/myTest.obj", "w") as f:
    print '# %s' % (objName)
    print 'o %s' % (objName)
    f.write('#----File---- %s\n' % (objName))
    f.write('o %s\n' % (objName))
    for v in vertices:
        print 'v %f %f %f' % (v[0]/10.0,v[1]/10.0,v[2]/10.0)
        f.write('v %f %f %f\n' % (v[0]/10.0,v[1]/10.0,v[2]/10.0))


    #i represents x, y or z
    for i in range(0,3):
        #faceVerts represents the list of vertices that make up the face
        faceVerts = []

        #s stands for sign we collect faces that are have the same
        # sign along the x's, the y's or the z's each
        # sign is either neg or pos
        # 2 options for sign ,3 options for axis = 6 sides
        for s in [-1,1]:

            #collect verts to put into faceVert
            for v in range(0,len(vertices)):
                if(s<0 and vertices[v][i] < 0):
                    faceVerts.append(v)
                elif(s>0 and vertices[v][i] > 0):
                    faceVerts.append(v)

            #now we need to arange the verts in order

            for vi in range(0,len(faceVerts)):

                if(faceVerts[vi])


            print 'f ',
            f.write('f ')
            while len(faceVerts)>0:
                face= faceVerts.pop() + 1
                print face,
                f.write('%d ' % face)
            print
            f.write('\n')
    f.close()











