# Define the outer list
M2 = []
M4 = []
M6 = []
M8 = []
M10 = []

def Mov2():
    for i in range(3):
        x = 220
        y = -900
        z = 0
        while y <= 620:
            M2.append([x, y, z])
            y = y + 2

        # while x >= -220:
        #     M2.append([x, y, z])
        #     x = x - 2

        # while y >=-850:
        #     M2.append([x, y ,z])
        #     y = y - 2
    return M2

def Mov4():
    for i in range(3):
        x = 220
        y = -850
        z = 0
        while y <= 620:
            M4.append([x, y, z])
            y = y + 2

        # while x >= -220:
        #     M4.append([x, y, z])
        #     x = x - 2

        # while y >=-800:
        #     M4.append([x, y ,z])
        #     y = y - 2
    return M4

def Mov6():
    for i in range(3):
        x = 220
        y = -800
        z = 0
        while y <= 620:
            M6.append([x, y, z])
            y = y + 2

        # while x >= -220:
        #     M6.append([x, y, z])
        #     x = x - 2

        # while y >=-800:
        #     M6.append([x, y ,z])
        #     y = y - 2
    return M6

def Mov8():
    for i in range(3):
        x = 220
        y = -750
        z = 0
        while y <= 620:
            M8.append([x, y, z])
            y = y + 2

        # while x >= -220:
        #     M8.append([x, y, z])
        #     x = x - 2

        # while y >=-800:
        #     M8.append([x, y ,z])
        #     y = y - 2
    return M8

def Mov10():
    for i in range(3):
        x = 220
        y = -700
        z = 0
        while y <= 620:
            M10.append([x, y, z])
            y = y + 2

        # while x >= -220:
        #     M10.append([x, y, z])
        #     x = x - 2

        # while y >=-800:
        #     M10.append([x, y ,z])
        #     y = y - 2
    return M10