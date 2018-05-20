__author__ = 'ozandeniz'

from bs4 import BeautifulSoup
import re
import codecs

NO_REL_DELIMITER = "~"
SENTENCE_SPAN = 1

with codecs.open('/Users/ozandeniz/Dropbox/COGS/528/COGS_528_Term_Project/for_norel_annotations/all_annotations_combined/00001131_agreed_bir.xml', 'r', encoding='utf8') as connective_file:
    connective = connective_file.read()

with codecs.open('/Users/ozandeniz/Dropbox/COGS/528/COGS_528_Term_Project/odtu_tsb_dagitim_528/metin_dosyalari/00001131.txt', 'r', encoding='utf8') as text_file:
    text = text_file.read()

connectiveInfo = BeautifulSoup(connective, "xml")
relations = connectiveInfo.findAll('Relation')

without_no_rel_text = text
with_no_rel_text = text

for relation in relations:
    first_dot_indexV1 = text[:int(relation.Arg1.BeginOffset.contents[0])].rfind('.')

    last_dot_indexV1 = int(relation.Arg1.EndOffset.contents[0]) + \
                       text[int(relation.Arg1.EndOffset.contents[0]):].find('.')

    first_dot_indexV2 = text[:int(relation.Arg2.BeginOffset.contents[0])].rfind('.')

    last_dot_indexV2 = int(relation.Arg2.EndOffset.contents[0]) + \
                       text[int(relation.Arg2.EndOffset.contents[0]):].find('.')

    first_dot_indexV3 = text[:int(relation.Conn.BeginOffset.contents[0])].rfind('.')

    last_dot_indexV3 = int(relation.Conn.EndOffset.contents[0]) + \
                       text[int(relation.Conn.EndOffset.contents[0]):].find('.')

    with_no_rel_text = with_no_rel_text[:first_dot_indexV1] \
                       + NO_REL_DELIMITER * (last_dot_indexV1 - first_dot_indexV1)\
                       + with_no_rel_text[last_dot_indexV1:]

    with_no_rel_text = with_no_rel_text[:first_dot_indexV2] \
                       + NO_REL_DELIMITER * (last_dot_indexV2 - first_dot_indexV2) \
                       + with_no_rel_text[last_dot_indexV2:]

    with_no_rel_text = with_no_rel_text[:first_dot_indexV3] \
                       + NO_REL_DELIMITER * (last_dot_indexV3 - first_dot_indexV3) \
                       + with_no_rel_text[last_dot_indexV3:]

with_no_rel_sentences = re.compile(NO_REL_DELIMITER + "+").split(with_no_rel_text)

for with_no_rel_sentence in with_no_rel_sentences:
    print(with_no_rel_sentence.strip('.').strip())
    print('XXXX')

