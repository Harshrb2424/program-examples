from nltk.util import ngrams
from nltk.tokenize import word_tokenize

def generate_ngrams(text, n):
    tokens = word_tokenize(text)
    n_grams = list(ngrams(tokens, n))
    return [" ".join(gram) for gram in n_grams]
# Sample Input
text = "The quick brown fox jumps over the lazy dog."
bigrams = generate_ngrams(text, 2)
trigrams = generate_ngrams(text, 3)
print("Bigrams:", bigrams)
print("Trigrams:", trigrams)

# Output
# PS D:\Github\program-examples> python -u "d:\Github\program-examples\resources\NLP\7b.py"
# Bigrams: ['The quick', 'quick brown', 'brown fox', 'fox jumps', 'jumps over', 'over the', 'the lazy', 'lazy dog', 'dog .']
# Trigrams: ['The quick brown', 'quick brown fox', 'brown fox jumps', 'fox jumps over', 'jumps over the', 'over the lazy', 'the lazy dog', 'lazy dog .'