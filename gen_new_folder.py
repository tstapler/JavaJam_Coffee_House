#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import re

parser = argparse.ArgumentParser(description='Generate new folders for COMS106')
parser.add_argument('files', metavar='FILE', nargs='+')

args = parser.parse_args()

# Filter Files to correct Folders
files = list(filter(lambda x: "TylerStapler" in x, args.files))

# Find the file with the largest number
last_week = max(files, key=lambda x: list(map(int, re.findall('\d+', x))))

last_week_number = re.findall('\d+', last_week)[1]

this_week = 'TylerStaplerG2WK{}P'.format(int(last_week_number) + 1)
print("Making {}", this_week)

os.makedirs(this_week)
