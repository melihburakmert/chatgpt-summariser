from concurrent.futures import ThreadPoolExecutor

from io_utils import split_into_chunks
from get_completion import get_completion

PROMPT_TEMPLATE = """
Generate a summary of the text below which is delimited with ~~ by keeping the important details.
Only output the generated summary, nothing else.

~{chunk}~

"""

def summarise_in_parallel(text):
    chunks = split_into_chunks(text)
    prompts = [PROMPT_TEMPLATE.format(chunk=chunk) for chunk in chunks]

    with ThreadPoolExecutor() as executor:
        responses = list(executor.map(get_completion, prompts))

    for response in responses:
        print(response)