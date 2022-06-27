import asyncio
import httpx
from itertools import chain


API_DOMAIN = "https://swapi.dev"


def handler(event, context):
    return asyncio.run(get(event["path"]))


async def get(path):
    async with httpx.AsyncClient() as client:
        people = await client.get(f"{API_DOMAIN}{path}")
        person = people.json()
        related_things = ["starships", "films"]
        related = [
            [client.get(thing) for thing in person[things]] for things in related_things
        ]
        responses = await asyncio.gather(
            *chain.from_iterable(related), return_exceptions=True
        )
        return replace_with_response(person, related_things, map_response(responses))


def map_response(responses):
    jsons = [r.json() for r in responses]
    mapped_responses = {}
    [mapped_responses.update({j["url"]: j}) for j in jsons]
    return mapped_responses


def replace_with_response(obj, keys, replacements):
    for key in keys:
        new_list = []
        for thing in obj[key]:
            new_list.append(replacements[thing])
        obj[key] = new_list
    return obj
