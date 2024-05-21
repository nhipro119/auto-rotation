import trimesh
from MeshTweaker import Tweak
import numpy as np
import math
mesh = trimesh.load("87_9.obj")
vertices = mesh.vertices
faces = mesh.faces
fv = []
for i in range(len(faces)):
    for j in range(3):
        # print(vertices[faces[i,j]])
        index = faces[i,j]
        ver = np.expand_dims(vertices[index],axis=0)
        fv.append(ver)
fvv = np.concatenate(fv,axis=0)
# fvv = fvv.reshape(-1,3,3)
# print(faces.shape)
# print(fvv.shape)
# print(fvv[2000,2,:])
# print(vertices[faces[2000,2]])
result = Tweak(fvv,verbose=False, min_volume=True, extended_mode=True)
a = result.matrix
a = np.concatenate((a,np.array([[0,0,0]]).T),axis=1)
a = np.concatenate((a,np.array([[0,0,0,1]])),axis=0)
# rot = trimesh.transformations.quaternion_about_axis(p, v)
add_rotation = trimesh.transformations.rotation_matrix(-0.5*math.pi,[1,0,0])
new_rot = a*add_rotation
print(new_rot)
mesh.apply_transform(a)
mesh.export("test.obj")
