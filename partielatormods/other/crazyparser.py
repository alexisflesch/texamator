# -*- coding: utf-8 -*-

import os


def contientExos(root,fichier_sans_root,balises1,balises2):
    """If a file is a .tex and contains exercise(s), then return the exercise(s)"""
    exos = []
    fichier = os.path.join(root,fichier_sans_root)
    if fichier[-4:].lower() == ".tex":    
        try:
            f = open(fichier,"r")
            hop = f.readlines()
            f.close()
        except:
            print("Couldn't open" + fichier)
            return []
        enregistrer = False
        for ligne in hop:
            for balise in balises1:
                if balise in ligne.split("%")[0]:
                    enregistrer = True
                    exos.append("")
            if enregistrer:
                if "\\includegraphics" in ligne:
                    a = ligne.split('{')[1].split('}')[0]
                    b = os.path.split(a)[0]
                    try:
                        t = os.listdir(b)
                    except:
                        t = []
                    if a not in t:
                            ligne = ligne.replace(a,os.path.join(root,a))
                exos[-1] += ligne
            for balise in balises2:
                if balise in ligne.split("%")[0]:
                    enregistrer = False
    return exos


def crazyparser(directory,tags):
    """Creates a tree similar to os.walk() but with interesting folders/files only.
    A folder is interesting if contientExos doesn't return an empty list"""
    balises1 = tags[0]
    balises2 = tags[1]
    treeTex = []
    nb_ex = 0
    for root,dirs,files in os.walk(directory,topdown=False):

        dossiers_a_ajouter = []
        fichiers_a_ajouter = []

        #Look for exercises in the files
        for fichier_sans_root in files:
            exos = contientExos(root,fichier_sans_root,balises1,balises2)
            if exos:
                fichiers_a_ajouter.append((fichier_sans_root , exos))
                nb_ex += len(exos)

        #Look for folders containing "interesting" sub-folders
        for dossier in dirs:
            for a in treeTex:
                if os.path.join(root,dossier) == a[0]:
                    dossiers_a_ajouter.append(dossier)

        #If exercises or intersting sub-folders where found , give them
        if dossiers_a_ajouter or fichiers_a_ajouter:
            treeTex.append((root,dossiers_a_ajouter,fichiers_a_ajouter))

    treeTex.reverse()
    return nb_ex , treeTex

#Little function to enhance the search functionnality :
#it will replace "é" with "\'e" etc...
def power_rangers(string):
    a = string.replace("é","\\'e").replace("è","\\`e").replace("ê","\\^e")
    a = a.replace("à","\\`a").replace("â","\\^a")
    a = a.replace("ù","\\`u")
    a = a.replace("ô","\\^o")
    a = a.replace("ç","\\c{c}")
    return a


def smart_cut(search):
    """"transforms a search string into a list of strings dealing with quotes. For example :
    '"hello world" !' will become ['hello world','!'] """
    b = search.split(" ")
    g = False #True if a quote is detected
    c = []
    for i in b:
        if i == '':
            continue
        if g and c:
            c[-1] += ' ' + i
            c[-1] = c[-1].replace('"','')
        else:
            c.append(i)
            c[-1] = c[-1].replace('"','')
        if i[0] == '"':
            g = True
        elif len(i)>1 and i[0] == '-' and i[1] == '"':
            g = True
        if i[-1] == '"':
            g = False
    return c



if __name__ == "__main__":
    a = 'matrices -'
    print(smart_cut(a))
