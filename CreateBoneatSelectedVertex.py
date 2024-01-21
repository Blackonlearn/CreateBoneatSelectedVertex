bl_info = {
    "name": "Create Bone at Selected Vertices",
    "author": "JR",
    "version": (1, 0),
    "blender": (3, 3, 0),
    "location": "Vertex > Create Bone at Selected Vertices",
    "description": "Create a bone at each selected vertex of the active object's mesh",
    "category": "Object"
}

import bpy
import bmesh
from mathutils import Vector, Matrix
from mathutils import Euler


#----------------------------------------------
#Panel for Create Bones                       |
#----------------------------------------------


class CreateBonesPanel(bpy.types.Panel):
    bl_label = "Create Bones Panel"
    bl_idname = "OBJECT_PT_create_bones_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Create Bones at Selected Vertices" 
    

    def draw(self, context):
        layout = self.layout
        #layout.operator("object.create_bones_at_vertices", text="Create Bones in Normal")
        
        row = layout.row()
        row.operator("object.create_bones_at_vertices_normal_pos", text="Create Bones in Normal" , icon = "CONSTRAINT_BONE")

        row = layout.row()
        row.operator("object.create_bones_at_vertices_z_pos", text="Create Bones in °Z" , icon = "CONSTRAINT_BONE")
        
        row = layout.row()
        row.operator("object.create_bones_at_vertices_y_pos", text="Create Bones in °Y" , icon = "CONSTRAINT_BONE")
        
        row = layout.row()
        row.operator("object.create_bones_at_vertices_x_pos", text="Create Bones in °X" , icon = "CONSTRAINT_BONE")

        
                



#----------------------------------------------
#Panel for Create Customs Shapes              |
#----------------------------------------------


class CreateCustomsShapesPanel(bpy.types.Panel):
    bl_label = "Create Custom Shapes Panel"
    bl_idname = "OBJECT_PT_create_customs_shapes_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Create Customs Shapes at selected Bones" 
    bl_parent_id = "OBJECT_PT_create_bones_panel"

    def draw(self, context):
        
        layout = self.layout
            
        # Show a label for the custom shape
        row = layout.row()
        row.label(text="Custom Shape:")
        row = layout.row()
        row.prop(context.scene, "radius")
        row = layout.row()             
        # Add a button to apply the circle custom shape to all selected bones
        row.operator("object.create_circle", text="Circle", icon = "MESH_CIRCLE")
        row = layout.row()
        
        
   
#----------------------------------------------
#Create bone at vertices in normal orientation |
#----------------------------------------------

#______________________________________________________________________________________________________________




class CreateBonesAtVerticesNormalPos(bpy.types.Operator):
    bl_idname = "object.create_bones_at_vertices_normal_pos"
    bl_label = "Create Bones at Selected Vertices in normal pos"
    bl_description = "Create a bone at each selected vertex of the active object's mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        mesh = obj.data

        # Create a new armature object
        armature = bpy.data.armatures.new(name="Armature")
        armature_obj = bpy.data.objects.new(name="Armature", object_data=armature)
        context.collection.objects.link(armature_obj)

        # Enter edit mode for the armature
        bpy.context.view_layer.objects.active = armature_obj
        bpy.ops.object.mode_set(mode='EDIT')

        # Create a new bone for each selected vertex
        for vert in mesh.vertices:
            if vert.select:
                bone = armature.edit_bones.new(name="Bone")
                bone.head = obj.matrix_world @ vert.co
                bone.tail = bone.head + (obj.matrix_world @ vert.normal)
            
                
        # Exit edit mode for the armature
        bpy.ops.object.mode_set(mode='OBJECT')

        # Set the armature as the parent of the object
        #obj.parent = armature_obj

        return {'FINISHED'}


#-----------------------------------------
#Create bone at vertices in z orientation |
#-----------------------------------------

    
class CreateBonesAtVerticesZpos(bpy.types.Operator):
    bl_idname = "object.create_bones_at_vertices_z_pos"
    bl_label = "Create Bones at Selected Vertices in z pos"
    bl_description = "Create a bone at each selected vertex of the active object's mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        mesh = obj.data

        # Create a new armature object
        armature = bpy.data.armatures.new(name="Armature")
        armature_obj = bpy.data.objects.new(name="Armature", object_data=armature)
        context.collection.objects.link(armature_obj)

        # Enter edit mode for the armature
        bpy.context.view_layer.objects.active = armature_obj
        bpy.ops.object.mode_set(mode='EDIT')

        # Create a new bone for each selected vertex
        for vert in mesh.vertices:
            if vert.select:
                bone = armature.edit_bones.new(name="Bone")
                bone.head = obj.matrix_world @ vert.co
                tail = bone.head + obj.matrix_world @ Vector((0,0,1))
                bone.tail = tail
             
                 

        # Exit edit mode for the armature
        bpy.ops.object.mode_set(mode='OBJECT')

        # Set the armature as the parent of the object
        #obj.parent = armature_obj

        return {'FINISHED'}


#-----------------------------------------
#Create bone at vertices in y orientation |
#-----------------------------------------

    
class CreateBonesAtVerticesYpos(bpy.types.Operator):
    bl_idname = "object.create_bones_at_vertices_y_pos"
    bl_label = "Create Bones at Selected Vertices in z pos"
    bl_description = "Create a bone at each selected vertex of the active object's mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        mesh = obj.data

        # Create a new armature object
        armature = bpy.data.armatures.new(name="Armature")
        armature_obj = bpy.data.objects.new(name="Armature", object_data=armature)
        context.collection.objects.link(armature_obj)

        # Enter edit mode for the armature
        bpy.context.view_layer.objects.active = armature_obj
        bpy.ops.object.mode_set(mode='EDIT')

        # Create a new bone for each selected vertex
        for vert in mesh.vertices:
            if vert.select:
                bone = armature.edit_bones.new(name="Bone")
                bone.head = obj.matrix_world @ vert.co
                tail = bone.head + obj.matrix_world @ Vector((0,1,0))
                bone.tail = tail
             
                 

        # Exit edit mode for the armature
        bpy.ops.object.mode_set(mode='OBJECT')

        # Set the armature as the parent of the object
        #obj.parent = armature_obj

        return {'FINISHED'}

#-----------------------------------------
#Create bone at vertices in x orientation |
#-----------------------------------------
    
class CreateBonesAtVerticesXpos(bpy.types.Operator):
    bl_idname = "object.create_bones_at_vertices_x_pos"
    bl_label = "Create Bones at Selected Vertices in z pos"
    bl_description = "Create a bone at each selected vertex of the active object's mesh"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        mesh = obj.data

        # Create a new armature object
        armature = bpy.data.armatures.new(name="Armature")
        armature_obj = bpy.data.objects.new(name="Armature", object_data=armature)
        context.collection.objects.link(armature_obj)

        # Enter edit mode for the armature
        bpy.context.view_layer.objects.active = armature_obj
        bpy.ops.object.mode_set(mode='EDIT')

        # Create a new bone for each selected vertex
        for vert in mesh.vertices:
            if vert.select:
                bone = armature.edit_bones.new(name="Bone")
                bone.head = obj.matrix_world @ vert.co
                tail = bone.head + obj.matrix_world @ Vector((1,0,0))
                bone.tail = tail
            
                
                

        # Exit edit mode for the armature
        bpy.ops.object.mode_set(mode='OBJECT')

        # Set the armature as the parent of the object
        #obj.parent = armature_obj

        return {'FINISHED'}
    
    
#-----------------------
#Create Customs Shapes |
#-----------------------

def create_circle(radius, context, rotation):
    
    me = bpy.data.meshes.new('Circle')
    bm = bmesh.new()
    bmesh.ops.create_circle(bm, radius=radius, segments=32)
    bm.to_mesh(me)
    bm.free()
    obj = bpy.data.objects.new('Circle', me)
    
    bpy.context.scene.collection.objects.link(obj)
        
    armature_obj = bpy.context.active_object
    
    selected_bones = context.selected_pose_bones
    
    # Apply the circle custom shape to each selected bone
    if not selected_bones:
        self.report({"ERROR"}, "No pose bones selected.")
        return {"CANCELLED"}
    
    rotation_euler = Euler(rotation, 'XYZ')
    rotation_euler.rotate_axis('X', 1.57)
       
    for bone in selected_bones: 
        bone.custom_shape = obj
        bone.custom_shape_rotation_euler = rotation_euler
    
    return {'FINISHED'}
           
    

class OBJECT_OT_create_circle(bpy.types.Operator):
    
    bl_idname = "object.create_circle"
    bl_label = "Circle"
    
    rotation: bpy.props.FloatVectorProperty(name="Rotation", size=3, default=(0, 0, 0), subtype='EULER')
    
    def execute(self, context):
        create_circle(context.scene.radius, context, self.rotation)
        return {'FINISHED'} 
           


def menu_func(self, context):
    self.layout.operator(CreateBonesAtVerticesNormalPos.bl_idname, icon='CONSTRAINT_BONE')

def register():
    
    bpy.types.Scene.radius = bpy.props.FloatProperty(name="radius", default=1.0)
    bpy.types.Scene.selected_bone = bpy.props.StringProperty(name="Selected Bone")
    bpy.utils.register_class(CreateBonesPanel)
    bpy.utils.register_class(CreateCustomsShapesPanel)
    bpy.utils.register_class(CreateBonesAtVerticesNormalPos)
    bpy.utils.register_class(CreateBonesAtVerticesZpos)
    bpy.utils.register_class(CreateBonesAtVerticesYpos)
    bpy.utils.register_class(CreateBonesAtVerticesXpos)
    bpy.utils.register_class(OBJECT_OT_create_circle)

    


def unregister():
    
    del bpy.types.Scene.radius
    del bpy.types.Scene.selected_bone
    bpy.utils.unregister_class(CreateBonesPanel)
    bpy.utils.unregister_class(CreateCustomsShapesPanel)
    bpy.utils.unregister_class(CreateBonesAtVerticesNormalPos)
    bpy.utils.unregister_class(CreateBonesAtVerticesZpos)
    bpy.utils.unregister_class(CreateBonesAtVerticesYpos)
    bpy.utils.unregister_class(CreateBonesAtVerticesXpos)
    bpy.utils.unregister_class(OBJECT_OT_create_circle)
    




if __name__ == "__main__":
    register()