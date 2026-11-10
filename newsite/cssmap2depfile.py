#!/usr/bin/env python3

import argparse
import json
import os

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=argparse.FileType("rt"), help="CSS map")
    ap.add_argument("output", type=argparse.FileType("wt"), help="depfile")
    args = ap.parse_args()

    m = json.load(args.input)
    args.input.close()

    map_dir = os.path.dirname(args.input.name)

    # The "file" field in the map is relative to the map file location
    css = os.path.join(map_dir, m["file"])
    css = os.path.normpath(css)

    sources = [os.path.join(map_dir, s) for s in m["sources"]]
    sources = [os.path.normpath(s) for s in sources]

    args.output.write(f"{css}: \\\n    ")
    args.output.write(" \\\n    ".join(sources))
    args.output.write("\n")

    args.output.close()

if __name__ == "__main__":
    main()
