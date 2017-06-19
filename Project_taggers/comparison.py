import treetaggerwrapper
import string

punkt = string.punctuation+'»«-'

t = treetaggerwrapper.TreeTagger(TAGLANG=u'ru', TAGDIR='/Users/Valeriya/Downloads')
file = open('/Users/Valeriya/Downloads/test_good.txt', 'r')
f = file.read()
# print(f)
# analysis = t.tag_text(f, tagblanks=False)

analyzed = []
# for a in analysis:
#     if a.split()[0] in punkt or a.split()[0].isdigit():
#         analyzed.append([a.split()[0], a.split()[0]]) #tag, word
#     else:
#         analyzed.append([a.split()[1], a.split()[0]])


f = open('/Users/Valeriya/Downloads/TestSet_2/GoldStandard.txt', 'r')

file = f.readlines()

def for_nouns(raw): # принимает на вход ВСЮ строку файла
    tags = raw.split()[3].split(',')
    result = '' # звездочка, если тега нет
    result+='N*'

    if 'f' in tags:       #gen
        result+='f'
    elif 'm' in tags:       #gen
        result+='m'
    elif 'n' in tags:       #gen
        result+='n'
    else:
        result+='*'

    if 'sg' in tags:  #num
        result+='s'
    elif 'pl' in tags:
        result+='p'
    else:
        result+='*'
    #case
    f = False
    for i in ['nom', 'gen', 'dat', 'acc', 'ins', 'abl', 'part', 'loc', 'voc']:
        if i in tags:
            result += i[0]
            f = True
    if f is False:
        result += '*'

    result+='**'
    return result

def for_adj(raw):
    tags = raw.split()[3].split(',')
    result = ''
    result+='A**'

    if 'f' in tags:       #gen
        result+='f'
    elif 'm' in tags:       #gen
        result+='m'
    elif 'n' in tags:       #gen
        result+='n'
    else:
        result+='*'


    if 'sg' in tags:  # num
        result += 's'
    elif 'pl' in tags:
        result += 'p'
    else:
        result += '*'
    # case
    f = False
    for i in ['nom', 'gen', 'dat', 'acc', 'ins', 'abl', 'part', 'loc', 'voc']:
        if i in tags:
            result += i[0]
            f = True
    if f is False:
        result += '*'

    result+= '*'
    return result

def for_verbs(raw):
    tags = raw.split()[3].split(',')
    result = ''
    result+='V*'
    if 'partcp' in tags:
        result+='p'
    else:
        result+='*'

    if 'pres' in tags: #tense
        result+='p'
    elif 'past' in tags:
        result+='s'
    else:
        result+='*'

    if any(['1' in t for t in tags]):
        result+='1'
    elif any(['2' in t for t in tags]):
        result+='2'
    elif any(['3' in t for t in tags]):
        result+='3'
    else:
        result+='*'

    if 'sg' in tags:  #num
        result+='s'
    elif 'pl' in tags:
        result+='p'
    else:
        result+='*'

    if 'f' in tags:       #gen
        result+='f'
    elif 'm' in tags:       #gen
        result+='m'
    elif 'n' in tags:       #gen
        result+='n'
    else:
        result+='*'

    if 'act' in tags: #voice
        result+= 'a'
    elif 'pass' in tags:
        result+='p'
    else:
        result+='*'

    result+='**'

    #case
    f = False
    for i in ['nom','gen','dat','acc','ins','abl','part','loc','voc']:
        if i in tags:
            result+=i[0]
            f = True
    if f is False:
        result+='*'

    return result

def for_all_prons(raw):
    if len(raw.split()) == 4:
        tags = raw.split()[3].split(',')
    elif len(raw.split()) == 3:
        tags = raw.split()[2].split(',')

    result = ''
    result+='P*'
    if any(['1' in t for t in tags]):
        result+='1'
    elif any(['2' in t for t in tags]):
        result+='2'
    elif any(['3' in t for t in tags]):
        result+='3'
    else:
        result+='*'

    if 'f' in tags:       #gen
        result+='f'
    elif 'm' in tags:       #gen
        result+='m'
    elif 'n' in tags:       #gen
        result+='n'
    else:
        result+='*'

    if 'sg' in tags:  #num
        result+='s'
    elif 'pl' in tags:
        result+='p'
    else:
        result+='*'


    # case
    f = False
    for i in ['nom','gen','dat','acc','ins','abl','part','loc','voc']:
        if i in tags:
            result+=i[0]
            f = True
    if f is False:
        result+='*'


    #syntactic type
    if 'ADVPRO' in tags:
        result+='r'
    elif 'APRO' in tags:
        result+='a'
    elif 'SPRO' in tags:
        result+='n'

    result+='*'

    return result

def for_adverbs(raw):
    if len(raw.split()) == 4:
        result ='R'
        if 'comp' in raw.split()[3]:
            result+='c'
        elif 'supr' in raw.split()[3]:
            result+='s'
        else:
            result+='*'
    else:
        result = 'R*'

    return result

def for_adpos(raw):
    result = 'S***'
    return result

def for_conj(raw):

    result = 'C****'
    return result

def for_num(raw):
    tags = raw.split()[3].split(',')
    result = 'M*'
    # gender
    if 'f' in tags:       #gen
        result+='f'
    elif 'm' in tags:       #gen
        result+='m'
    elif 'n' in tags:       #gen
        result+='n'
    else:
        result+='*'

    if 'sg' in tags:  #num
        result+='s'
    elif 'pl' in tags:
        result+='p'
    else:
        result+='*'

    # case
    f = False
    for i in ['nom', 'gen', 'dat', 'acc', 'ins', 'abl', 'part', 'loc', 'voc']:
        if i in tags:
            result += i[0]
            f = True
    if f is False:
        result += '*'

    result+='**'

    return result

tags_from_gs = []


lemmata_gold = []
lemmata_tree = []


for i in range(1, len(file)):
    raw = file[i]

    tags = raw.split()
    if len(tags) > 1:
        lemma = raw.split()[1]
        lemmata_gold.append(lemma)
    else:
        lemmata_gold.append('')

    word = raw.split()[0]
    latin = string.ascii_letters
    ana_treetag = t.tag_text(word, tagblanks=False)
    if ana_treetag[0].split()[0] in punkt or ana_treetag[0].split()[0].isdigit():
        analyzed.append((ana_treetag[0].split()[0], ana_treetag[0].split()))       #tag, word
        lemma_tree = ana_treetag[0].split()[0]
    else:
        analyzed.append([ana_treetag[0].split()[1], ana_treetag[0].split()[0]])
        lemma_tree = ana_treetag[0].split()[2]

    lemmata_tree.append(lemma_tree)
    if any(char in latin for char in word):
        tags_from_gs.append('-')
        continue

    if len(raw.split()) == 4:
        pos = raw.split()[2]
        if pos == 'S':
            result = for_nouns(raw)
            tags_from_gs.append(result)
        elif pos == 'A':
            result = for_adj(raw)
            tags_from_gs.append(result)
        elif pos =='V':
            result = for_verbs(raw)
            tags_from_gs.append(result)
        elif pos == 'ADVPRO' or pos == 'SPRO' or pos == 'APRO':
            result = for_all_prons(raw)
            tags_from_gs.append(result)
        elif pos == 'ADV':
            result = for_adverbs(raw)
            tags_from_gs.append(result)
        elif pos == 'NUM' or pos == 'ANUM':
            result = for_num(raw)
            tags_from_gs.append(result)
        else:
            print(raw)
            tags_from_gs.append(raw.split()[0])

    elif len(raw.split()) == 3:
        pos = raw.split()[2]
        if pos == 'CONJ':
            result = for_conj(raw)
            tags_from_gs.append(result)
        elif pos == 'PR':
            result = for_adpos(raw)
            tags_from_gs.append(result)
        elif pos == 'ADVPRO' or pos == 'SPRO' or pos == 'APRO':
            result = for_all_prons(raw)
            tags_from_gs.append(result)
        elif pos == 'ADV':
            result = for_adverbs(raw)
            tags_from_gs.append(result)
        else:
            tags_from_gs.append(raw.split()[0])
    else:
        tags_from_gs.append(raw.split()[0])




corr = 0
corr_pos = 0
corr_lemma = 0
for tag1, tag2, lemma_gold, lemma_tree in zip(tags_from_gs, analyzed, lemmata_gold, lemmata_tree):
    flag = False
    if tag1[0] == tag2[0][0]:
        corr_pos += 1
    if lemma_gold == lemma_tree:
        corr_lemma += 1
    if any([letter1 != letter2 for letter1, letter2 in zip(tag1,tag2[0]) if letter1 != '*']):
        flag=True

    if flag==True:
        print(tag1, tag2[1], tag2)
    else:
        corr+=1


# print(len(tags_from_gs), len(analyzed))
print(corr / len(tags_from_gs)) #accuracy
print(corr_pos / len(tags_from_gs)) #accuracy по частям речи
print(corr_lemma / len(tags_from_gs)) #лексическая точность