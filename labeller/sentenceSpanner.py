import re
from labeller.constants import NO_REL_DELIMITER, SENTENCE_SPAN

__author__ = 'ozandeniz'


def get_span(with_no_rel_text):
    with_no_rel_sentences = re\
    .compile(NO_REL_DELIMITER + "+")\
    .split(with_no_rel_text)

    for with_no_rel_sentence in with_no_rel_sentences:
        spans = with_no_rel_text.split(with_no_rel_sentence)

        span_left = spans[0]
        span_right = spans[1]

        left = '.'.join(span_left.split('.')[-1 * SENTENCE_SPAN:])
        right = '.'.join(span_right.split('.')[-1 * SENTENCE_SPAN:])

        print('****')
        #print(left.strip('.').strip())
        #print('----')
        #print(right.strip('.').strip())
        #print('----')
        print(with_no_rel_sentence.strip('.').strip())
        print('****\n')