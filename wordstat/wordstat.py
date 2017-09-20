import ast
import os
import collections
import itertools

from nltk import pos_tag


class WordStat():
    def __init__(self, path=None, project=None, files_limit=100, extension='.py', word_type='VB', encoding='utf-8',
                 func_limit=100):
        self.path = self._set_path(path, project)
        self.files_limit = files_limit
        self.extension = extension
        self.word_type = word_type
        self.encoding = encoding
        self.func_limit = func_limit

    def __str__(self):
        return ('List of files in folder and subfilders:\n {}'.format(self.get_files()) + '\n' +
                'List of all words in files:\n {}'.format(self.get_all_words()) + '\n' +
                'Stats of words in functions:\n {}'.format(self.get_func_words_stat()))

    def _set_path(self, path=None, project=None):
        if not path:
            path = os.getcwd()
        if project:
            path = os.path.join(path, project)
        if os.path.isdir(path):
            return path
        else:
            raise NotADirectoryError('{} is not a directory'.format(path))

    def _flat(self, _list):
        """ [(1,2), (3,4)] -> [1, 2, 3, 4]"""
        return list(itertools.chain(*_list))

    def _get_words_from_function_name(self, function_name):
        return [word for word in function_name.split('_') if self._is_word_of_type(word)]

    def _is_word_of_type(self, word):
        if not word:
            return False
        pos_info = pos_tag([word])
        return pos_info[0][1] == self.word_type

    def get_files(self):
        filenames = []
        for (dirpath, dirs, files) in os.walk(self.path, topdown=True):
            files_list = [file for file in files if file.endswith(self.extension)]
            for file in files_list:
                filenames.append(os.path.join(dirpath, file))
        filenames = filenames[:self.files_limit] if self.files_limit else filenames
        return filenames

    def _get_trees(self):
        trees = []
        filenames = self.get_files()
        for filename in filenames:
            with open(os.path.join(filename), 'r', encoding=self.encoding) as attempt_handler:
                main_file_content = attempt_handler.read()
            tree = ast.parse(main_file_content)
            trees.append(tree)
        return trees

    def _get_all_names(self, tree):
        return [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]

    def get_all_words(self):
        trees = self._get_trees()
        function_names = [f for f in self._flat([self._get_all_names(t) for t in trees]) if
                          not (f.startswith('__') and f.endswith('__'))]

        def split_snake_case_name_to_words(name):
            return [n for n in name.split('_') if n]

        return self._flat([split_snake_case_name_to_words(function_name) for function_name in function_names])

    def get_func_words_stat(self):
        trees = self._get_trees()
        fncs = [f for f in self._flat(
            [[node.name.lower() for node in ast.walk(t) if isinstance(node, ast.FunctionDef)] for t in trees])
                if
                not (f.startswith('__') and f.endswith('__'))]
        words = self._flat([self._get_words_from_function_name(function_name) for function_name in fncs])

        return collections.Counter(words).most_common(self.func_limit)
