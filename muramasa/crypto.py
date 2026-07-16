"""
MuramasaVN
crypto.py

Implements the XOR encryption/decryption used by
Muramasa Rebirth (PS Vita).
"""

from typing import ByteString


class MuramasaCrypto:
    START_KEY = 0x5F
    MULTIPLIER = 0x15

    @classmethod
    def process(cls, data: ByteString) -> bytes:
        key = cls.START_KEY
        output = bytearray()

        for b in data:
            output.append(b ^ key)
            key = (key * cls.MULTIPLIER) & 0xFF

        return bytes(output)

    decrypt = process
    encrypt = process