def is_encoded(word):
    vowels = set('aeiouAEIOU')
    for i, char in enumerate(word):
        if char in vowels and i + 2 < len(word):
            if word[i+1] == char and word[i+2] == char:
                return True
    return False

def decode_word(word):
    if not is_encoded(word):
        return word
    
    vowels = set('aeiouAEIOU')
    result = []
    i = 0
    while i < len(word):
        result.append(word[i])
        if word[i] in vowels and i + 2 < len(word):
            if word[i+1] == word[i] and word[i+2] == word[i]:
                i += 3  # Skip the next two characters if they're the same as the vowel
            else:
                i += 1
        else:
            i += 1
    return ''.join(result)

# Get input from user
input_text = input()

# Check if the input length is within the valid range
if 0 < len(input_text) <= 100:
    # Split the input into words and decode each word
    words = input_text.split()
    decoded_words = [decode_word(word) for word in words]
    output_text = ' '.join(decoded_words)
    print(output_text)
else:
    print(input_text)  # Print original text if length is invalid