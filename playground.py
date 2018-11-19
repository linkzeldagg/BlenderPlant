import bpy
import os
import sys
import math

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path: 
    sys.path.append(dir)

import SDFtoMeshSettings
from utils_3d import V3
import dualContour3D as dc

import importlib

importlib.reload(dc)
importlib.reload(SDFtoMeshSettings)

### Basic Mesh defination ###

if False:
    # Define vertices and faces
    verts = [(0,0,0),(0,5,0),(5,5,0),(5,0,0)]
    faces = [(0,1,2,3)]

    # Define mesh and object variables
    mymesh = bpy.data.meshes.new("Plane")
    myobject = bpy.data.objects.new("Plane", mymesh)  

    # Set location and scene of object
    myobject.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(myobject)

    # Create mesh
    mymesh.from_pydata(verts,[],faces)
    mymesh.update(calc_edges=True)

### SDF Test ###

def circle_function(x, y, z):
    return 5 - math.sqrt(x*x + y*y + z*z)

if True:
    # Collect geometry from SDF
    verts, faces = dc.dual_contour_3d(circle_function, None, -10, 10, -10, 10, -10, 10)
    
    # Define mesh and object variables
    mymesh = bpy.data.meshes.new("SDF")
    myobject = bpy.data.objects.new("SDF", mymesh)
    
    print(verts)
    print(faces)

    # Set location and scene of object
    myobject.location = bpy.context.scene.cursor_location
    bpy.context.scene.objects.link(myobject)

    # Create mesh
    mymesh.from_pydata(verts,[],faces)
    mymesh.update(calc_edges=True)
