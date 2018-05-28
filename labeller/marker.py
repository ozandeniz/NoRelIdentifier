# coding=utf-8
import codecs
from bs4 import BeautifulSoup, Tag
from labeller.config import out_file_path, annotation_file_path

__author__ = 'ozandeniz'
'''
Sample marking style for no rel

<Relation note="" sense="" type="NOREL">
    <Conn>
        <Span>
            <Text>Halil</Text>
            <BeginOffset>10700</BeginOffset>
            <EndOffset>10705</EndOffset>
        </Span>
    </Conn>
    <Mod/>
    <Arg1>
        <Span>
            <Text>Başka kimse olmadığından iki kadının da yüzü açıktı.</Text>
            <BeginOffset>10647</BeginOffset>
            <EndOffset>10699</EndOffset>
        </Span>
    </Arg1>
    <Arg2>
        <Span>
            <Text> onları korkutacağı yere geldiğinde donakaldı</Text>
            <BeginOffset>10705</BeginOffset>
            <EndOffset>10750</EndOffset>
        </Span>
    </Arg2>
    <Supp1/>
    <Supp2/>
    <Shared/>
    <Supp_Shared/>
</Relation>
'''


def mark_no_rel(text, no_rel_list_with_span):
    with codecs.open(annotation_file_path, 'r', encoding='utf8') as connective_file:
        connective = connective_file.read()

    connective_info = BeautifulSoup(connective, "xml")

    for no_rel_with_span in no_rel_list_with_span:
        start_index = text.find(no_rel_with_span[0])
        end_index = start_index + len(no_rel_with_span[0])

        conn_text = Tag(name='Text')
        conn_text.string = no_rel_with_span[0][0:1]

        conn_begin = Tag(name='BeginOffset')
        conn_begin.string = str(start_index)

        conn_end = Tag(name='EndOffset')
        conn_end.string = str(start_index + 1)

        arg1_text = Tag(name='Text')
        arg1_text.string = no_rel_with_span[0]

        arg1_begin = Tag(name='BeginOffset')
        arg1_begin.string = str(start_index)

        arg1_end = Tag(name='EndOffset')
        arg1_end.string = str(end_index)

        arg2_text = Tag(name='Text')
        arg2_text.string = no_rel_with_span[0]

        arg2_begin = Tag(name='BeginOffset')
        arg2_begin.string = str(start_index)

        arg2_end = Tag(name='EndOffset')
        arg2_end.string = str(end_index)

        rel = Tag(name='Relation', attrs={'note': '', 'sense': '', 'type': 'NOREL'})

        conn = Tag(name='Conn')
        span = Tag(name='Span')
        span.append(conn_text)
        span.append(conn_begin)
        span.append(conn_end)
        conn.append(span)
        rel.append(conn)

        mod = Tag(name='Mod')
        rel.append(mod)

        arg1 = Tag(name='Arg1')
        span = Tag(name='Span')
        span.append(arg1_text)
        span.append(arg1_begin)
        span.append(arg1_end)
        arg1.append(span)
        rel.append(arg1)

        arg2 = Tag(name='Arg2')
        span = Tag(name='Span')
        span.append(arg2_text)
        span.append(arg2_begin)
        span.append(arg2_end)
        arg2.append(span)
        rel.append(arg2)

        connective_info.Document.append(rel)

    with open(out_file_path, "w") as f:
        f.write(str(connective_info))
        f.close()
