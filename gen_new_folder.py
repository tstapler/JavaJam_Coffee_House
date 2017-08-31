#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import os
import re

parser = argparse.ArgumentParser(description='Generate new folders for COMS106')
parser.add_argument('files', metavar='FILE', nargs='+')

args = parser.parse_args()

last_week = max(args.files, key=lambda x: list(map(int, re.findall('\d+', x))))

last_week_number = re.findall('\d+', last_week)[1]

os.makedirs('TylerStaplerG2WK{}P'.format(int(last_week_number) + 1))
