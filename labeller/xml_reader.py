from bs4 import BeautifulSoup
import codecs
from labeller.config import annotation_file_path

__author__ = 'ozandeniz'


def read_annotation():

    with codecs.open(annotation_file_path, 'r', encoding='utf8') as connective_file:
        connective = connective_file.read()

    connective_info = BeautifulSoup(connective, "xml")
    return connective_info.findAll('Relation')


def read_text(file_path):

    with codecs.open(file_path, 'r', encoding='utf8') as text_file:
        text = text_file.read()

    return text
