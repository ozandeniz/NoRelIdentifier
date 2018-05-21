from labeller.config import annotation_file_path, text_file_path
from labeller.extractor import extract
from labeller.sentence_spanner import get_span
from labeller.xml_reader import read_annotation, read_text

__author__ = 'ozandeniz'


def main():

    annotation = read_annotation(annotation_file_path)
    text = read_text(text_file_path)

    with_no_rel_text = extract(text, annotation)

    get_span(with_no_rel_text, text)
    pass

if __name__ == "__main__":
    main()
