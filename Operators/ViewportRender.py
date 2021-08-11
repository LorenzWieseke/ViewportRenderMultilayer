import bpy

class ViewportRenderOperator(bpy.types.Operator):
    """Render all Enabled Viewports as seperate Viewport Render Animations"""
    bl_idname = "scene.viewport_render_multilayer"
    bl_label = "Viewport Render Multilayer"

    @classmethod
    def poll(cls, context):
        scene = context.scene
        if len(scene.view_layers) <= 1:
            return False
        else:
            return True
        
    # def invoke(self,context,event):
    #     # self.execute(context)
    #     context.window_manager.modal_handler_add(self)
    #     return {'RUNNING_MODAL'}
    
    # def modal(self,context,event):
       
    #     if event.type == 'LEFTMOUSE':
    #         self.execute(context)
    #         return{'RUNNING_MODAL'}
        
    #     if event.type == 'ESC':
    #         print(event.type)
    #         return{'FINISHED'}
        
    #     return {'PASS_THROUGH'}

    def execute(self, context):
        scene = context.scene
        view_layers = scene.view_layers
        current_path = context.scene.render.filepath
        
        for layer in view_layers:
            if not layer.use:
                continue
                         
            context.window.view_layer = layer
            context.scene.render.filepath = current_path + layer.name + "\\" + layer.name
            bpy.ops.render.opengl(animation=True)
            
        context.scene.render.filepath = current_path
        return {'FINISHED'}
