#!c:\apps\testcart\myenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'flower==0.9.2','console_scripts','flower'
__requires__ = 'flower==0.9.2'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('flower==0.9.2', 'console_scripts', 'flower')()
    )
