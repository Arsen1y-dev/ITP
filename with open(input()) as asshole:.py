

with open('input.txt', 'r') as asshole:
    line = asshole.read()
    line = (line.split('\n'))
line = list(filter(None, line))
a = line[0]
b = line[1:]
o = str()
for i in b:
    if i.startswith(a):
        str = i
        break
with open('output.txt', 'w') as out_file:
        out_file.write(str)