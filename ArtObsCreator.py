###     Artificial map creator      ###

import random
file = open("Artificalmap.xml", "w")

file.write("<environment>\n")
file.write('<material id="1" resistivity="100" relativePermittivity="4.5" relativePermeability="1" /> <!-- concrete-->\n')

for i in range(-900, 920, 20):
    if i == 240 or i == 220 or i == 200 or i == -240 or i == -220 or i == -200 or i == -640 or i == -620 or i == -600 or i == 640 or i == 620 or i == 600 or i == 0:
        continue
    for j in range(-900, 920, 20):
        if j == 240 or j == 220 or j == 200 or j == -240 or j == -220 or j == -200 or j == -640 or j == -620 or j == -600 or j == 640 or j == 620 or j == 600 or i == 0:
            continue
        x = f'<object position="min {i} {j} 0" orientation=" 0 0 0" shape="cuboid {random.randint(10, 15)} {random.randint(10, 15)} {random.randint(40, 150)} " material="1" />\n'
        file.write(x)

file.write('</environment>')

file.close()