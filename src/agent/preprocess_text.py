import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# Function to preprocess text
def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalnum(
    ) and token not in stopwords.words('english')]
    return set(tokens)
