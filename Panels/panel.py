import bpy
              
# class GTT_ResolutionPanel(bpy.types.Panel):
#     bl_idname = "ViewportRender_PT_main_panel"
#     bl_label = "Render"
#     bl_space_type = "VIEW_3D"
#     bl_region_type = "UI"
#     bl_category = 'Viewport Render'
#     bl_order = 0

def draw_menu(self, context):
    layout = self.layout
    
    layout.operator("scene.viewport_render_multilayer",icon="RENDERLAYERS")
    

def register():
    bpy.types.VIEW3D_MT_view.append(draw_menu)


def unregister():
    bpy.types.VIEW3D_MT_view.remove(draw_menu)
