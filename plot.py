#!/usr/bin/env python
# -*- coding: utf-8 -*-


import gensim
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# configuration
cuv2 = ["nord",
"vest",
"sud",
"est",
"nord-est",  
"nord-vest",
"sud-vest", 
"sud-est"  
]

cuvinte=[
"calculator",
"aplicație",
"computer",
"aparat",
"utilizator",
"modulul",
"logic",
"digital",
"server",
"interfață_grafică",
"utilizatorii",
"sistem_unix",
"utilizatorul",
"sql",
"lcd", 
"fișiere",
"cablurilor",
"design",
"gnu",
"ecran",
"ssl",
]

def draw_words(model, words, pca=False, alternate=True, arrows=True, x1=3, x2=3, y1=3, y2=3, title=''):
    # get vectors for given words from model
    vectors = [model[word] for word in words]

    if pca:
        pca = PCA(n_components=2, whiten=True)
        vectors2d = pca.fit(vectors).transform(vectors)
    else:
        tsne = TSNE(n_components=2, random_state=0)
        vectors2d = tsne.fit_transform(vectors)

    # draw image
    plt.figure(figsize=(6,6))
    if pca:
        plt.axis([x1, x2, y1, y2])

    first = True # color alternation to divide given groups
    for point, word in zip(vectors2d , words):
        # plot points
        plt.scatter(point[0], point[1], c='r' if first else 'g')
        # plot word annotations
        plt.annotate(
            word, 
            xy = (point[0], point[1]),
            xytext = (-7, -6) if first else (7, -6),
            textcoords = 'offset points',
            ha = 'right' if first else 'left',
            va = 'bottom',
            size = "x-large"
        )
        first = not first if alternate else first

    # draw arrows
    if arrows:
        for i in xrange(0, len(words)-1, 2):
            a = vectors2d[i][0] + 0.04
            b = vectors2d[i][1]
            c = vectors2d[i+1][0] - 0.04
            d = vectors2d[i+1][1]
            plt.arrow(a, b, c-a, d-b,
                shape='full',
                lw=0.1,
                edgecolor='#bbbbbb',
                facecolor='#bbbbbb',
                length_includes_head=True,
                head_width=0.08,
                width=0.01
            )

    # draw diagram title
    if title:
        plt.title(title)

    plt.tight_layout()
    plt.show()


# get trained model
#model.seek(0)
#model = gensim.models.Word2Vec.load(r'C:\Users\BSSoper\Downloads\out_v4.bin', binary=True)
model = gensim.models.KeyedVectors.load_word2vec_format(r'C:\Users\BSSoper\Downloads\out_v4.bin', binary=True)
# draw pca plots
#model.wv.vocab[2:10]
draw_words(model, cuvinte , True, True, False, -3, 3, -2, 2, r't1')
#draw_words(model, ["iran","irak","copac"], True, False, False, -30, 30, -2, 2.2, r't2')
# draw_words(model, language, True, True, True, -3, 3, -2, 1.7, r't3')
