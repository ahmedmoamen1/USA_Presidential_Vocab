# USA_Presidential_Vocab

##Getting Started:
Must Install the following Libraries on python:
  - Flask
  - Selenuim
  - Genism
  - NLTK
  - Collections
  - Spacy

## Presidential Vocabulary

### presidentialVocab.py

A Python script that finds the most similar words to a given word based on all the speeches made by U.S. presidents. It preprocesses speeches using the `process_speeches()` and `merge_speeches()` functions from `president_helper.py`. The `findMostSimilar()` function uses the `gensim` library to create a Word2Vec model of the speeches and returns a list of the most similar words to the input word.

### president_helper.py

A module with helper functions used by `presidentialVocab.py`. Functions include `read_file()`, `process_speeches()`, `merge_speeches()`, `get_president_sentences()`, `get_presidents_sentences()`, and `most_frequent_words()`.

### GatherData.py

A Python script that uses Selenium to scrape transcripts of speeches by US presidents from the Miller Center website. It appends the text to separate files in directories named after the corresponding president. The data will be returned in the presidents file.

### webpage.py

A Flask web application that allows users to search for the most similar words to a given word in the speeches of selected U.S. presidents. It calls functions from `presidentialVocab.py` and `president_helper.py` to find and display the results. The `run()` function from `GatherData.py` is called to gather data required by the Flask app (presidents name).

**Note:** If `run()` takes a long time to execute, it may delay the startup of the Flask app. Consider running it in a separate process or thread or finding a way to pre-cache the data it generates.
