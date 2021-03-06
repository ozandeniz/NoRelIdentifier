from labeller.constants import SENTENCE_END_MARKINGS
from labeller.extractor import extract
from labeller.marker import mark_no_rel
from labeller.sentence_spanner import get_span
from labeller.xml_reader import read_annotation, read_text
from preprocess.end_marker import convert_to_dot

__author__ = 'ozandeniz'


def main():

    annotation = read_annotation()
    text = read_text()

    text = convert_to_dot(text)

    with_no_rel_text = extract(text, annotation)
    no_rel_with_span = get_span(with_no_rel_text, text)

    mark_no_rel(text, no_rel_with_span)
    pass

if __name__ == "__main__":
    main()
