import markovify

# Read the dataset
with open("dataset/sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Create the Markov model
# state_size=1 works better for small datasets
text_model = markovify.Text(text, state_size=1)

print("=" * 60)
print("        TEXT GENERATION USING MARKOV CHAINS")
print("=" * 60)

while True:
    # Try multiple times to generate a sentence
    sentence = text_model.make_short_sentence(200, tries=100)

    if sentence:
        print("\nGenerated Text:")
        print(sentence)
    else:
        print("\nNo sentence could be generated. Try adding more text to the dataset.")

    choice = input("\nGenerate another sentence? (y/n): ").strip().lower()

    if choice != "y":
        print("\nThank you for using the Text Generator!")
        break