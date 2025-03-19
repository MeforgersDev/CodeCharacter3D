import bpy

# Mevcut sahneyi temizlemek için
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# Fonksiyon: Küre oluştur (Baş, eller, ayaklar için)
def create_sphere(name, location, radius, color=(1, 1, 1, 1)):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=radius, location=location)
    obj = bpy.context.object
    obj.name = name
    
    mat = bpy.data.materials.new(name + "_Material")
    mat.diffuse_color = color
    obj.data.materials.append(mat)

    return obj

# Fonksiyon: Silindir oluştur (Gövde, kollar ve bacaklar için)
def create_cylinder(name, location, radius, height, color=(1, 1, 1, 1)):
    bpy.ops.mesh.primitive_cylinder_add(radius=radius, depth=height, location=location)
    obj = bpy.context.object
    obj.name = name
    
    # Malzeme ekleyelim
    mat = bpy.data.materials.new(name + "_Material")
    mat.diffuse_color = color
    obj.data.materials.append(mat)

    return obj

# Fonksiyon: Karakteri oluştur
def create_character():
    # **Baş (Ten rengi)**
    head = create_sphere("Head", (0, 0, 1.6), 0.3, (1, 0.8, 0.6, 1))

    # **Gözler (Beyaz + Siyah)**
    left_eye = create_sphere("Left_Eye", (-0.1, 0.15, 1.75), 0.05, (1, 1, 1, 1))
    right_eye = create_sphere("Right_Eye", (0.1, 0.15, 1.75), 0.05, (1, 1, 1, 1))
    
    left_pupil = create_sphere("Left_Pupil", (-0.1, 0.17, 1.78), 0.02, (0, 0, 0, 1))
    right_pupil = create_sphere("Right_Pupil", (0.1, 0.17, 1.78), 0.02, (0, 0, 0, 1))

    # **Gövde (Tişört)**
    body = create_cylinder("Body", (0, 0, 1.0), 0.3, 0.8, (0.2, 0.6, 1, 1))

    # **Kollar (Ten rengi)**
    left_arm = create_cylinder("Left_Arm", (-0.5, 0, 1.1), 0.1, 0.6, (1, 0.8, 0.6, 1))
    left_arm.rotation_euler = (1.57, 0, 0)

    right_arm = create_cylinder("Right_Arm", (0.5, 0, 1.1), 0.1, 0.6, (1, 0.8, 0.6, 1))
    right_arm.rotation_euler = (1.57, 0, 0)

    # **Eller**
    left_hand = create_sphere("Left_Hand", (-0.5, 0, 1.3), 0.1, (1, 0.8, 0.6, 1))
    right_hand = create_sphere("Right_Hand", (0.5, 0, 1.3), 0.1, (1, 0.8, 0.6, 1))

    # **Bacaklar (Pantolon)**
    left_leg = create_cylinder("Left_Leg", (-0.2, 0, 0.4), 0.12, 0.8, (0.1, 0.1, 0.8, 1))
    right_leg = create_cylinder("Right_Leg", (0.2, 0, 0.4), 0.12, 0.8, (0.1, 0.1, 0.8, 1))

    # **Ayaklar (Ayakkabı)**
    left_foot = create_sphere("Left_Foot", (-0.2, 0, 0), 0.12, (0, 0, 0, 1))
    right_foot = create_sphere("Right_Foot", (0.2, 0, 0), 0.12, (0, 0, 0, 1))

    print("Detaylı karakter oluşturuldu!")

# Karakteri oluştur
create_character()
