import bpy

# Tên đối tượng bạn muốn thay đổi vị trí
object_name ="Armature"

# Lấy đối tượng từ tên
object = bpy.data.objects[object_name]

def change_position(x, y, z):
    # Đặt vị trí mới cho đối tượng
    object.location = (x, y, z)

# Sử dụng hàm change_position để thay đổi vị trí đối tượng
change_position(0,0,0)
