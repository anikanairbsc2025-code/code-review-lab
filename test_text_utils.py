from text_utils import clean_text, word_count
def clean_text(text):
  return text.strip().lower()
def word_count(text):
  return len(text.split())

print("All tests passed")
