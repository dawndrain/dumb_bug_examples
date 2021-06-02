from whitespace_buggy import get_leading_whitespace


def test_whitespace():
    assert get_leading_whitespace('    qwer') == '    '
    assert get_leading_whitespace('\t asdf  ') == '\t '