import re
import numpy as np

def extract_features(line: str):
    clean = line.replace(" ", "")

    return [
        len(clean),                         # length
        sum(c.isdigit() for c in clean),    # digit count
        clean.count("_"),                   # underscore count
        int("1" in clean),                  # contains '1'
        int("_1" in clean),                 # contains _1
        int("1_" in clean),                 # contains 1_
        int(bool(re.search(r"_\s*1\s*_|\_1|1_", clean)))  # regex match
    ]
