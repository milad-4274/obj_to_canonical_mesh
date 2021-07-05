import numpy as np


class Vertex:
    x: float
    y: float
    z: float
    xn: float = 0.0
    yn: float = 0.0

    def __init__(self,x,y,z):
        self.x = x;
        self.y = y;
        self.z = z;


    

obj_name = "test.obj"
output_name = "file.txt"

with open(obj_name,"r") as f:
    lines = f.readlines()


vertices = []
indices = []

vs = 0


face_elements = {}
vts = {}

for i,line in enumerate(lines):
    if line.startswith("v "):
        res = line.split()
        v = Vertex(float(res[1]),float(res[2]),float(res[3]))
        vertices.append(v)
        vs += 1

    elif line.startswith("vt "):
        res = line.split()
        vts[i-vs] = (res[1],str(1-float(res[2])))

    elif line.startswith("f "):
        res = line.split()
        for re in res[1:]:
            k,v = re.split("/")
            face_elements[int(k)-1] = int(v) -1
            indices.append(int(k)-1)


for key, value in face_elements.items():
    vertices[key].xn = vts[value][0]
    vertices[key].yn = vts[value][1]

print("number of vertices: ",len(vertices))

print("number of indices: ",len(indices))


with open(output_name, "w") as f:
    f.write("canonical_mesh: {\n")
    f.write("  vertex_type: VERTEX_PT\n")
    f.write("  primitive_type: TRIANGLE\n")
    for v in vertices:
        f.write(f"  vertex_buffer: {str(v.x)}\n")
        f.write(f"  vertex_buffer: {str(v.y)}\n")
        f.write(f"  vertex_buffer: {str(v.z)}\n")
        f.write(f"  vertex_buffer: {str(v.xn)}\n")
        f.write(f"  vertex_buffer: {str(v.yn)}\n")
    for i in indices:
        f.write(f"  index_buffer: {str(i)}\n")
    f.write("}")
    print(f"file {output_name} wrote successfully")
        
        
        
        

        