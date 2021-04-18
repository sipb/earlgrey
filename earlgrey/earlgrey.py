#!/usr/bin/env python
import argparse

import config as cf

parser = argparse.ArgumentParser(
    description="A framework for SIPB's miscellaneous Discord bots")
parser.add_argument('-f',
                    help="path to config.yaml",
                    dest='config_file',
                    required=True)
args = parser.parse_args()

config = cf.Config()
config.load_file(args.config_file)
