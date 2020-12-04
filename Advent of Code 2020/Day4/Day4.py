passports = []
mod_pass = []
temp_pass = []
with open('day4testinput.txt', 'r') as infile:
    for row in infile:
        passports.append(row[0:-1])


print(passports)

print(passports[0] + ' ' + passports[1])

for row in passports:
    if row == '':
        mod_pass.append(temp_pass)
        temp_pass = []
    else:
        if temp_pass == []:
            temp_pass.append(row)
        else:
            temp_pass[0] += (' ' + row)
mod_pass.append(temp_pass) # get the last passport

#def create_dicts_from_modpass

print(mod_pass)