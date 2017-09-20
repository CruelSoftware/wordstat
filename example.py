from wordstat.wordstat import WordStat

word_stat = WordStat()
print(word_stat)
all_words = word_stat.get_all_words()
all_files = word_stat.get_files()
words_stat = word_stat.get_func_words_stat()
