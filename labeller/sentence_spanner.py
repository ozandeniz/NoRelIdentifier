import re
from labeller.constants import NO_REL_DELIMITER, SENTENCE_SPAN

__author__ = 'ozandeniz'


def get_span(with_no_rel_text, text):

    no_rel_sentences = re.compile(NO_REL_DELIMITER + r"+").split(with_no_rel_text)

    no_rel_with_span = []

    for no_rel_sentence in no_rel_sentences:
        spans = text.split(no_rel_sentence)

        span_left = spans[0]
        span_right = spans[1]

        left = '.'.join(span_left.split('.')[-1 * SENTENCE_SPAN:])
        right = '.'.join(span_right.split('.')[SENTENCE_SPAN:])

        no_rel_with_span.append([no_rel_sentence, left, right])
        '''
        For debugging purpose

        print('****')
        print('---span left start---')
        print(left.strip('.').strip())
        print('---span left end---')
        print('--- no rel start')
        print(no_rel_sentence.strip('.').strip())
        print('--- no rel end')
        print('----span right start---')
        print(right.strip('.').strip())
        print('----span right end---')
        print('****\n')
        '''

    return no_rel_with_span
