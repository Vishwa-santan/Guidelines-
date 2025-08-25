
from pypdf import PdfReader
import spacy
import nltk

nltk.download("punkt")
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text


pdf_path = "sample.pdf"
parsed_text = extract_text_from_pdf(pdf_path)

from nltk.tokenize import sent_tokenize
sentences = sent_tokenize(parsed_text)

print("Sample Sentences:\n", sentences[:5])

nlp = spacy.load("en_core_web_sm")
doc = nlp(parsed_text)

print("\nNamed Entities:")
for ent in doc.ents[:20]: 
    print(ent.text, "-", ent.label_)

clean_sentences = [s.replace("\n", " ").replace("\uf07c", " ") for s in sentences]
print(clean_sentences[:5])

#convert into json
import json

clean_sentences = [s.replace("\n", " ").replace("\uf07c", " ") for s in sentences]

entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

data = {
    "sentences": clean_sentences[:20],   
    "entities": entities
}

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)






