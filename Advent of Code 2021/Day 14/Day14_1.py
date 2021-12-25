# get dots
template = list("KOKHCCHNKKFHBKVVHNPN")
template = list("NNCB")
template_set = set(template)
print(template_set)
power_template = dict()
pairs = dict()
with open('day14_input_sample.txt', 'r') as infile:
    for row in infile:
        row = (row.strip('\n').split(' -> '))
        pairs[row[0]] = row[1]
print(pairs)
for pair in pairs:
    power_template[pair] = 0
# print(power_template)
# print(len(power_template))
# print(pairs)
def get_step_pairs(template):
    step_pairs = []
    i=0
    while i < len(template)-1:
        step_pairs.append(template[i:i+2])
        i+=1
    return step_pairs

step = 0
steps = 3
char_counts = dict()
while step < steps:
    step_pairs = get_step_pairs(template)
    insertion_index = 1
    for pair in step_pairs:
        insertion = pairs[''.join(pair)]
        template.insert(insertion_index,insertion)
        insertion_index +=2
    step+=1
    print(len(template))
    for char in template_set:
        char_counts[char] = template.count(char)
    print(char_counts)
max=0
min=float('inf')
for char in template_set:
    if template.count(char) > max:
        max = template.count(char)
    if template.count(char) < min:
        min = template.count(char)
print(max-min)
