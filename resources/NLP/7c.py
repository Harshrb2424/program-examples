from collections import Counter
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

def laplace_smoothing(unigrams, bigrams, vocab_size):
    smoothed_probs = {}
    for bigram in bigrams:
        count_bigram= bigrams[bigram]
        count_unigram = unigrams[bigram[0]]
        prob = (count_bigram + 1) / (count_unigram + vocab_size)
        smoothed_probs[bigram] = prob
    return smoothed_probs
# Sample Input
text = "The cat sat on the mat. The dog sat on the rug."
tokens = word_tokenize(text)
# Count unigrams and bigrams
unigram_counts = Counter(tokens)
bigram_counts = Counter(ngrams(tokens, 2))
vocab_size = len(unigram_counts)
# Apply Laplace Smoothing
smoothed_bigram_probs = laplace_smoothing (unigram_counts,bigram_counts, vocab_size)
print("Smoothed Bigram Probabilities:")
for bigram, prob in smoothed_bigram_probs.items():
    print(f"P({bigram[1]} | {bigram[0]}) = {prob:.4f}")


# Output
# PS D:\Github\program-examples> python -u "d:\Github\program-examples\resources\NLP\7c.py"
# Smoothed Bigram Probabilities:
# P(cat | The) = 0.1818
# P(sat | cat) = 0.2000
# P(on | sat) = 0.2727
# P(the | on) = 0.2727
# P(mat | the) = 0.1818
# P(. | mat) = 0.2000
# P(The | .) = 0.1818
# P(dog | The) = 0.1818
# P(sat | dog) = 0.2000
# P(rug | the) = 0.1818
# P(. | rug) = 0.2000