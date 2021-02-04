#!/usr/bin/env python

from collections import defaultdict
import csv
import pprint
import pdb

import nltk


# What is NN, JJ? See:
# https://en.wikipedia.org/wiki/Brown_Corpus#Part-of-speech_tags_used
ADJECTIVE = ['JJ']
REVIEW_COLUMN = 4


def _load_text():
    text = ''
    with open('Recommendations.csv') as f:
        reader = csv.reader(f)
        # Skip the header row.
        next(reader, None)
        for line in reader:
            text = f'{text} {line[REVIEW_COLUMN]}'
    return text


def _find_top_3_words_per_tag(words_tags):
    result = defaultdict(list)
    for v, k in words_tags:
        result[k].append(v)
    for k in result.keys():
        fdist = nltk.probability.FreqDist(result[k])
        result[k] = fdist.most_common(3)
    return result


def main():
    """Print top 3 adjectives from LinkedIn recommendations."""
    text = _load_text()
    tokens = nltk.tokenize.word_tokenize(text)
    adjectives = [x for x, tag in nltk.pos_tag(tokens) if tag in ADJECTIVE]
    fdist = nltk.probability.FreqDist(adjectives)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint([x for x, _ in fdist.most_common(3)])


if __name__ == '__main__':
    main()
