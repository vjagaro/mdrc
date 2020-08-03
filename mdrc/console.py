import argparse
import sys

from . import convert, __version__


def get_parser():
    parser = argparse.ArgumentParser(
        description='Convert markdown links to reference-links.')
    parser.add_argument('-V', '--version',
                        action='store_true', help='show version')
    parser.add_argument('-i', '--in-place',
                        action='store_true', help='edit in-place')
    parser.add_argument('infile', nargs='?', default='-',
                        type=argparse.FileType('r+', encoding='utf-8'),
                        help='the input path')
    parser.add_argument('outfile', nargs='?',
                        type=argparse.FileType('w', encoding='utf-8'),
                        help='the output path')
    return parser


def run():
    args = get_parser().parse_args()
    if args.version:
        print('mdrc version ' + __version__)
        sys.exit(0)

    text = convert(args.infile.read())

    if args.outfile:
        if args.in_place:
            sys.stderr.write('ERROR: --in-place and outfile specified')
            sys.exit(1)
        out = args.outfile
    elif args.in_place:
        out = args.infile
        out.seek(0)
    else:
        out = sys.stdout

    out.write(text)

    if args.in_place:
        out.truncate()
