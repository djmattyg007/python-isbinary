import argparse

from .check import is_binary


def main(args = None):
    if args is None:
        import sys

        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="Check if a file is binary or not.")

    parser.add_argument("filename", help="Path to a file that should be checked.")

    args = parser.parse_args(args)

    print(is_binary(**vars(args)))
