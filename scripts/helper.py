import re
from nltk.corpus import stopwords

# Load english stopwords
stop_words = set(stopwords.words('english'))

def clean_headline(text):
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove punctuation and numbers (keep only letters)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    # 3. Remove extra spaces
    text = text.strip()
    
    # 4. Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    return ' '.join(words)