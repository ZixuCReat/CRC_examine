# C(x)= x^rK(x) + R(x)
# CRC_4  X4 + X1 +1          0X03
# CRC_8  X8 + X2 + X1 + 1    0X07
# CRC_16/IBM  X16 + X16 +X2 +1    0X8005


def bin_tool(poly):
    # 多项式处理
    poly = ''.join(filter(lambda a: a in '0123456789+', poly))
    temp_poly = list(poly.split('+'))
    string = temp_poly[-1]
    del temp_poly[-1]
    temp_poly = temp_poly[::-1]
    # 二进制
    for i in range(len(temp_poly)):
        if len(string) == int(temp_poly[i]):
            string += "1"
        else:
            for j in range(int(temp_poly[i]) - len(string)):
                string += "0"
            string += "1"
        return string[::-1]


def xor_tool(string1, string2):
    # 初始化结果
    xor_result = str()
    # 补0
    if len(string1) < len(string2):
        for i in range(len(string2) - len(string1)):
            string2 = '0' + string2
    elif len(string1) > len(string2):
        for i in range(len(string1) - len(string2)):
            string1 = '0' + string1
    # 异或
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            xor_result = '1' + xor_result
        elif string1[i] == string2[i]:
            xor_result = '0' + xor_result
    # 无效0处理
    for i in range(len(xor_result)):
        if xor_result[i] == '1':
            return xor_result[i::]
    return xor_result


def crc(string, poly):
    # 初始化crc码
    crc_code = str()
    # 预处理
    bin_poly = bin_tool(poly)
    for i in range(len(bin_poly) - 1):
        string = string + '0'


s = input()
s = bin_tool(s)
print(s)
