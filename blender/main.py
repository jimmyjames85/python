import sys
import imp
sys.path.insert(0, '/home/jim/git/python/blender')
sys.path.insert(0, '/home/jim/git/python/objBuilder')
import importObj
import workbench
import build

imp.reload(build.materials)
imp.reload(build.objects.hexahedron)
imp.reload(workbench)
imp.reload(importObj)


# theFile = 'C:\\Users\jim\\blenderFiles\\myTest.obj'
theFile = '/home/jim/blenderFiles/myTest.obj'
importObj.importObjFile(theFile)

