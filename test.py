from opensimplex import OpenSimplex


gen = OpenSimplex()
def noise(nx, ny):
    # Rescale from -1.0:+1.0 to 0.0:1.0
    return gen.noise2d(nx, ny) / 2.0 + 0.5

value = []
for y in range(Settings.wymiaryMapyx):
    value.append([0] * Settings.wymiaryMapyy)
    for x in range(Settings.wymiaryMapyy):
        nx = x/Settings.wymiaryMapyy - 0.5
        ny = y/Settings.wymiaryMapyx - 0.5
        value[y][x] = noise(nx, ny)

print(len(value))
print((value))