from pathlib import Path

START_KEY = 0x5F
MULTIPLIER = 0x15


def decrypt(data):
    key = START_KEY
    out = bytearray()

    for b in data:
        out.append(b ^ key)
        key = (key * MULTIPLIER) & 0xFF

    return bytes(out)


cpk_path = input("NinPri.cpk: ").strip().strip('"')

with open(cpk_path, "rb") as f:
    f.seek(0x10)
    encrypted = f.read(0x2B0)

utf = decrypt(encrypted)

with open("utf_dump.bin", "wb") as f:
    f.write(utf)

print("Saved utf_dump.bin")
print("Size:", len(utf))