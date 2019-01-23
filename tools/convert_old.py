"""Convert all the old posts.

Author: Alex Alemi
Date: 2019-01-23
"""

import os
import logging

CURRENT_DIR = os.path.dirname(__file__)
POSTS_DIR = os.path.normpath(os.path.join(CURRENT_DIR, '../posts/old'))

def fix_front(line):
    """Redo the front of the metadata lines for the nikola format."""
    return '.. ' + line[0].lower() + line[1:]

def has_math(lines):
    """Test if math appears anywhere in the post."""
    for line in lines:
        if '$$' in line:
            return True
        elif '$' in line:
            return True
    return False


def fix_preamble(lines):
    """Convert the preamble to the correct form."""

    # get the first empty line
    first_empty_line = lines.index('\n')
    if first_empty_line == 0:
        raise Exception()

    preamble = [fix_front(line) for line in lines[:first_empty_line]] 
    if has_math(lines):
        preamble.append('.. has_math: true\n')
    
    lines = ['<--\n'] + preamble + ['-->\n'] + lines[first_empty_line:]
    return lines

def fix_static(lines):
    """Fix image links to handle new static path."""
    def fix_static_line(line):
        return line.replace('/static/images', '/images')
    return [fix_static_line(line) for line in lines]


def transform(filepath):
    """Transform a file."""
    with open(filepath, 'r') as f:
        lines = f.readlines()

    try:
        lines = fix_preamble(lines)
        lines = fix_static(lines)
    except Exception:
        logging.exception(f'Error on {filepath}')
        raise

    return lines


if __name__ == "__main__":

    if not os.path.exists(POSTS_DIR):
        os.makedirs(POSTS_DIR)

    for subdir, dirs, files in os.walk(os.path.join(CURRENT_DIR, "../content.bk/old")):
        for file in files:
            filepath = os.path.normpath(os.path.join(subdir, file))

            if filepath.endswith(".md"):
                print(f"Processing {filepath}")

                transformed_lines = transform(filepath)

                new_filepath = os.path.join(POSTS_DIR, file)
                with open(new_filepath, 'w') as f:
                    f.writelines(transformed_lines)
                print(f"Wrote {new_filepath}")




