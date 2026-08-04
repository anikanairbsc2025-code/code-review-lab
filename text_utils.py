def clean_text(text):
    cleaned_text = text.lower().strip()
    return cleaned_text


def word_count(text):
    count = 0
    for _ in text.split():
        count += 1
    return count
