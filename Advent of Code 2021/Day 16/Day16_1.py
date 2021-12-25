hex_dict = dict()
hex_dict["0"] = "0000"
hex_dict["1"] = "0001"
hex_dict["2"] = "0010"
hex_dict["3"] = "0011"
hex_dict["4"] = "0100"
hex_dict["5"] = "0101"
hex_dict["6"] = "0110"
hex_dict["7"] = "0111"
hex_dict["8"] = "1000"
hex_dict["9"] = "1001"
hex_dict["A"] = "1010"
hex_dict["B"] = "1011"
hex_dict["C"] = "1100"
hex_dict["D"] = "1101"
hex_dict["E"] = "1110"
hex_dict["F"] = "1111"
print(hex_dict)

input = "D2FE28"
bin_s = ""
for hex in input:
    bin_s+=(hex_dict[hex])
print(bin_s)

def parse_bin(packet):
    versions = []
    vers = ""
    for i in range(3):
        vers+=packet[i]
    versions.append(vers)

    type = ""
    for i in range(3,6):
        type+=packet[i]
    if type == "100":
        return parse_literal(packet[6::])
    else:
        return parse_operator(packet[6::])

def parse_literal(packet):
    literal = ""
    while packet[0]!="1":
        packet=packet[1::]
    while packet[0] != "0":
        literal += packet[1:5]
        packet = packet[5::]
        if len(packet) < 5:
            return convert_str_bin_to_int(literal)



def convert_str_bin_to_int(str_bin):
    str_bin = list(str_bin)
    str_bin.reverse()
    encoded_bin = 0
    for i in range(len(str_bin)):
        encoded_bin += int(str_bin[i])*(2**i)
    return encoded_bin

def parse_operator(packet):
    length = 0
    if packet[0] == "0":
        length = 15
    else:
        length = 11

    for i in range(length):
        pass

# print(parse_bin(bin_s))

L = "000000000011011"
A = "11010001010"
B = "0101001000100100"
print(convert_str_bin_to_int(L),parse_literal(A), parse_literal(B))
