# Proof of Vaccine Decoding

Hacky scripts meant to deconstruct and view the raw contents of the SMART QR code, that is being used for proof of
vaccine in Ontario, mostly just out of curiosity to see what is being stored in it.

## What this does

* Decode the content of the proof of vaccine QR code (Only tested on a very small dataset of Ontario codes)

## What this doesn't do

* Verify that the content is properly signed
* Probably doesn't work for all jurisdiction implementations
* Doesn't support the wider SMART health cards spec
* Doesn't handle errors particularly well, so I wouldn't use this for anything outside of curiosity

## Running

Ensure that `source.png` already exists.

```
./decode.sh source.png > decoded-data.json
```

## Resources

Resources that I used to help determine how to decode the values.

* https://spec.smarthealth.cards/
* https://github.com/ongov/OpenVerify
