import math
def volume_of_sphere(radius):
    return (4/3) * math.pi * (radius ** 3)

rad = int(input("Enter the radius of the sphere: "))
print("The volume of the sphere is:" + str(volume_of_sphere(rad)))
