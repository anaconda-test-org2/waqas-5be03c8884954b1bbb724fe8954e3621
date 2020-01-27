"""
This file is just a simple wrapper to allow intake-server to accept
anaconda-project specific flags. This isn't needed on a local machine,
only on Anaconda Enterprise.
"""

from __future__ import absolute_import, division, unicode_literals

import sys

def transform_cmds(argv):
    """
    Allows usage with anaconda-project by remapping the argv list provided
    into arguments accepted by intake.
    """
    replacements = {'--anaconda-project-port': '--port'}
    transformed = []
    skip = False
    for arg in argv:
        if skip:
            skip = False
            continue
        if arg in replacements.keys():
            transformed.append(replacements[arg])
        elif arg == '--anaconda-project-iframe-hosts':
            skip = True
            continue
        elif arg.startswith('--anaconda-project'):
            continue
        else:
            transformed.append(arg)
    return transformed

def main():
    from intake.cli.server.__main__ import main as intake_entry_point
    sys.argv = transform_cmds(sys.argv)
    intake_entry_point()

if __name__ == "__main__":
    main()
