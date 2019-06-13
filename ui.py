import bpy

class BenchmarkPanel(bpy.types.Panel):
    bl_idname = "BENCHMARK_PT_main"
    bl_label = "Benchmark"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "Benchmark"

    @classmethod
    def poll(cls, context):
        area = context.area
        return area.type == 'NODE_EDITOR' and area.ui_type == 'ShaderNodeTree'

    def draw(self, context):
        layout = self.layout
        layout.label(text="Hello World")

