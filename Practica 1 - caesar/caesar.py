#!/usr/bin/env python
import argparse

plaintextx = input()
parser = argparse.ArgumentParser()
parser.add_argument("key", type = int)
args = parser.parse_args()

print(parser.key())