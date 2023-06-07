import tiktoken

CHUNK_TOKEN_SIZE = 3750
MODEL = 'gpt-3.5-turbo'

def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def save_file(content, filepath):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def split_into_chunks(text):
    encoding = tiktoken.encoding_for_model(MODEL)
    words = encoding.encode(text)
    chunks = []
    for i in range(0, len(words), CHUNK_TOKEN_SIZE):
        chunks.append(''.join(encoding.decode(words[i:i + CHUNK_TOKEN_SIZE])))
    return chunks 