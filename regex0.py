#!/usr/bin/env python3

import re

line = 'git version control is aaaaawwwaaaesome !!'

# after patched same
result = re.findall(r"([a*])",line)



print('all matches of the pattern : ',result)
