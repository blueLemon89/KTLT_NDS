import bpy
import random

# Tên đối tượng bạn muốn thay đổi màu sắc
object_name = "Object_9"

# Lấy đối tượng từ tên
object = bpy.data.objects[object_name]

# Tạo một vật liệu mới cho đối tượng
material = bpy.data.materials.new(name="NewColor")
object.data.materials.append(material)

def change_color(scene):
    # Tạo một giá trị màu sắc ngẫu nhiên
    color = (random.random(), random.random(), random.random(), 1)
    
    # Đặt giá trị màu sắc mới cho vật liệu
    material.diffuse_color = color
    
    # Áp dụng vật liệu cho đối tượng
    object.active_material = material

# Đặt một handler để gọi hàm change_color sau khi chuyển khung hình
bpy.app.handlers.frame_change_post.append(change_color)
