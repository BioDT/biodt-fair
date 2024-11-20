---
layout: default
title: "Model Attributes"
permalink: /metadata_profiles/model
---

Central to the prototype Digital Twins (pDTs) are the computational models that power them. Even within a single scientific discipline, there are many different types of models which function in a different way. Here, we use refer to computational models as a computational representation of a problem or a process that can be executed to simulate, solve, or analyse the behaviour of a system. Given the reliance of computational models on software code, we have drawn inspiration from the [CodeMeta Project](https://codemeta.github.io/) and FAIR-IMPACT's [Guidelines for recommended metadata standard for research software within EOSC](https://zenodo.org/records/10786147) (which reference the _FAIR principles for Research Software_ —or FAIR4RS— extensively) for the metadata attributes.

For more detailed descriptions of specific types of models, consider the following resources:

-   The [ODMAP protocol](https://odmap.wsl.ch/) for species distribution models (SDMs): and particularly.
-   HugginFace's [Model Cards](https://huggingface.co/docs/hub/en/model-cards) for machine learning (ML) models.

## Model Attributes

Format: the name of each metadata attribute includes a link to [Schema.org](https://schema.org/) (or another vocabulary to which the property belongs), and is followed by a definition in the "Description" line. "Type" indicates the expected values for each property, while "Cardinality" specifies the amount and whether they are optional or mandatory. Lastly, additional remarks might be added as "Comments", and an example is given in the final line.

---

**[codeRepository](https://schema.org/codeRepository)**

-   **Description:** Link to the repository or repositories where the un-compiled, human-readable code is located.
-   **Type:** [URL](https://schema.org/URL)
-   **Cardinality:** 1/many
-   **Comments:** A link to GitHub, GitLab, or similar. Preferably, the code repository should be under the [BioDT GitHub organisation](https://github.com/BioDT) so people in the project have access to it.
-   **Example:** `"codeRepository": "https://github.com/BioDT/biodt-fair"`

---

**[contributor](https://schema.org/contributor)**

-   **Description:** Additional people or organisations that contributed to developing the model, despite not having authorship.
-   **Type:**
    -   [Organization](http://schema.org/Organization)
    -   [Person](http://schema.org/Person)
-   **Cardinality:** 0/many
-   **Comments:** If possible, use an ORCiD (or ROR ID, for organizations), otherwise use full name in natural order.
-   **Example:** `"contributor": "https://orcid.org/0000-0003-0791-7164"`

---

**[softwareVersion](https://schema.org/softwareVersion)**

-   **Description:** The version of the model instance.
-   **Type:** [Text](https://schema.org/Text)
-   **Cardinality:** 1/1
-   **Comments:** It is advised to follow the [semantic versioning](https://semver.org/) guidelines.
-   **Example:** `"softwareVersion": "2.0.13"`

---

**[programmingLanguage](https://schema.org/programmingLanguage)**

-   **Description:** The computer programming language the code is written in.
-   **Type:**
    -   [ComputerLanguage](http://schema.org/ComputerLanguage)
    -   [Text](http://schema.org/Text)
-   **Cardinality:** 1/many
-   **Comments:**
-   **Example:** `"programmingLanguage": "Python"`

---

**[softwareRequirements](https://schema.org/softwareRequirements)**

-   **Description:** Component dependency requirements for the model.
-   **Type:**
    -   [Text](http://schema.org/Text)
    -   [URL](http://schema.org/URL)
-   **Cardinality:** 0/many
-   **Comments:** This includes runtime environments and shared libraries that are not included as part of the model but are required to run it.
-   **Example:** `"softwareRequirements" : "https://pypi.org/project/cwltool/"`

---

**[supportingData](https://schema.org/supportingData)**

-   **Description:** Related datasets used for the model, for example, as training or input data.
-   **Type:**
    -   [Dataset](https://schema.org/Dataset)
    -   [DataFeed](https://schema.org/DataFeed)
-   **Cardinality:** 1/many
-   **Comments:**
-   **Example:** `"supportingData": {"@id": "https://doi.org/10.15468/dl.b3n3r9"}`

---

#### Example Metadata File (`ro-crate-metadata.json`)

```json
{
    "@context": ["https://w3id.org/ro/crate/1.1"],
    "@graph": [
        {
            "@id": "ro-crate-metadata.json",
            "@type": "CreativeWork",
            "about": { "@id": "./" },
            "conformsTo": { "@id": "https://w3id.org/ro/crate/1.1" },
            "author": { "@id": "http://orcid.org/0000-0003-0401-5122" }
        },
        {
            "@id": "./",
            "@type": ["Dataset", "SoftwareApplication"],
            "identifier": "https://workflowhub.eu/workflows/810?version=1",
            "name": "Cultural Ecosystem Services pDT - Biodiversity Model",
            "description": "Species distribution models for species that provide cultural ecosystem services.",
            "conformsTo": "https://biodt.github.io/biodt-fair/metadata_profiles/model",
            "dateCreated": "2023-06-29",
            "license": { "@id": "https://spdx.org/licenses/MIT.html" },
            "author": [
                { "@id": "https://orcid.org/0000-0001-6755-9456" },
                { "@id": "https://orcid.org/0000-0003-2428-272X" },
                { "@id": "https://orcid.org/0009-0003-5290-786X" },
                { "@id": "https://orcid.org/0000-0002-4180-9338" },
                { "@id": "https://orcid.org/0000-0003-0401-5122" }
            ],
            "codeRepository": "https://github.com/BioDT/uc-ces/tree/main/biodiversity_model",
            "contributors": [
                { "@id": "https://orcid.org/0000-0001-6755-9456" },
                { "@id": "https://orcid.org/0009-0003-5290-786X" }
            ],
            "softwareVersion": "0.1.0",
            "programmingLanguage": "R",
            "softwareRequirements": [
                "readr",
                "rmarkdown",
                "dplyr",
                "spThin",
                "knitr",
                "fields",
                "viridisLite",
                "spam",
                "rgbif",
                "flexsdm",
                "sf",
                "terra"
            ],
            "supportingData": [{ "@id": "https://doi.org/10.15468/dl.b3n3r9" }]
        },
        {
            "@id": "https://doi.org/10.15468/dl.b3n3r9",
            "@type": "DataFeed",
            "name": "Species occurrence data from the Cairngorms, Scotland",
            "description": "Species occurrence data from the Cairngorms, Scotland was obtained by download from GBIF. We filtered environmental variables to only include environment data from within a 5 km buffer of recorded occurrences, and conducted spatial thinning.",
            "variableMeasured": "species occurrence",
            "measurementTechnique": "",
            "spatialCoverage": { "@id": "https://sws.geonames.org/10104113/" },
            "temporalCoverage": "",
            "encodingFormat": "",
            "contentSize": "179 KB",
            "version": "",
            "publisher": "GBIF"
        },
        {
            "@id": "https://sws.geonames.org/10104113/",
            "@type": "Place",
            "name": "Cairngorms National Park",
            "description": "The Cairngorms is part of an international family of National Parks and is the largest in the UK, at 4,528 sq km (1,748 sq miles). It is located in the Scottish Highlands, 127 miles north of Edinburgh and 140 miles north of Glasgow. The Park covers parts of Aberdeenshire, Moray, Highland, Angus and Perth and Kinross. Nearly half of the land in the National Park is considered ‘wild land’. 49 per cent of the park has been recognised as being of international importance for nature, and is protected by European Law. There are 19 Areas of Conservation, 12 Special Protection Areas and 46 Sites of Special Scientific Interest within the Park.",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": "57.04395",
                "longitude": "-3.60334",
                "name": "Latitude: 57.04395 Longitude: -3.60334"
            }
        },
        {
            "@id": "https://orcid.org/0000-0001-6755-9456",
            "@type": "Person",
            "name": "Simon Rolph",
            "email": "simrol@ceh.ac.uk",
            "affiliation": { "@id": "https://ror.org/00pggkr55" }
        },
        {
            "@id": "https://orcid.org/0000-0003-2428-272X",
            "@type": "Person",
            "name": "Chris Andrews",
            "affiliation": { "@id": "https://ror.org/00pggkr55" }
        },
        {
            "@id": "https://orcid.org/0009-0003-5290-786X",
            "@type": "Person",
            "name": "Dylan Carbone",
            "email": "dylcar@ceh.ac.uk",
            "affiliation": { "@id": "https://ror.org/00pggkr55" }
        },
        {
            "@id": "https://orcid.org/0000-0002-4180-9338",
            "@type": "Person",
            "name": "Jan Dick",
            "affiliation": { "@id": "https://ror.org/00pggkr55" }
        },
        {
            "@id": "https://ror.org/00pggkr55",
            "@type": "Organization",
            "name": "UK Centre for Ecology & Hydrology",
            "url": "https://www.ceh.ac.uk/"
        },
        {
            "@id": "http://orcid.org/0000-0003-0401-5122",
            "@type": "Person",
            "name": "Julian Lopez Gordillo",
            "affiliation": { "@id": "https://ror.org/0566bfb96" }
        },
        {
            "@id": "https://ror.org/0566bfb96",
            "@type": "Organization",
            "name": "Naturalis Biodiversity Center",
            "url": "http://www.naturalis.nl/"
        },
        {
            "@id": "http://orcid.org/0000-0002-0655-3699",
            "@type": "Person",
            "name": "Christoph Wohner",
            "affiliation": { "@id": "https://ror.org/013vyke20" }
        },
        {
            "@id": "https://ror.org/013vyke20",
            "@type": "Organization",
            "name": "Environment Agency Austria",
            "url": "http://www.umweltbundesamt.at/en/"
        },
        {
            "@id": "https://ror.org/05fjyn938",
            "@type": "Organization",
            "name": "Global Biodiversity Information Facility",
            "url": "https://www.gbif.org/"
        },
        {
            "@id": "https://spdx.org/licenses/MIT.html",
            "@type": "CreativeWork",
            "name": "MIT License",
            "description": "The MIT License is a permissive free software license originating at the Massachusetts Institute of Technology in the late 1980s. As a permissive license, it puts only very limited restriction on reuse and has, therefore, high license compatibility."
        }
    ]
}
```
