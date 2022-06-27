# Corinth Code

Deployed to https://corinth-code.vercel.app/

## Development

Start with `npm run dev`

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result

## Tests

* Unit tests: `npm run tests`
* UI tests: `npm run ui-tests`

# Simple Version

Using next.js, the simple version calls the Star Wars API directly.
The search is unoptimized. Debouncing is needed.
The search also uses the provided search that the Star Wars API provides. This only searches one entity type e.g. person, at a time.

# Advanced Version

The Star Wars API is small. Putting the entities into Algoila and using their provided search UI, the search experience is vastly richer.
This shifts the search from the API directly to a search provider.
Asynchronously, the search database may be changed to reflect changes of the data from the API.


# Tentmaking

## `tentmaking/api.py`

When deployed, this small "gateway" API will request related resources for the entity requested e.g. a person. The list of related resources is hardcoded for simplicity. This could be moved to an environmental variable or as user input with the request to make it more dynamic.

After requesting the related resources concurrently, the API will replace the entity link with the response, making a single HTTP request possible from the frontend to get an entity and its associated related resources.

## Dependencies

1. `cd tentmaking`
1. [Create a virtualenv for python](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
1. `pip install -r requirements.txt`

## Tests

1. `pytest`


## `tentmaking/crawler.py`

Crawls the Star Wars API and stores each entity on the file system.

This data can then be used to populate the search index.

## `tentmaking/search.py`

Uploads the Star Wars API data to the search index.
