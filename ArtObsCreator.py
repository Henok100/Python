###     Artificial map creator      ###

import random
file = open("Artificalmap.xml", "w")

file.write("<environment>\n")
file.write('<material id="1" resistivity="100" relativePermittivity="4.5" relativePermeability="1" /> <!-- concrete-->\n')

for i in range(-800, 820, 20):
    if i == 220 or i == 200 or i == -220 or i == -200 or i == -620 or i == -600 or i == 620 or i == 600:
        continue
    for j in range(-800, 820, 20):
        if j == 220 or j == 200 or j == -220 or j == -200 or j == -620 or j == -600 or j == 620 or j == 600:
            continue
        x = f'<object position="min {i} {j} 0" orientation=" 0 0 0" shape="cuboid 10 10 {random.randint(30, 150)} " material="1" />\n'
        file.write(x)

file.write('</environment>')

file.close()