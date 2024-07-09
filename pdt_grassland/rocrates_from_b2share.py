# Create RO Crates from BioDT B2Share records
#
# written for the BioDT project https://doi.org/10.3030/101057437
# July 2024

!pip install rocrate
!pip install deims

from rocrate.rocrate import ROCrate # tested with rocrate 0.10.0
from rocrate.model.contextentity import ContextEntity
import json
import deims
from urllib.request import urlopen

# Create RO Crates from BioDT B2Share records
#
# written for the BioDT project https://doi.org/10.3030/101057437   
# Feb 2024

# query B2Share API for LTER, BioDT and Grassland records
url = "https://b2share.eudat.eu/api/records/?q=keywords.keyword=%27BioDT%20AND%20Grassland%20pDT%27&community=d952913c-451e-4b5c-817e-d578dc8a4469"
response = urlopen(url)
json_response = json.loads(response.read())

crate = ROCrate()

for record in json_response['hits']['hits']:

    # deims.id can be used to get any information about site from DEIMS
    deims_id = record["metadata"]["community_specific"]["d2f5457f-6318-494a-b363-8098356035b7"]["metadata_url"]

    list_of_keyword_labels = []
    for keyword in record["metadata"]["keywords"]:
        list_of_keyword_labels.append(keyword["keyword"])

    list_of_related_files = []


    deims_site_record = deims.getSiteById(deims_id)

    current_crate = crate.add(ContextEntity(crate, "dataset", properties={
        "name": record["metadata"]["titles"][0]["title"],
        "description": record["metadata"]["descriptions"][0]["description"],
        "keywords": list_of_keyword_labels,
        "dateCreated": record["created"],
        "variableMeasured": "Grassland Dynamics",
        "spatialCoverage": {
            "@id": deims_id
        },
        "hasPart": list_of_related_files
    }))

    eLTER = crate.add(ContextEntity(crate, "https://elter-ri.eu/", properties={
        "@type": "Organization",
        "name": "eLTER",
        "url": "https://elter-ri.eu/",
    }))
    current_crate.append_to("organization", eLTER)

    deims_site_record["attributes"]["geographic"]

    coordinates = deims_site_record["attributes"]["geographic"]["coordinates"]
    coordinates = coordinates.split("(")[1].split(")")[0].split(" ")

    place = crate.add(ContextEntity(crate, deims_id, properties={
        "@type": "Place",
        "name": deims_site_record["attributes"]["general"]["siteName"],
        "description": deims_site_record["attributes"]["general"]["abstract"],
        "geo": {
            "@type": "GeoCoordinates",
            "lat": coordinates[1],
            "lon": coordinates[0],
        }
    }))
    current_crate.append_to("Place", place)

    for file in record['files']:
        list_of_related_files.append(file['ePIC_PID'])
        current_file = crate.add_file(file['ePIC_PID'], properties={
            "name": file['key'],
            "contentSize": str(file['size']),
        })

    current_crate.append_to("file", current_file)

# crate.write("grassland_crate")
