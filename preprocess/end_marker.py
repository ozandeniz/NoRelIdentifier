from labeller.constants import SENTENCE_END_MARKINGS

__author__ = 'ozandeniz'


def convert_to_dot(text):
    for end_marker in SENTENCE_END_MARKINGS:
        text = text.replace(end_marker, '.')

    return text
