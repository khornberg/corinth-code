from itertools import chain
import json
import asyncio
import httpx

API_DOMAIN = "https://swapi.dev"


def flatten(iterable):
    return chain.from_iterable(iterable)


async def accumulate(response, client):
    results = []

    def accumulator(result):
        results.append(result.get("results"))

    await paginate(response, client, accumulator)
    return list(flatten(results))


async def paginate(response, client, function):
    while True:
        try:
            result = response.json()
            function(result)
            if not result.get("next"):
                break
            return await paginate(
                await client.get(result.get("next")), client, function
            )
        except StopIteration:
            break


async def get_entity(entity, client):
    path = f"/api/{entity}"
    response = await client.get(f"{API_DOMAIN}{path}")
    return await accumulate(response, client)


async def crawl(entities):
    async with httpx.AsyncClient() as client:
        requests = [get_entity(entity, client) for entity in entities]
        responses = await asyncio.gather(*requests, return_exceptions=True)
        return dump(responses)


def dump(responses):
    with open("starwars.json", "w") as f:
        data = list(flatten(responses))
        json.dump(data, f)
        print(f"Dumpped {len(data)} records")
    return True


if __name__ == "__main__":
    entities = {
        "films": "https://swapi.dev/api/films/",
        "people": "https://swapi.dev/api/people/",
        "planets": "https://swapi.dev/api/planets/",
        "species": "https://swapi.dev/api/species/",
        "starships": "https://swapi.dev/api/starships/",
        "vehicles": "https://swapi.dev/api/vehicles/",
    }
    asyncio.run(crawl(list(entities.keys())))
