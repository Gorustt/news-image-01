"""Entry program for make.fun news-image-01.

Copies the pre-made entry image sitting beside this script to the
output directory, byte for byte.

The image is a magazine-cover montage summing up the world news of
13 November 2026 in a single picture: a central globe ringed by seven
labelled vignettes covering the day's biggest stories.
"""

import os
import shutil

SOURCE_NAME = "entry.png"


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(script_dir, SOURCE_NAME)
    if not os.path.isfile(source_path):
        raise FileNotFoundError("entry image not found next to main.py: %s" % source_path)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    dest_path = os.path.join(output_dir, SOURCE_NAME)
    shutil.copyfile(source_path, dest_path)


if __name__ == "__main__":
    main()
