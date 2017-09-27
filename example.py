# -*- coding: UTF-8 -*-

import argparse

from wordstat.wordstat import WordStat


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', type=str)
    parser.add_argument('-project', type=str)
    parser.add_argument('-files_limit', type=int)
    parser.add_argument('-func_limit', type=int)
    parser.add_argument('-extension', type=str)
    parser.add_argument('-encoding', type=str)
    parser.add_argument('-word_type', type=str, choices=['VB', 'NN', 'CC', 'RB', 'IN', 'JJ'])

    return parser

if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()
    params = namespace.__dict__ if namespace else {}
    clear_params = {key:value for key, value in params.items() if value is not None}
    wordstat = WordStat(**clear_params)
    print(wordstat)

