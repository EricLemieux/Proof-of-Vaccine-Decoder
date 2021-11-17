#!/usr/bin/env python3

import base64
import zlib


def decode_base64(encoded: str) -> bytes:
    # They replace these characters in the government app, not 100% sure why as of right now
    # https://github.com/ongov/OpenVerify/blob/3f60e992d24dedf31ec6a0d11eacdcaf646bc9f9/src/services/QRCodeValidator/lib/utils/utils.ts#L28
    encoded = encoded.replace('-', '+')
    encoded = encoded.replace('_', '/')
    padded = encoded + '=' * (-len(encoded) % 4)
    return base64.b64decode(padded)


raw_data = input()

split = raw_data.split('.')
header = decode_base64(split[0])
payload = decode_base64(split[1])
signature = decode_base64(split[2])

# Print the decoded FHIR data
# -15 is a magic number that I don't understand but it fixes the decompression, something to do with the zlib headers
# being omitted for size limitations...
print(zlib.decompress(payload, -15).decode('utf-8'))
