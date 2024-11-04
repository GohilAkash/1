!pip install nltk

import nltk
nltk.download('punkt')
nltk.download('stopwords')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Example text data
text = "hello my name is jordan i live in london,jordan"

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Stop word removal
stop_words = set(stopwords.words('english'))
filtered_tokens = [w for w in tokens if not w.lower() in stop_words]
print("Filtered Tokens:", filtered_tokens)

# Further processing (e.g., stemming, lemmatization)
# ...