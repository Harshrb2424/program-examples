import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
nltk.download ('punkt')
nltk.download ('averaged_perceptron_tagger')
nltk.download ('wordnet')
def get_wordnet_pos(word):
    """Map POS tag to first character for WordNetLemmatizer"""
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ, "N": wordnet.NOUN, "V": wordnet.VERB,"R": wordnet.ADV}
    return tag_dict.get(tag, wordnet.NOUN)
def morphological_analysis(text):
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word, get_wordnet_pos(word)) for word in tokens]
    return lemmatized_words
# Sample Input
text = "The running cats were quickly jumping over the fences."
lemmatized_result = morphological_analysis(text)
print("Original Text:", text)
print("Morphological Analysis (Lemmatized Text):", lemmatized_result)

# Output
# PS D:\Github\program-examples> python -u "d:\Github\program-examples\resources\NLP\7a.py"
# [nltk_data] Downloading package punkt to
# [nltk_data]     C:\Users\harsh\AppData\Roaming\nltk_data...
# [nltk_data]   Package punkt is already up-to-date!
# [nltk_data] Downloading package averaged_perceptron_tagger to
# [nltk_data]     C:\Users\harsh\AppData\Roaming\nltk_data...   
# [nltk_data]   Unzipping taggers\averaged_perceptron_tagger.zip.
# [nltk_data] Downloading package wordnet to
# [nltk_data]     C:\Users\harsh\AppData\Roaming\nltk_data...
# Original Text: The running cats were quickly jumping over the fences.
# Morphological Analysis (Lemmatized Text): ['The', 'run', 'cat', 'be', 'quickly', 'jumping', 'over', 'the', 'fence', '.']