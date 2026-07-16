from pathlib import Path
import struct

START_KEY = 0x5F
MULTIPLIER = 0x15


def xor_crypt(data: bytes) -> bytes:
    key = START_KEY
    result = bytearray(len(data))

    for i, value in enumerate(data):
        result[i] = value ^ key
        key = (key * MULTIPLIER) & 0xFF

    return bytes(result)


cpk_path = input("Đường dẫn tới NinPri.cpk: ").strip().strip('"')
path = Path(cpk_path)

if not path.is_file():
    print("Không tìm thấy file.")
    raise SystemExit(1)

with path.open("rb") as file:
    header = file.read(16)

    if header[:4] != b"CPK ":
        print("Đây không phải CPK đã giải mã.")
        raise SystemExit(1)

    table_size = struct.unpack_from("<I", header, 8)[0]
    encrypted_table = file.read(table_size)

decrypted_table = xor_crypt(encrypted_table)

print(f"\nCPK table size: {table_size} bytes (0x{table_size:X})")
print(f"Encrypted signature: {encrypted_table[:4].hex(' ')}")
print(f"Decrypted signature: {decrypted_table[:4].hex(' ')}")
print(f"Decrypted ASCII: {decrypted_table[:4]!r}")

print("\n64 byte đầu của bảng sau giải mã:")

for offset in range(0, min(64, len(decrypted_table)), 16):
    chunk = decrypted_table[offset:offset + 16]
    print(f"{offset:08X}: {chunk.hex(' ')}")