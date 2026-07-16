"""
MuramasaVN
crypto.py

Implements the XOR encryption/decryption used by
Muramasa Rebirth (PS Vita).
"""

from typing import ByteString


class MuramasaCrypto:
    """Muramasa archive XOR cipher."""

    START_KEY = 0x5F
    MULTIPLIER = 0x15

    @classmethod
    def process(cls, data: ByteString) -> bytes:
        key = cls.START_KEY
        output = bytearray(len(data))

        for i, value in enumerate(data):
            output[i] = value ^ key
            key = (key * cls.MULTIPLIER) & 0xFF

        return bytes(output)

    @classmethod
    def decrypt(cls, data: ByteString) -> bytes:
        return cls.process(data)

    @classmethod
    def encrypt(cls, data: ByteString) -> bytes:
        return cls.process(data)
