from ..api import handler, map_response, replace_with_response


starship_12 = {
    "name": "X-wing",
    "model": "T-65 X-wing",
    "manufacturer": "Incom Corporation",
    "cost_in_credits": "149999",
    "length": "12.5",
    "max_atmosphering_speed": "1050",
    "crew": "1",
    "passengers": "0",
    "cargo_capacity": "110",
    "consumables": "1 week",
    "hyperdrive_rating": "1.0",
    "MGLT": "100",
    "starship_class": "Starfighter",
    "pilots": [
        "https://swapi.dev/api/people/1/",
        "https://swapi.dev/api/people/9/",
        "https://swapi.dev/api/people/18/",
        "https://swapi.dev/api/people/19/",
    ],
    "films": [
        "https://swapi.dev/api/films/1/",
        "https://swapi.dev/api/films/2/",
        "https://swapi.dev/api/films/3/",
    ],
    "created": "2014-12-12T11:19:05.340000Z",
    "edited": "2014-12-20T21:23:49.886000Z",
    "url": "https://swapi.dev/api/starships/12/",
}

film_1 = {
    "title": "A New Hope",
    "episode_id": 4,
    "opening_crawl": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....",
    "director": "George Lucas",
    "producer": "Gary Kurtz, Rick McCallum",
    "release_date": "1977-05-25",
    "characters": [
        "https://swapi.dev/api/people/1/",
        "https://swapi.dev/api/people/2/",
        "https://swapi.dev/api/people/3/",
        "https://swapi.dev/api/people/4/",
        "https://swapi.dev/api/people/5/",
        "https://swapi.dev/api/people/6/",
        "https://swapi.dev/api/people/7/",
        "https://swapi.dev/api/people/8/",
        "https://swapi.dev/api/people/9/",
        "https://swapi.dev/api/people/10/",
        "https://swapi.dev/api/people/12/",
        "https://swapi.dev/api/people/13/",
        "https://swapi.dev/api/people/14/",
        "https://swapi.dev/api/people/15/",
        "https://swapi.dev/api/people/16/",
        "https://swapi.dev/api/people/18/",
        "https://swapi.dev/api/people/19/",
        "https://swapi.dev/api/people/81/",
    ],
    "planets": [
        "https://swapi.dev/api/planets/1/",
        "https://swapi.dev/api/planets/2/",
        "https://swapi.dev/api/planets/3/",
    ],
    "starships": [
        "https://swapi.dev/api/starships/2/",
        "https://swapi.dev/api/starships/3/",
        "https://swapi.dev/api/starships/5/",
        "https://swapi.dev/api/starships/9/",
        "https://swapi.dev/api/starships/10/",
        "https://swapi.dev/api/starships/11/",
        "https://swapi.dev/api/starships/12/",
        "https://swapi.dev/api/starships/13/",
    ],
    "vehicles": [
        "https://swapi.dev/api/vehicles/4/",
        "https://swapi.dev/api/vehicles/6/",
        "https://swapi.dev/api/vehicles/7/",
        "https://swapi.dev/api/vehicles/8/",
    ],
    "species": [
        "https://swapi.dev/api/species/1/",
        "https://swapi.dev/api/species/2/",
        "https://swapi.dev/api/species/3/",
        "https://swapi.dev/api/species/4/",
        "https://swapi.dev/api/species/5/",
    ],
    "created": "2014-12-10T14:23:31.880000Z",
    "edited": "2014-12-20T19:49:45.256000Z",
    "url": "https://swapi.dev/api/films/1/",
}

people_1 = {
    "name": "Jek Tono Porkins",
    "height": "180",
    "mass": "110",
    "hair_color": "brown",
    "skin_color": "fair",
    "eye_color": "blue",
    "birth_year": "unknown",
    "gender": "male",
    "homeworld": "https://swapi.dev/api/planets/26/",
    "films": [film_1],
    "species": [],
    "vehicles": [],
    "starships": [starship_12],
    "created": "2014-12-12T11:16:56.569000Z",
    "edited": "2014-12-20T21:17:50.343000Z",
    "url": "https://swapi.dev/api/people/19/",
}


def test_api():
    event = {"path": "/api/people/19"}
    expected = people_1
    assert handler(event, {}) == expected


def _get_some_responses(n=2):
    urls = iter(("a", "b", "c"))

    class Response:
        def json(self):
            return {"url": next(urls)}

    return [Response() for r in range(n)]


def test_map_responses():
    expected = {"a": {"url": "a"}, "b": {"url": "b"}}
    assert map_response(_get_some_responses()) == expected


def test_replace_with_response():
    obj = {"things": ["a", "b"], "another": ["c"]}
    keys = ["things", "another"]
    replacements = map_response(_get_some_responses(n=3))
    expected = {"things": [{"url": "a"}, {"url": "b"}], "another": [{"url": "c"}]}
    assert replace_with_response(obj, keys, replacements) == expected
