# anki_card_generator/card_generator.py

from .utils import process_content

class AnkiCardGenerator:
    def __init__(self, gpt_model):
        self.gpt_model = gpt_model

    def generate_card(self, topic):
        content = self.gpt_model.generate(topic)
        question, answer = process_content(content)
        return question, answer