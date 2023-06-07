from io_utils import split_into_chunks
from get_completion import get_completion

PROMPT_TEMPLATE = """
Generate a summary by following the steps below:

1- Generate the summary of the text which is delimited with ~~.
2- By using the summary created in step 1 and another given text which is delimited by <>, generate a new summary of these. \
Keep as much as details possible from the summary generated in step 1. \
If the given text which is delimited by <> is empty, only generate the summary of the text which is delimited with ~~.
3- Output only the final generated summary from step 2.

~{chunk}~
<{summary}>

"""

def summarise_recursively(text):
    chunks = split_into_chunks(text)
    summary = ""

    for chunk in chunks:
        summary = _get_completion_recursively(chunk, summary)
    
    return summary

def _get_completion_recursively(chunk, summary):

    prompt = PROMPT_TEMPLATE.format(chunk=chunk, summary=summary)
    return get_completion(prompt)