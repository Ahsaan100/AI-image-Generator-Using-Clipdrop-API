from collections import Counter
import math
import os
import random
import re
import sys
s = input("Enter a word: ")
result = Counter(sorted(s)).most_common(3)
for i,j in result:
    print(i,j)