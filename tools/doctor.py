import sys
import shutil
import platform

print("=" * 40)
print(" MuramasaVN Doctor")
print("=" * 40)

print(f"Python : {platform.python_version()}")

git = shutil.which("git")

if git:
    print(f"Git    : OK ({git})")
else:
    print("Git    : NOT FOUND")

print("=" * 40)