import json

input_json = "sample_2.json"

with open(input_json, "r", encoding="utf-8") as f:
    data = json.load(f)

# Extract guidelines from the "sentences" array
guidelines = [sentence.strip() for sentence in data.get("sentences", [])]

# Save guidelines to a text file
with open("extracted_guidelines.txt", "w", encoding="utf-8") as f:
    for guideline in guidelines:
        f.write(guideline + "\n")

# Save guidelines to a JSON file
with open("extracted_guidelines.json", "w", encoding="utf-8") as f:
    json.dump([{"guideline": g} for g in guidelines], f, indent=4, ensure_ascii=False)

# Print guidelines
for guideline in guidelines:
    print(guideline)
