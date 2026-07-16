from pathlib import Path
import struct

cpk_path = input("Đường dẫn tới NinPri.cpk: ").strip()

path = Path(cpk_path)

with path.open("rb") as f:
    data = f.read(64)

print("Magic:", data[0:4])

print("")

for offset in range(0, 64, 16):
    chunk = data[offset:offset + 16]
    print(f"{offset:08X}: {chunk.hex(' ')}")

print("")
print("DWORD @ 0x08 :", struct.unpack("<I", data[8:12])[0])
print("DWORD @ 0x0C :", struct.unpack("<I", data[12:16])[0])
print("DWORD @ 0x10 :", struct.unpack("<I", data[16:20])[0])
print("DWORD @ 0x14 :", struct.unpack("<I", data[20:24])[0])