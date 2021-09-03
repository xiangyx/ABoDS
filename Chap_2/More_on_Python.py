def find_pos(v, x):
    for i in range(len(v)):
        print(f"i = {i}")
        if v[i] >= x:
            return i

v = [1, 3, 5, 7]
print(find_pos(v, 4))
