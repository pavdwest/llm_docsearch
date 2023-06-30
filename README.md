# Overview

A simple collection of LLM snippets and utilities.

# How to Use

1. Download or clone the repo: `git clone git@github:pavdwest/llm_docsearch.git`
2. `cd llm_docsearch`
3. Create virtual env: `pip -m venv .venv`
4. Activate venv: `source ./venv/bin/activate`
5. Install requirements: `pip install -r requirements.txt`
6. Copy `.env.example` to `.env` and fill out your OpenAI key

# Running the Example

The `docs` folder already contains some example data saved as pdfs and raw text, attributed to the following sources:

* https://www.touropia.com/famous-cathedrals-in-the-world/
* https://www.veranda.com/travel/g33234419/beautiful-cathedrals-in-the-world/
* https://www.rivieratravel.co.uk/blog/2019/05/23/the-10-most-famous-cathedrals-and-basilicas-across-europe/
* https://www.thecollector.com/greatest-gothic-cathedrals/

## Run 'training'

`python ./train.py`

It should output something like the following:

```
Delete existing db...
Loading 4 documents...
Creating vector db...
Done!
```
Note that you can rerun the training at any time to delete the existing db and reload only the files currently in the `docs` dir.

## Run the query

`python ./run_query.py`

It should output something like the following:

```
Running query: 'When was the Cologne Cathedral built and how tall is it?'
Response: ' The Cologne Cathedral was built in 1248 and is 157 metres tall. This information can be found in the Riviera Travel Blog and Touropia sources.'
```

# Running with your own data

## (Optional) Backup the Example Data

It might be worth making a backup of the example `docs` if you'd like to use them again in the future.

## Delete the Example Data

Delete everything in the `docs` directory.

## Load your own data

Copy all of your source documents into the `docs` folder.
Explicitly supported file types are `*.html` and `*.pdf`. It will attempt to load other types as text, mileage may vary.

## Run 'training'

Run 'training':

`python ./train.py`

## Run a query

Run a query by passing it as basic text via the command line:

`python ./run_query.py Find all the details about 'SomeTopic' in my documents`
