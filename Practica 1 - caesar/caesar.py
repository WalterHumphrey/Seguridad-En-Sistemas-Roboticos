#!/usr/bin/env python
import argparse

plaintext = input()
parser = argparse.ArgumentParser()
parser.add_argument("key", type = int)
args = parser.parse_args()

plaintext.lower()
print(args.key)
print(plaintext)