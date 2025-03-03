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
import os
from pathlib import Path

# Retrieve PIDs from Grassland's dataset RO-Crates
base_dir = Path('./')
directories = [f for f in base_dir.iterdir()
          if f.is_dir() and f.name.startswith("Grassland Dynamics - ")]
datasets = [ ROCrate(rocrate).root_dataset["identifier"][0] for rocrate in directories]

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
model_creator1 = model_crate.add(Person(model_crate, "https://orcid.org/0000-0001-8541-789X", properties={
    "family_name": "Banitz",
    "given_name": "Thomas",
    "affiliation": {"@id": "https://ror.org/000h6jb29"}
}))
model_creator2 = model_crate.add(Person(model_crate, "https://orcid.org/0000-0001-7594-8152", properties={
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
