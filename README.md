# Long Text Summariser with ChatGPT

This repo provides two different summarisers, parallel and recursive, both can be used to summarize long texts (long = longer than OpenAI's maximum request token count, which is 4096)

## Requirements

- A recent version of python
- An openAI api key
- Something to run Jupyter Notebooks

### Dependencies

- openai: openai library, used to get chat completions
- tiktoken: a tokenizer by openai, used to split the text into chunks

## Usage

Check Main.ipynb.

## Recursive Summariser

Processes the text in chunks, summarises a chunk at a time and composes a new summary by accumulating with the summary generated so far.
Extracts a single short summary.

To be used to extract the most important information in a long text, to have a general idea.

## Parallel Summariser

Processes the text in chunks, summarises a chunk at a time and outputs all the generated short summaries.

To be used to summarise a few page long texts, and have a short summary of per page, or short summary of a few paragraphs in a long article.