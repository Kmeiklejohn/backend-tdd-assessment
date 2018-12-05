#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "???"


import sys
import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Perform transformation on input text.")
    parser.add_argument("-u", "--upper", action="store_true", help="convert text to uppercase")
    parser.add_argument("-l", "--lower", action="store_true", help="convert text to lower")
    parser.add_argument("-t", "--title", action="store_true", help="convertvtext to titlecase")
    parser.add_argument("text", type=str, help="Text to be manipulated")
    return parser


def main(args):
    """Implementation of echo"""
    parser = create_parser()
    answer = parser.parse_args(args)
    args_length = len([x for x in (answer.lower, answer.upper, answer.title)if x is True])
    output = ''

    if answer.upper:
        output = answer.text.upper()
    if answer.lower:
        output = answer.text.lower()
    if answer.title:
        output = answer.text.title()
    if args_length == 0:
        output = answer.text
    
    return output


if __name__ == '__main__':
    print(main(sys.argv[1:]))
