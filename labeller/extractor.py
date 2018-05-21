from labeller.constants import NO_REL_DELIMITER

__author__ = 'ozandeniz'


def extract(text, relations):
    with_no_rel_text = text

    for relation in relations:
        first_dot_index_arg1 = text[:int(relation.Arg1.BeginOffset.contents[0])].rfind('.')

        last_dot_index_arg1 = int(relation.Arg1.EndOffset.contents[0]) + \
                           text[int(relation.Arg1.EndOffset.contents[0]):].find('.')

        first_dot_index_arg2 = text[:int(relation.Arg2.BeginOffset.contents[0])].rfind('.')

        last_dot_index_arg2 = int(relation.Arg2.EndOffset.contents[0]) + \
                           text[int(relation.Arg2.EndOffset.contents[0]):].find('.')

        first_dot_index_conn = text[:int(relation.Conn.BeginOffset.contents[0])].rfind('.')

        last_dot_index_conn = int(relation.Conn.EndOffset.contents[0]) + \
                           text[int(relation.Conn.EndOffset.contents[0]):].find('.')

        with_no_rel_text = with_no_rel_text[:first_dot_index_arg1] \
                           + NO_REL_DELIMITER * (last_dot_index_arg1 - first_dot_index_arg1)\
                           + with_no_rel_text[last_dot_index_arg1:]

        with_no_rel_text = with_no_rel_text[:first_dot_index_arg2] \
                           + NO_REL_DELIMITER * (last_dot_index_arg2 - first_dot_index_arg2) \
                           + with_no_rel_text[last_dot_index_arg2:]

        with_no_rel_text = with_no_rel_text[:first_dot_index_conn] \
                           + NO_REL_DELIMITER * (last_dot_index_conn - first_dot_index_conn) \
                           + with_no_rel_text[last_dot_index_conn:]

    return with_no_rel_text
