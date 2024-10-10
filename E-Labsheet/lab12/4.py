def validate_filename(filename):
    # Step 1: Replace spaces and forbidden characters with underscores
    forbidden_chars = r'[\\/*:|"<>\s]'
    cleaned_filename = re.sub(forbidden_chars, '_', filename)

    # Step 2: Replace all dots except the last one with underscores
    if '.' in cleaned_filename:
        name_parts = cleaned_filename.rsplit('.', 1)  # Split on the last dot
        name, extension = name_parts[0], name_parts[1]
    else:
        name, extension = cleaned_filename, ''  # No extension present
    
    # Step 3: Replace any remaining dots in the name with underscores
    name = name.replace('.', '_')
    
    # Step 4: Truncate the name to a maximum of 15 characters
    name = name[:15]
    
    # Step 5: Truncate the extension to a maximum of 3 characters
    extension = extension[:3]
    
    # Step 6: Reconstruct the filename with a dot, only if there's an extension
    if extension:
        return f"{name}.{extension}"
    else:
        return name

# Test cases
test_filenames = [
    "a.b.c.d.e",        # Normal case
    "abcdefghijklmnop.qrstuv",  # Long filename with extension
    "*$ 7h|$_to<>:dif.\/.g|od",     # Filename without extension
    "Is this too difficult?",  # Multiple dots in filename
    "invalid*chars<>|\".mp3",  # Invalid characters in filename
    "no_extension_needed",  # No extension
]

# Apply the function to each test case
validated_filenames = [validate_filename(fn) for fn in test_filenames]
validated_filenames
