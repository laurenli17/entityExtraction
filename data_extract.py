import spacy
nlp = spacy.load("zh_core_web_sm")
doc = nlp("这是一个句子。")
