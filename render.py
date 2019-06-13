import bpy
import time
from bpy.app.handlers import persistent

def render_and_get_time():
    bpy.ops.render.render()
    return last_render_time


# Measure Render Time
#################################################

last_start_time = None
last_render_time = None

@persistent
def render_begin(dummy):
    global last_start_time
    last_start_time = time.perf_counter()

@persistent
def render_end(dummy):
    global last_render_time
    assert last_start_time is not None
    last_render_time = time.perf_counter() - last_start_time


# Register
#################################################

def register():
    bpy.app.handlers.render_init.append(render_begin)
    bpy.app.handlers.render_complete.append(render_end)

def unregister():
    bpy.app.handlers.render_init.remove(render_begin)
    bpy.app.handlers.render_complete.append(render_end)
