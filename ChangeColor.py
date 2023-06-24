import bpy

# Tên đối tượng bạn muốn thay đổi màu sắc
object_name = "Object_9"

# Lấy đối tượng từ tên
object = bpy.data.objects[object_name]

# Tạo một vật liệu mới cho đối tượng
material = bpy.data.materials.new(name="NewColor")
object.data.materials.append(material)

# Đặt giá trị màu sắc mới cho vật liệu
material.diffuse_color = (1, 0 ,0,  1)  # Thay đổi R, G, B thành giá trị màu mong muốn

# Áp dụng vật liệu cho đối tượng
object.active_material = material

# Kích hoạt chế độ chạy script trong Blender
bpy.app.driver_namespace["__name__"] = "__main__"

# Xóa tất cả các handler hiện có
bpy.app.handlers.frame_change_pre.clear()

# Chạy các handler khi chuyển khung hình
bpy.app.handlers.frame_change_pre.append(change_color)
