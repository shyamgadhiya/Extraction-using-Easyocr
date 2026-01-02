import regex as re

def extract_target_line(ocr_text):
    lines = ocr_text.splitlines()

    pattern = re.compile(r'.*(_1_|_1\b|\b1_).*')

    matches = []
    for line in lines:
        clean = line.replace(" ", "")
        if pattern.search(clean):
            matches.append(line.strip())

    return matches
