from src.text_extraction import extract_target_line

def test_pattern():
    text = """
    ABC123
    163233702292313922_1_lWV
    XYZ456
    """
    result = extract_target_line(text)
    assert len(result) == 1
