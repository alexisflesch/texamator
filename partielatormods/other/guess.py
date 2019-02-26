# -*- coding: utf-8 -*-
import re
import codecs

def get_tags_header(d):
    e = r'\\begin[{][^}]*}'
    a = ''
    try:
        f = codecs.open(d,"r","utf-8")
    except:
        return [],""
    for i in f:
        a+= i
    liste = re.findall(e,a)
    exclude = ["\\begin{document}", \
               "\\begin{array}", \
               "\\begin{enumerate}", \
               "\\begin{tabular}", \
               "\\begin{figure}", \
               "\\begin{itemize}", \
               "\\begin{verbatim}", \
               "\\begin{flushleft}", \
               "\\begin{flushright}", \
               "\\begin{center}", \
               "\\begin{equation}", \
               "\\begin{equation*}", \
               "\\begin{array}", \
               "\\begin{array*}", \
               "\\begin{align}", \
               "\\begin{align*}", \
               "\\begin{eqnarray}", \
               "\\begin{eqnarray*}", \
               "\\begin{displaymath}", \
               "\\begin{multline}", \
               "\\begin{multline*}", \
               "\\begin{description}", \
               "\\begin{gather}", \
               "\\begin{gather*}", \
               "\\begin{pspicture}", \
               "\\begin{proof}", \
               "\\begin{multicols}", \
               "\\begin{matrix}", \
               "\\begin{smallmatrix}",\
               "\\begin{minipage}",\
               "\\begin{cases}" ]
    tags = []
    for i in liste:
        if i[7:-1] not in tags and i not in exclude:
            tags.append(i[7:-1])
    m = re.search(r'\\begin\{document\}',a)
    if m:
        header = a[:m.start()]
    else:
        header = ''
    return tags, header



if __name__ == "__main__":
    tags, header = get_tags_header("/home/snouffy/Documents/enseignement/ro/poly/ro.tex")
    print(tags)
    print(header)