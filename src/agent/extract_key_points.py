import spacy

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")


def extract_key_points(cv_text):
    # Process the CV text using spaCy
    doc = nlp(cv_text)

    # Initialize dictionaries to store extracted information
    key_points = {
        'Skills': [],
        'Experience': [],
        'Education': [],
        'Other': []
    }

    # Extract key information from the parsed document
    for ent in doc.ents:
        if ent.label_ == 'SKILL':
            key_points['Skills'].append(ent.text)
        elif ent.label_ == 'ORG' or ent.label_ == 'LOC':
            key_points['Experience'].append(ent.text)
        elif ent.label_ == 'DATE':
            key_points['Education'].append(ent.text)
        else:
            key_points['Other'].append(ent.text)

    return key_points
