
from filtering import filter_url_strings, filter_url_lists, filter_values

value_s = ['\n Guido Santillan \n', '\n Vinicio Arias']
value_f = ['\n      ', 'Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor', '\n      \n      \n        ', 'Hardcover', '\n\n        \n        \n        \n        \n\n        ', '\n        \n\n        \n          \n            \n            \n              \n            \n          \n        \n\n        \n          ', '– January 23, 2018', '\n        \n      \n      \n      \n    ']
value_l = ['\n Books', '\n History \n', ' \n American \n History \n']

value = "['\n      ', 'Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor', '\n      \n      \n        ', 'Hardcover', '\n\n        \n        \n        \n        \n\n        ', '\n        \n\n        \n          \n            \n            \n              \n            \n          \n        \n\n        \n          ', '– January 23, 2018', '\n        \n      \n      \n      \n    ']"


def test_filter_url_strings():
    assert filter_url_strings('\n \n This is a \n test') == 'This is a test'

def test_filter_url_lists():
    assert filter_url_lists(['\n \n First  item\n \n', '\n Second  item\n', ' Third item ']) == ['First item', 'Second item', 'Third item']

def test_filter_values_s():
    assert filter_values(value_s, 's') == 'Guido Santillan - Vinicio Arias'

def test_filter_values_f():
    assert filter_values(value_f, 'f') == 'Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor'

def test_filter_values_l():
    assert filter_values(value_l, 'l') == ['Books', 'History', 'American History']
