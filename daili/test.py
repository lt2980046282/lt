from werkzeug.routing import Map


class Dic():
    def __init__(self,):
        pass

    def __setitem__(self, key, value):
        self.key = value

    def __str__(self):
        return "%s" % (self.key)

a1 = a2 = 65
dc = Dic()
for i in range(1, 677):
    if a2 > 90:
        a1 += 1
        a2 = 65
    key = f'{str(bytes([a1]) + bytes([a2]))}'
    dc[key] = i
    print(dc[key])
    a2 += 1

print(dc['1'])


