import os
import bpy
import mathutils
from math import radians

def help(obj):
    print(dir(obj))
    return


def importObjFile(objfileloc):
    
    #clear scene
    for obj in bpy.data.objects:
        obj.hide = False
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete(use_global=True)

        # Design note: as mentioned above, prior to Blender 2.56, when switching "Units" 
        # type, i.e. "Metric" and "Imperial" units, the underlying 'scale' value remains 
        # unchanged. In other words, each of the measurement sub-systems use the same
        # base unit, which is synonymous with a measurement of one metre. This means 
        # Imperial unit calculations must be done relative to metres being the base unit,
        # rather than feet as is the case Blender 2.56 and above; inches require 
        # "Scale: 0.0254", feet "Scale: 0.3048", yards "Scale: 0.9144" and so on.
        
    bpy.data.scenes["Scene"].unit_settings.system = 'IMPERIAL'
    bpy.data.scenes["Scene"].unit_settings.scale_length=0.0254
    bpy.data.scenes["Scene"].unit_settings.use_separate = True
        
        
    scene = bpy.context.scene
    lamp_top_data = bpy.data.lamps.new(name = "overhead_lamp", type='POINT')
    lamp_top_data.energy=10.0
    
    lamp_btm_data = bpy.data.lamps.new(name = "overhead_lamp", type='POINT')
    lamp_btm_data.energy=3.0
        
        
    for x in range(-8,9, 4):
        for y in range(-8, 9, 4):
            lamp_object = bpy.data.objects.new(name="lamp",object_data=lamp_top_data)
            lamp_object.location = [x*12,y*12,8*12]
            scene.objects.link(lamp_object)
            lamp_object.hide = True
                
            lamp_object_btm = bpy.data.objects.new(name="lamp",object_data=lamp_btm_data)
            lamp_object_btm.location = [x*12,y*12,-1*12]
            scene.objects.link(lamp_object_btm)
            lamp_object_btm.hide = True



    cameraObj = bpy.ops.object.camera_add()
    camera = bpy.data.objects["Camera"]
    camera.location=[15.5*12, -7.5*12, 8.5*12]

    print("\n\n\n")
    print(dir(camera.rotation_mode))
    camera.rotation_mode='XYZ'
    camera.rotation_euler[0]=radians(66)
    camera.rotation_euler[1]=radians(0)
    camera.rotation_euler[2]=radians(63)
    camera.scale=[1.5,1.5,1.5]
        
    cameraData = camera.data
    cameraData.clip_end = 32*12


    #for a in bpy.context.screen.areas:
    #    if(a.type == 'VIEW_3D'):
    #        override = bpy.context.copy()
    #        override['area'] = a
    #        bpy.ops.view3d.viewnumpad(override, type='CAMERA')
    #        bpy.ops.object.select_all(action='SELECT')
    #        bpy.ops.object.origin_set(type='ORIGIN_CENTER_OF_MASS')
    #        break
    #    print(a.type)

    bpy.ops.import_scene.obj(filepath = objfileloc)

    # currently importObj has the origin at 0,0,0 for all object so we
    # recenter origins to the center of each object
    for obj in bpy.data.objects:
        bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY')

