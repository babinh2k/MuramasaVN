from pathlib import Path
import struct

START_KEY = 0x5F
MULTIPLIER = 0x15


def decrypt(data):
    key = START_KEY
    out = bytearray()

    for b in data:
        out.append(b ^ key)
        key = (key * MULTIPLIER) & 0xFF

    return bytes(out)


path = input("NinPri.cpk: ").strip().strip('"')

with open(path, "rb") as f:

    f.seek(0x10)

    encrypted = f.read(0x2B0)

utf = decrypt(encrypted)

print("Magic:", utf[0:4])

print()

for offset in range(0, 128, 16):
    chunk = utf[offset:offset + 16]
    print(f"{offset:04X}: {chunk.hex(' ')}")