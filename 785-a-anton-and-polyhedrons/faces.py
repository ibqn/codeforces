n = int(input())

faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}

count = sum(faces[input()] for _ in range(n))

print(count)
