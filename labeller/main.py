import sys
from labeller.extractor import extract
from labeller.sentenceSpanner import get_span
from labeller.xmlReader import read_annotation, read_text

__author__ = 'ozandeniz'


def main(argv):
    annotation_file_path = '/Users/ozandeniz/Dropbox/COGS/528/COGS_528_Term_Project/for_norel_annotations/all_annotations_combined/00001131_agreed_bir.xml'
    text_file_path = '/Users/ozandeniz/Dropbox/COGS/528/COGS_528_Term_Project/odtu_tsb_dagitim_528/metin_dosyalari/00001131.txt'

    annotation = read_annotation(annotation_file_path)
    text = read_text(text_file_path)

    with_no_rel_text = extract(text, annotation)

    get_span(with_no_rel_text)
    pass

if __name__ == "__main__":
    main(sys.argv)