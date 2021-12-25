# get dots
template = list("KOKHCCHNKKFHBKVVHNPN")
# template = list("NNCB")

char = dict()

power_template = dict()
pairs = dict()
with open('day14_input.txt', 'r') as infile:
    for row in infile:
        row = (row.strip('\n').split(' -> '))
        pairs[row[0]] = row[1]
        char[row[1]] = 0
print(pairs)


for character in template:
    if character in char.keys():
        char[character] = char.get(character) + 1
    else:
        char[character] = 1
print("chars: ", char)

for pair in pairs:
    power_template[pair] = 0
print("power_template: ", power_template)

def get_step_pairs(template):
    step_pairs = []
    i=0
    while i < len(template)-1:
        step_pairs.append(template[i:i+2])
        i+=1
    return step_pairs

step_pairs = get_step_pairs(template)
for pair in step_pairs:
    power_template[''.join(pair)] = power_template.get(''.join(pair)) + 1

step = 0
steps = 40
print("power_temp: " , power_template)
while step < steps:
    temp_template = dict()
    for key in power_template:
        char[pairs[key]] = char.get(pairs[key]) + power_template[key]
        if key[0]+pairs[key] in temp_template.keys():
            temp_template[key[0]+pairs[key]] = temp_template.get(key[0]+pairs[key]) + power_template[key]
        else:
            temp_template[key[0]+pairs[key]] = power_template[key]
        if pairs[key]+key[1] in temp_template.keys():
            temp_template[pairs[key]+key[1]] = temp_template.get(pairs[key]+key[1]) + power_template[key]
        else:
            temp_template[pairs[key] + key[1]] = power_template[key]
        if key in temp_template.keys():
            temp_template[key] = temp_template.get(key)-(power_template[key])
        else:
            temp_template[key] = -(power_template[key])
    for key in temp_template:
        power_template[key] = power_template.get(key) + temp_template[key]
    print("power_temp: " , power_template)
    step+=1

max = 0
min = float('inf')
for c in char.keys():
    if char[c] > max:
        max = char[c]
    if char[c] < min:
        min = char[c]
print(max, min, max-min)