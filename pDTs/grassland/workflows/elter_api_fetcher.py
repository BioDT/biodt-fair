# Return PIDs of BioDT+Grassland records from B2Share
#
# written for the BioDT project https://doi.org/10.3030/101057437
# February 2025

import json
from urllib.request import urlopen
import argparse

# Query B2Share API for LTER, BioDT and Grassland records (hardcoded)
parser = argparse.ArgumentParser(
    prog='elter_api_fetcher',
    description='Return a file with the JSON response to a B2Share API query.')
parser.add_argument('--query', type=str)
args = parser.parse_args()
search_query = args.query
# search_query = "https://b2share.eudat.eu/api/records/?page=1&sort=bestmatch&q=keywords.keyword%3D%27BioDT+AND+Grassland+pDT%27&size=100"

# Read response into a JSON object
json_response = json.loads(urlopen(search_query).read())
with open("b2share_records.json", mode='w', encoding="utf-8") as f:
    json.dump(json_response, f)

# Extract PIDs from JSON object's metadata
# pids = [record["metadata"]["DOI"] for record in json_response['hits']['hits']]
# with open("elter_pids.json", mode='w', encoding="utf-8") as f:
#     json.dump(pids, f)
