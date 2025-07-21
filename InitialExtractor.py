# InitialExtractor.py
# Function to extract uppercase initials from a full name

def extract_initials(full_name: str) -> str:
    # Strip leading/trailing spaces and split by spaces
    words = full_name.strip().split()
    # Take the first character of each word and convert to uppercase
    initials = ''.join(word[0].upper() for word in words if word)
    return initials

# Test cases
test_names = [
    "John Doe",
    "   alice   brown   ",
    "Mahatma Gandhi",
    "leonardo da vinci",
    "A P J Abdul Kalam"
]

# Report results
print("Initial Extractor Report:\n")
for name in test_names:
    result = extract_initials(name)
    print(f"Input: '{name}' -> Output: '{result}'")
