# wordstat
Small python module for simple manipulations with words in files \n
Provides only one class: "WordStat"

## Arguments
    path - path to your projects directory (default = current directory)
    project - project name directory (default = None, specify if needed)
    files_limit - limit of files count to handle with (default = 100)
    extension - extension of files to handle with (default = '.py')
    word_type - Natural Language ToolKit tag (default = 'VB' - verbs, more information:
    [Nltk Tagger](http://www.nltk.org/book/ch05.html)
    encoding - files encoding (default = 'utf-8')
    func_limit - limit of functions to handle with (default = 100)

## Install requirements
```
pip3 install -r ./requirements.txt
```

Sometimes you will need to update nltk modules, just run this in console if needed:
```
>> import nltk
>> nltk.download('all')
```

## Usage

Add wordstat module to your project

## Methods

### get_all_words() - returns list of all words in all specified files
### get_files() - returns list of files in specified folder and subfolders
### get_func_words_stat() - returns list of tuples with current nltk tag with its density
