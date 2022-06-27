from ..crawler import crawl, paginate, flatten, accumulate
from itertools import islice
import asyncio
import json

response_1 = {
    "count": 37,
    "next": "https://swapi.dev/api/species/?page=2",
    "previous": None,
    "results": [
        {
            "name": "Human",
            "classification": "mammal",
            "designation": "sentient",
            "average_height": "180",
            "skin_colors": "caucasian, black, asian, hispanic",
            "hair_colors": "blonde, brown, black, red",
            "eye_colors": "brown, blue, green, hazel, grey, amber",
            "average_lifespan": "120",
            "homeworld": "https://swapi.dev/api/planets/9/",
            "language": "Galactic Basic",
            "people": [
                "https://swapi.dev/api/people/66/",
                "https://swapi.dev/api/people/67/",
                "https://swapi.dev/api/people/68/",
                "https://swapi.dev/api/people/74/",
            ],
            "films": [
                "https://swapi.dev/api/films/1/",
                "https://swapi.dev/api/films/2/",
                "https://swapi.dev/api/films/3/",
                "https://swapi.dev/api/films/4/",
                "https://swapi.dev/api/films/5/",
                "https://swapi.dev/api/films/6/",
            ],
            "created": "2014-12-10T13:52:11.567000Z",
            "edited": "2014-12-20T21:36:42.136000Z",
            "url": "https://swapi.dev/api/species/1/",
        }
    ],
}

response_2 = {
    "count": 37,
    "next": "https://swapi.dev/api/species/?page=2",
    "previous": None,
    "results": [
        {
            "name": "Ewok",
            "classification": "mammal",
            "designation": "sentient",
            "average_height": "100",
            "skin_colors": "brown",
            "hair_colors": "white, brown, black",
            "eye_colors": "orange, brown",
            "average_lifespan": "unknown",
            "homeworld": "https://swapi.dev/api/planets/7/",
            "language": "Ewokese",
            "people": ["https://swapi.dev/api/people/30/"],
            "films": ["https://swapi.dev/api/films/3/"],
            "created": "2014-12-18T11:22:00.285000Z",
            "edited": "2014-12-20T21:36:42.155000Z",
            "url": "https://swapi.dev/api/species/9/",
        },
        {
            "name": "Sullustan",
            "classification": "mammal",
            "designation": "sentient",
            "average_height": "180",
            "skin_colors": "pale",
            "hair_colors": "none",
            "eye_colors": "black",
            "average_lifespan": "unknown",
            "homeworld": "https://swapi.dev/api/planets/33/",
            "language": "Sullutese",
            "people": ["https://swapi.dev/api/people/31/"],
            "films": ["https://swapi.dev/api/films/3/"],
            "created": "2014-12-18T11:26:20.103000Z",
            "edited": "2014-12-20T21:36:42.157000Z",
            "url": "https://swapi.dev/api/species/10/",
        },
    ],
}


response_3 = {
    "count": 37,
    "next": None,
    "previous": None,
    "results": [
        {
            "name": "Trandoshan",
            "classification": "reptile",
            "designation": "sentient",
            "average_height": "200",
            "skin_colors": "brown, green",
            "hair_colors": "none",
            "eye_colors": "yellow, orange",
            "average_lifespan": "unknown",
            "homeworld": "https://swapi.dev/api/planets/29/",
            "language": "Dosh",
            "people": ["https://swapi.dev/api/people/24/"],
            "films": ["https://swapi.dev/api/films/2/"],
            "created": "2014-12-15T13:07:47.704000Z",
            "edited": "2014-12-20T21:36:42.151000Z",
            "url": "https://swapi.dev/api/species/7/",
        },
        {
            "name": "Mon Calamari",
            "classification": "amphibian",
            "designation": "sentient",
            "average_height": "160",
            "skin_colors": "red, blue, brown, magenta",
            "hair_colors": "none",
            "eye_colors": "yellow",
            "average_lifespan": "unknown",
            "homeworld": "https://swapi.dev/api/planets/31/",
            "language": "Mon Calamarian",
            "people": ["https://swapi.dev/api/people/27/"],
            "films": ["https://swapi.dev/api/films/3/"],
            "created": "2014-12-18T11:09:52.263000Z",
            "edited": "2014-12-20T21:36:42.153000Z",
            "url": "https://swapi.dev/api/species/8/",
        },
    ],
}


_responses = [response_1, response_2, response_3]


def my_setup(params):
    start, stop = params
    responses = iter(islice(_responses, start, stop))

    class Response:
        def __await__(self):
            return iter([])

        def json(self):
            return next(responses)

    class client:
        async def get(url):
            return Response()

    return client, Response


def test_paginate():
    client, Response = my_setup([0, None])
    results = []

    def function(result):
        results.append(result.get("results"))

    asyncio.run(paginate(Response(), client, function))
    assert len(list(flatten(results))) == 5


def test_paginate_two_items():
    client, Response = my_setup([1, None])
    results = []

    def function(result):
        results.append(result.get("results"))

    asyncio.run(paginate(Response(), client, function))
    assert len(list(flatten(results))) == 4


def test_accumulator():
    client, Response = my_setup([0, None])
    results = asyncio.run(accumulate(Response(), client))
    assert len(results) == 5


def test_crawl():
    entities = ["films"]
    assert asyncio.run(crawl(entities))
    with open("starwars.json", "r") as f:
        data = json.load(f)
        assert len(data) == 6
