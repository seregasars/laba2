import math
from copy import deepcopy

txt = input()


def addModuleTwo(x, y, module=2 ** 32):
    return ((x + y) % module)


def bitShift(s, sh):
    s = bin(s)[2:]
    s = int((s[sh:] + s[:sh]), 2)
    return s


def F(B, C, D):
    return (B & C | ~B & D)


def G(B, C, D):
    return (B & D | ~D & C)


def H(B, C, D):
    return (B ^ C ^ D)


def I(B, C, D):
    return (C ^ (B | ~D))


A = 0x12AC2375
B = 0x3B341042
C = 0x5F62B97C
D = 0x4BA763E
buffers = [A, B, C, D]

text = ''
for i in txt:
    text += hex(ord(i))[2:]
startLength = str(hex(len(text) * 4))
text += '8'
text += ('0' * (112 - len(text) % 128 + 4))
text = text + '0' * (16 - len(startLength)) + startLength[2:]

T = []
for i in range(1, 65):
    T.append(round(2 ** 32 * abs(math.sin(i))))

S = [[7, 12, 17, 22], [5, 9, 14, 20], [4, 11, 16, 23], [6, 10, 15, 21]]
MasOfFunctions = [F, G, H, I]

parts = []
for i in range(2, len(text), 128):
    parts.append(text[i:i + 128])

for i in range(len(parts)):
    part = deepcopy(parts[i])
    parts[i] = []
    for j in range(0, 128, 8):
        parts[i].append(int(part[j:j + 8], 16))

countForT = 0
for i in range(len(parts)):
    for r in range(4):
        for j in range(len(parts[i])):
            bCopy = deepcopy(buffers)
            curFunc = MasOfFunctions[r](buffers[1], buffers[2], buffers[3])
            buffers[0] = addModuleTwo(buffers[0], curFunc)
            buffers[0]=addModuleTwo(buffers[0], parts[i][j])
            buffers[0] = addModuleTwo(buffers[0], T[countForT])
            buffers[0] = bitShift(buffers[0], S[r][i // 4])
            buffers[0] = addModuleTwo(buffers[0], bCopy[0])
            buffers = buffers[3:4] + buffers[0:3]
            countForT += 1

hexStr = '0x'
for i in buffers:
    h = hex(i)[2:]
    if len(h) < 8:
        h = '0' * (8 - len(h)) + h
    hexStr += h

print(hexStr)

0x8c884ee850e3430a99b6ad62126ab7d1