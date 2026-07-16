from pathlib import Path
from muramasa.crypto import MuramasaCrypto

CPK_FILE = Path("NinPri.cpk")

if not CPK_FILE.exists():
    print("Không tìm thấy NinPri.cpk")
    raise SystemExit

with CPK_FILE.open("rb") as fp:
    data = fp.read(64)

decoded = MuramasaCrypto.decrypt(data)

print("Encrypted:")
print(data[:16].hex(" "))

print()

print("Decrypted:")
print(decoded[:16].hex(" "))

try:
    print()
    print(decoded[:4].decode())
except:
    pass
