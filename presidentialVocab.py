import os
import gensim
import spacy
from president_helper import read_file, process_speeches, merge_speeches, get_president_sentences, get_presidents_sentences, most_frequent_words

# get list of all speech files
files = sorted([("/Users/ahmedmoamen/Desktop/ahmed/work/Programming/python/NPL/USA presidential vocab/presidents/"+file) for file in os.listdir("/Users/ahmedmoamen/Desktop/ahmed/work/Programming/python/NPL/USA presidential vocab/presidents") if file[-4:] == '.txt'])
# read each speech file
speeches = [read_file(file) for file in files]
# preprocess each speech
pro_speech = process_speeches(speeches)
# merge speeches
all_speeches = merge_speeches(pro_speech)

def findMostSimilar(speeches, word, limit):
    # create gensim model of all speeches
    model = gensim.models.Word2Vec(speeches, vector_size=96, window=5, min_count=1, workers=2, sg=1)
    # view words similar to input
    close_to_word = model.wv.most_similar(word, topn=int(limit))
    result = list()
    for (word, number) in close_to_word:
        result.append(word)
    return result



"""# get President Roosevelt sentences
roosevelt_sent = get_president_sentences("trump")
print(roosevelt_sent)

# view most frequently used words of Roosevelt
most_freq_ros = most_frequent_words(roosevelt_sent)
#print(most_freq_ros)


# create gensim model for Roosevelt
Ros_emb = gensim.models.Word2Vec(roosevelt_sent, vector_size=96, window=5, min_count=1, workers=2, sg=1)

# view words similar to freedom for Roosevelt
close_to_freedom_ros = Ros_emb.wv.most_similar("", topn=20)
#print(close_to_freedom_ros)
# get sentences of multiple presidents
rushmore_sent = get_presidents_sentences(["washington","jefferson","lincoln","roosevelt"])


# view most frequently used words of presidents
most_freq_rush = most_frequent_words(rushmore_sent)
#print(most_freq_rush)
# create gensim model for the presidents
rush_emb = gensim.models.Word2Vec(rushmore_sent, vector_size=96, window=5, min_count=1, workers=2, sg=1)

# view words similar to freedom for presidents
close_to_freedom_rush = rush_emb.wv.most_similar("freedom", topn=20)
#print(close_to_freedom_rush)


# get sentences of presidents after 9/11
P911_sent = get_presidents_sentences(["trump","obama","bush","clinton"])

# view most frequently used words of presidents
most_freq_911 = most_frequent_words(P911_sent)
print(most_freq_rush)
# create gensim model for the presidents
P911_emb = gensim.models.Word2Vec(P911_sent, vector_size=1000, window=5, min_count=1, workers=2, sg=1)

# view words similar to muslim for presidents
close_to_freedom_911 = P911_emb.wv.most_similar("muslim", topn=20)
print(close_to_freedom_911)"""
