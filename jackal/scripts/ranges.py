#!/usr/bin/env python3
"""
Script to list all of the ranges
"""
from jackal import Core, Range
from jackal.utils import print_json, print_line

core = Core()


def main():
    response = core.get_ranges()
    if isinstance(response, int):
        print_line("Number of ranges: {}".format(response))
    else:
        for hit in response:
            hit = hit.to_dict(include_meta=True)
            source = hit.pop('_source')
            print_json({**hit, **source})


if __name__ == '__main__':
    main()
