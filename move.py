import bpy
import math

# 创建一个新的立方体
bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))
cube = bpy.context.object

# 创建一个新的样条曲线
bpy.ops.curve.primitive_bezier_curve_add(location=(0, 0, 0))
curve = bpy.context.object

# 获取曲线的第一个样条
spline = curve.data.splines[0]

# 添加更多的曲线点
spline.bezier_points.add(5)

# 设置曲线点的位置和控制点
points = [(0, 0, 0), (2, 0, 0), (2, 2, 0), (0, 2, 0), (0, 0, 2), (2, 0, 2)]
for point, coords in zip(spline.bezier_points, points):
    point.co = coords
    point.handle_left = (coords[0] - 1, coords[1], coords[2])
    point.handle_right = (coords[0] + 1, coords[1], coords[2])

# 更新曲线
curve.data.update_tag()

# 添加一个跟踪路径约束
constraint = cube.constraints.new('FOLLOW_PATH')
constraint.target = curve

# 设置动画长度
curve.data.path_duration = 100

# 插入关键帧
curve.data.keyframe_insert(data_path="eval_time", frame=1)
curve.data.eval_time = 100
curve.data.keyframe_insert(data_path="eval_time", frame=100)

# 在初始角度插入关键帧
cube.rotation_euler = (0, 0, 0)
cube.keyframe_insert(data_path="rotation_euler", frame=1)

# 改变立方体的角度
cube.rotation_euler = (0, 0, math.pi / 2)  # 90 degrees

# 在新角度插入关键帧
cube.keyframe_insert(data_path="rotation_euler", frame=50)

# 再次改变立方体的角度
cube.rotation_euler = (0, 0, math.pi)  # 180 degrees

# 在新角度插入关键帧
cube.keyframe_insert(data_path="rotation_euler", frame=100)