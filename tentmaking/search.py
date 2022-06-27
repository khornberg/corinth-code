import os
import json
from algoliasearch.search_client import SearchClient


def load_dotenv():
    with open("../.env.local", "r") as f:
        lines = f.readlines()
        for line in lines:
            key, value = line.replace("\n", "").split("=")
            os.environ[key] = value


def load():
    API_KEY = os.environ.get("API_KEY")
    INDEX = "corinth"
    client = SearchClient.create("8H44TT0Z6X", API_KEY)
    index = client.init_index(INDEX)
    with open("starwars.json") as f:
        records = json.load(f)
    index.save_objects(records, {"autoGenerateObjectIDIfNotExist": True})


def add_type():
    # after the fact of getting the data
    with open("starwars.json", "r") as f:
        records = json.load(f)

    with open("starwars.json", "w") as f:
        for r in records:
            r["type"] = r["url"].split("/")[4]
        json.dump(records, f)


if __name__ == "__main__":
    load_dotenv()
    load()
