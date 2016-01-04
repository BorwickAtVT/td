#!python
from glob import glob
import re
import sys

SEEN_REQUIREMENTS = set()

PIP_EQUALS_STRING = re.compile("""
^
    ([^=]+)   # not equals sign characters in 1
    ==
    (.*)      # version in 2
""",
                               re.VERBOSE)

def add_requirements(fh):
    for line in fh:
        equals_match = PIP_EQUALS_STRING.match(line)
        if equals_match:
            paren_string = '{} ({})'.format(equals_match.group(1),
                                            equals_match.group(2))
            SEEN_REQUIREMENTS.add(paren_string)
        else:
            SEEN_REQUIREMENTS.add(line.strip())


if __name__=='__main__':
    for req in glob('*.txt'):
        add_requirements(open(req))

    for line in sys.stdin:
        line = line.strip()
        if line not in SEEN_REQUIREMENTS:
            print line
