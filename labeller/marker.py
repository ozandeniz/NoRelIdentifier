# coding=utf-8
import re
from labeller.constants import NO_REL_DELIMITER

__author__ = 'ozandeniz'
'''
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


def mark_no_rel(with_no_rel_text):
    with_no_rel_sentences = re.compile(NO_REL_DELIMITER + r"+").split(with_no_rel_text)