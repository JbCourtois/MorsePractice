import unicodedata


def remove_accents(text):
    # Normalize the text to decompose accents from letters
    text = unicodedata.normalize('NFD', text)
    # Remove all accents by filtering out the combining characters
    text = ''.join([char for char in text if not unicodedata.combining(char)])
    return text


def read_and_process_file(file_path):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content into paragraphs (separated by two blank lines)
    paragraphs = content.split('\n\n')

    # Remove accents from each paragraph
    paragraphs_no_accents = [
        remove_accents(paragraph.strip())
        for paragraph in paragraphs if paragraph.strip()
    ]

    return paragraphs_no_accents
