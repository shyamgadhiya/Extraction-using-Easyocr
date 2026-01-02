import regex as re

def extract_target_line(ocr_text):
    lines = ocr_text.splitlines()

    pattern = re.compile(
        r'([A-Z0-9]+[_\-]?[1I|l][_A-Z0-9]+)', re.IGNORECASE
    )

    matches = []
    for line in lines:
        clean = line.replace(" ", "")
        if re.search(r'_1_|_1\b|\b1_', clean) or pattern.search(clean):
            matches.append(line.strip())

    return list(set(matches))
