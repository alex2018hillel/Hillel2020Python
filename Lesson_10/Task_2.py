class Add:
    def __init__(self,x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        self.z += other.z
        return None

p1 = Add(2,8,7)
p2 = Add(7,2,4)
s = p1 + p2
res_summa = p1.__dict__
print('x={} \ny={} \nz={}'.format(res_summa['x'], res_summa['y'], res_summa['z'] ))