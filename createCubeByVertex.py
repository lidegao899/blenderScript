import bpy
import bmesh

# 定义顶点列表
verts = [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)]

# 创建一个新的网格对象
mesh = bpy.data.meshes.new(name="New Cube Mesh")
obj = bpy.data.objects.new("New Cube", mesh)

# 将新对象添加到场景中
scene = bpy.context.scene
scene.collection.objects.link(obj)

# 创建一个bmesh对象
bm = bmesh.new()

# 添加顶点到bmesh对象
bm_verts = [bm.verts.new(v) for v in verts]

# 创建立方体的面
bm.faces.new(bm_verts[i] for i in (0, 1, 2, 3))  # 底面
bm.faces.new(bm_verts[i] for i in (4, 5, 6, 7))  # 顶面
bm.faces.new(bm_verts[i] for i in (0, 1, 5, 4))  # 侧面1
bm.faces.new(bm_verts[i] for i in (1, 2, 6, 5))  # 侧面2
bm.faces.new(bm_verts[i] for i in (2, 3, 7, 6))  # 侧面3
bm.faces.new(bm_verts[i] for i in (3, 0, 4, 7))  # 侧面4

# 更新bmesh到网格
bm.to_mesh(mesh)
bm.free()