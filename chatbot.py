"""NLP processing and FAQ matching for the College Enquiry Chatbot."""
import re
import nltk
from nltk.tokenize import wordpunct_tokenize
from nltk.stem import PorterStemmer

# NLTK stopwords are optional: the fallback keeps the project usable offline.
BASIC_STOP_WORDS = {
    "a", "an", "the", "is", "are", "am", "was", "were", "be", "been",
    "being", "to", "of", "in", "on", "for", "and", "or", "but", "with",
    "at", "by", "from", "as", "do", "does", "did", "how", "what", "when",
    "where", "which", "who", "can", "could", "would", "should", "i", "me",
    "my", "we", "our", "you", "your", "it", "this", "that", "about", "tell"
}

def load_stopwords():
    try:
        return set(nltk.corpus.stopwords.words("english"))
    except LookupError:
        try:
            nltk.download("stopwords", quiet=True)
            return set(nltk.corpus.stopwords.words("english"))
        except Exception:
            return BASIC_STOP_WORDS

STOP_WORDS = load_stopwords()
STEMMER = PorterStemmer()

def preprocess(text):
    """Lowercase, tokenize, remove stopwords and stem alphabetic words."""
    tokens = wordpunct_tokenize(text.lower())
    return {
        STEMMER.stem(token)
        for token in tokens
        if token.isalpha() and token not in STOP_WORDS
    }

def similarity(user_tokens, faq_tokens):
    """Return a simple overlap score between 0 and 1."""
    if not user_tokens or not faq_tokens:
        return 0.0
    common = user_tokens.intersection(faq_tokens)
    return len(common) / min(len(user_tokens), len(faq_tokens))

class CollegeChatbot:
    def __init__(self, faqs, threshold=0.30):
        self.faqs = faqs
        self.threshold = threshold

    def get_response(self, message):
        message = message.strip()
        if not message:
            return "Please type a question."

        simple = re.sub(r"[^a-z\s]", "", message.lower()).strip()

        if simple in {"hi", "hello", "hey", "good morning", "good afternoon"}:
            return ("Hello! Welcome to the College Enquiry Chatbot. "
                    "How can I help you?")
        if simple in {"bye", "goodbye", "see you"}:
            return "Thank you for contacting us. Have a nice day!"
        if "thank" in simple:
            return "You're welcome! Feel free to ask another college-related question."

        user_tokens = preprocess(message)
        best_score = 0.0
        best_answer = None

        for item in self.faqs:
            for example in item["questions"]:
                score = similarity(user_tokens, preprocess(example))
                if score > best_score:
                    best_score = score
                    best_answer = item["answer"]

        if best_answer and best_score >= self.threshold:
            return best_answer

        return (
            "Sorry, I could not understand your question. Try asking about "
            "admissions, courses, fees, hostel, transport, library, exams "
            "or placements. You can also contact the college office."
        )
