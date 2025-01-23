# Create RO-Crates from BioDT B2Share records
#
# written for the BioDT project https://doi.org/10.3030/101057437
# January 2025

# Comment/uncomment if executing as a Jupyter notebook
# !pip install rocrate
# !pip install deims

from rocrate.rocrate import ROCrate  # tested with rocrate 0.13.0
from rocrate.model import ContextEntity, Person, SoftwareApplication, ComputerLanguage, RootDataset
import json
import deims
from urllib.request import urlopen

### --- Dataset crates
# Query B2Share API for LTER, BioDT and Grassland records
url = "https://b2share.eudat.eu/api/records/?q=keywords.keyword=%27BioDT%20AND%20Grassland%20pDT%27&community=d952913c-451e-4b5c-817e-d578dc8a4469&size=100"
response = urlopen(url)
json_response = json.loads(response.read())
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

### --- Model crate
model_crate = ROCrate()

root_dataset = model_crate.add(RootDataset(model_crate, properties={
    "@type": ["Dataset", "SoftwareApplication"],
    "conformsTo": "https://biodt.github.io/biodt-fair/metadata_profiles/model",
    "name": "GRASSMIND",
    "description": "GRASSMIND is an individual- and process-based grassland model designed for simulating the structure and dynamics of species-rich herbaceous communities (including management).",
    "dateCreated": "2024-07-10",
    "keywords": ["BioDT", "Biodiversity dynamics", "Grasslands"],
    "license": {"@id": "https://eupl.eu/"},
    "codeRepository": "https://github.com/BioDT/uc-grassland", # FIXME: Currently a private repo. Shouldn't it be made public?
    # "contributor": [],
    "softwareVersion": "2.0.0",
    "programmingLanguage": {"@id": "https://isocpp.org/"},
    # "softwareRequirements": [],
    "supportingData": datasets,
    "url": "https://www.ufz.de/index.php?en=48445",
}))

cpp_language = model_crate.add(ComputerLanguage(model_crate, "https://isocpp.org/", properties={
    "name": "C++",
    "description": "C++ is a high-level, general-purpose programming language. C++ has object-oriented, generic, and functional features, in addition to facilities for low-level memory manipulation for systems like microcomputers.",
    "version": "C++23"
})) # FIXME: Should we add or change this to Python, as used in BioDT work?

# Add authors
model_creator1 = model_crate.add(ContextEntity(model_crate, "https://orcid.org/0000-0001-8541-789X", properties={
    "@type": "Person",
    "family_name": "Banitz",
    "given_name": "Thomas",
    "affiliation": {"@id": "https://ror.org/000h6jb29"}
}))
model_creator2 = model_crate.add(ContextEntity(model_crate, "https://orcid.org/0000-0001-7594-8152", properties={
    "@type": "Person",
    "family_name": "Taubert",
    "given_name": "Franziska",
    "affiliation": {"@id": "https://ror.org/000h6jb29"}
}))
ufz_affiliation = model_crate.add(ContextEntity(model_crate, "https://ror.org/000h6jb29", properties={
    "@type": "Organization",
    "name": "Helmholtz Centre for Environmental Research",
    "url": "https://www.ufz.de/"
}))
model_crate.root_dataset.append_to("creator", [model_creator1, model_creator2])

# Write RO-Crate to disk
model_crate.write(model_crate.name)
### --- Model crate
