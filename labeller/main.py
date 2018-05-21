from labeller.config import annotation_file_path, text_file_path
from labeller.extractor import extract
from labeller.marker import mark_no_rel
from labeller.sentence_spanner import get_span
from labeller.xml_reader import read_annotation, read_text

__author__ = 'ozandeniz'


def main():

    annotation = read_annotation()
    text = read_text(text_file_path)

    with_no_rel_text = extract(text, annotation)
    no_rel_with_span = get_span(with_no_rel_text, text)

    mark_no_rel(text, no_rel_with_span)
    pass

if __name__ == "__main__":
    main()
