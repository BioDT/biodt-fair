# Create RO-Crates from BioDT B2Share records
#
# written for the BioDT project https://doi.org/10.3030/101057437
# February 2025

from rocrate.rocrate import ROCrate  # tested with rocrate 0.13.0
from rocrate.model import ContextEntity, Person
import json
import deims


### --- Dataset crates
with open("elter_records.json", mode='r', encoding="utf-8") as f:
    json_response = json.load(f)
datasets = []



# Loop through all records
for record in json_response['hits']['hits']:

    # Create an empty RO-Crate for each record
    dataset_crate = ROCrate()

    # Add properties from record metadata
    dataset_crate.name = record["metadata"]["titles"][0]["title"]
    dataset_crate.description = record["metadata"]["descriptions"][0]["description"]

    dataset_crate.root_dataset.append_to("identifier", record["metadata"]["DOI"])
    datasets.append(record["metadata"]["DOI"])
    dataset_crate.root_dataset.append_to("dateCreated", record["created"])
    dataset_crate.root_dataset.append_to("variableMeasured", "Grassland Dynamics")
    dataset_crate.root_dataset.append_to("conformsTo", "https://biodt.github.io/biodt-fair/metadata_profiles/dataset")

    list_of_keyword_labels = []
    for keyword in record["metadata"]["keywords"]:
        list_of_keyword_labels.append(keyword["keyword"])
    dataset_crate.keywords = list_of_keyword_labels

    # Add authors
    creators = []
    for creator in record["metadata"]["creators"]:
        # FIXME: Can we get ORCIDs (or a URL) for the authors?
        creator_id = '#' + (creator["given_name"] + creator["family_name"]).replace(' ', '')
        creator_entity = dataset_crate.add(Person(dataset_crate, creator_id, properties={
            "family_name": creator["family_name"],
            "given_name": creator["given_name"]
        }))
        creators.append(creator_entity)
    dataset_crate.root_dataset.append_to("creator", creators)

    eLTER = dataset_crate.add(ContextEntity(dataset_crate, "https://elter-ri.eu/", properties={
        "@type": "Organization",
        "name": "eLTER",
        "description": "Integrated European Long-Term Ecosystem, critical zone and socio-ecological Research",
        "url": "https://elter-ri.eu/",
    }))
    dataset_crate.root_dataset.append_to("publisher", eLTER)

    # Add location information - deims.id can be used to get any information about site from DEIMS
    deims_id = record["metadata"]["community_specific"]["d2f5457f-6318-494a-b363-8098356035b7"]["metadata_url"]
    deims_site_record = deims.getSiteById(deims_id)
    coordinates = deims_site_record["attributes"]["geographic"]["coordinates"].split("(")[1].split(")")[0].split(" ")

    place = dataset_crate.add(ContextEntity(dataset_crate, deims_id, properties={
        "@type": "Place",
        "name": deims_site_record["attributes"]["general"]["siteName"],
        "description": deims_site_record["attributes"]["general"]["abstract"],
        "geo": {
            "@id":deims_id,
            "@type": "GeoCoordinates",
            "lat": coordinates[1],
            "lon": coordinates[0],
        }
    }))
    dataset_crate.root_dataset.append_to("spatialCoverage", place)

    # Add related files
    for file in record['files']:
        current_file = dataset_crate.add_file(file['ePIC_PID'], properties={
            "name": file['key'],
            "contentSize": str(file['size']),
        })

    # Add license information
    licence = dataset_crate.add(ContextEntity(dataset_crate, identifier=record["metadata"]["license"]["license_uri"], properties={
        "@type": "CreativeWork",
        "identifier": record["metadata"]["license"]["license_identifier"],
        "name": record["metadata"]["license"]["license"]
    }))
    dataset_crate.root_dataset.append_to("license", licence)

    # Write RO-Crate to disk
    dataset_crate.write(dataset_crate.name.replace('/', '-'))
### --- Dataset crates
