from text_utils import clean_text, word_count

assert clean_text("  Hello World  ") == "hello world"
assert word_count("Open source tools") == 3

print("All tests passed")
