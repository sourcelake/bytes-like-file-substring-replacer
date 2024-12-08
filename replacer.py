import argparse
from lakespack import colourfulconsole as cc
console = cc.Console()
def parse():
    parser = argparse.ArgumentParser("Bytes-type file substring replacer")
    parser.add_argument("file")
    parser.add_argument("search")
    parser.add_argument("replace")
    parser.add_argument("-s", help="Start, index start to search for the string.", default=0, type=int)
    parser.add_argument("-e", help="End/Stop, index stop to search for the string.", default=None, type=int)
    return parser.parse_args()


args = parse()

with open(args.file, "rb") as f:
    file = f.read()
    if args.e != None:
        idx = file.find(args.search.encode(), args.s, args.e)
    else:
        idx = file.find(args.search.encode(), args.s, len(file))

    if idx == -1:
        console.error("Error: Search string not found in file.")

    print(idx)
    print(len(args.search))
    
    file = bytearray(file)
    file[idx:idx+len(args.search.encode())] = args.replace.encode() # "This program cannot be run in DOS mode." is normally idx 78, the length of the DOS prompt is 39, so its [78:117]
    file = bytes(file)


with open(args.file, "wb") as f:
    f.write(file)
