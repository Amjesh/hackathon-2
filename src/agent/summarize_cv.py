from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


def summarize_cv(cv_text):
    parser = PlaintextParser.from_string(cv_text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    # Summarize to 2 sentences (adjust as needed)
    summary = summarizer(parser.document, 2)
    return ' '.join([str(sentence) for sentence in summary])
