# This is basic Bar chart for Blender Python 3.5+ script.
# Tested UPBGE 0.3 version.
# make testList.csv to test directory to access.
# Pylväsdiagrammi Blender Python 3.5+ skripti.

from pathlib import Path
import csv
import bpy

bar_spacing = 1.5
bar_width = 1

# absolute filename in the user's home directory in Linux users (python 3.5+).
home = str(Path.home())
path = "/test/testList.csv"

home_path = (home + path)

with open(home_path) as f:
    readout = list(csv.reader(f))
    
for a in readout:
    placement = readout.index(a)
    bpy.ops.mesh.primitive_plane_add(size=1)
    new_bar = bpy.context.object
        
    for vert in new_bar.data.vertices:
        vert.co[1] += 0.5
        vert.co[0] += placement*bar_spacing + 0.5
        
    new_bar.scale = (bar_width, float(a[1]), 1)
    
    bpy.ops.object.text_add()
    bpy.context.object.data.align_x = 'RIGHT'
    bpy.context.object.data.align_y = 'CENTER'
    bpy.ops.transform.rotate(value=-1.5708)
    bpy.ops.transform.translate(value=(placement*bar_spacing + 0.5, -0.5, 0))
    bpy.context.object.data.body = a[0]
