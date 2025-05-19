---
layout: default
title: "Dataset Attributes"
permalink: /metadata_profiles/dataset
---

Datasets are probably the most common type of FDO, and are widely used by different pDTs. Nonetheless, datasets can vary substantially: some might consist of a collection of data of the same type or format, while others might contain a mixture of datatypes. Likewise, they might be defined by a set of (say, a particular date range for a particular location) but can alse be open-ended (as with datafeeds that are automatically updated whenever recent data is obtained).

The metadata attributes shown below are based on the [RO-Crate guidelines](https://www.researchobject.org/ro-crate/1.1/), which rely on Schema.org's [Dataset](https://schema.org/Dataset) type. However, Bioschema's [Dataset](https://bioschemas.org/profiles/Dataset/1.0-RELEASE) profile offers a simpler selection more specific for our domain. They have also been influenced by the data sources used and described within BioDT's internal documentation.

There are several other (meta)data standards that could be interesting to align with, depending on the use case, the specifics of the dataset, and/or underlying technology of the prototype digital twin. For example:

- When necessary, more detailed metadata attributes could be included from the [Data Catalog Vocabulary (DCAT) - Version 3](https://www.w3.org/TR/vocab-dcat-3/#dcat-scope), while [Darwin Core](https://dwc.tdwg.org/) is more specific for the biodiversity domain.
- Current (meta)data models from the Research Infrastructures of BioDT, like the [GBIF Data Model](https://www.gbif.org/composition/HjlTr705BctcnaZkcjRJq/gbif-new-data-model), [DiSSCo's Open Digital Specimen](https://dev.terms.dissco.tech/), or the [LTER B2Share metadata attributes](https://b2share.eudat.eu/communities/LTER).
- The [ODMAP protocol](https://odmap.wsl.ch/) for reporting species distribution models.
- [Biodiversity data cubes](https://b-cubed.eu/data-and-evidence). This could link with the [Reliance RO-Crate profile](https://reliance-eosc.github.io/reliance-ro-crate/).
- HugginFace's [Dataset Cards](https://huggingface.co/docs/hub/datasets-cards) could be an interesting option for the AI-oriented datasets, as well as [Croissant Format Specification](https://docs.mlcommons.org/croissant/docs/croissant-spec.html).

## Dataset Attributes

Format: the name of each metadata attribute includes a link to [Schema.org](https://schema.org/) (or another vocabulary to which the property belongs), and is followed by a definition in the "Description" line. "Type" indicates the expected values for each property, while "Cardinality" specifies the amount and whether they are optional or mandatory. Lastly, additional remarks might be added as "Comments", and an example is given in the final line.

---

**[url](http://schema.org/url)**

- **Description:** The location of a page describing the dataset.
- **Type:** [URL](http://schema.org/URL)
- **Cardinality:** 1/1
- **Comments:**
- **Example:** `"url": "http://www.ebi.ac.uk/metabolights/MTBLS234"`

---

**[variableMeasured](https://schema.org/variableMeasured)**

- **Description:** The variables that are measured in the dataset, either described as text or as pairs of identifier and description using PropertyValue, or more explicitly as a [StatisticalVariable](https://schema.org/StatisticalVariable).
- **Type:**
    - [Property](https://schema.org/Property)
    - [PropertyValue](https://schema.org/PropertyValue)
    - [StatisticalVariable](https://schema.org/StatisticalVariable)
    - [Text](https://schema.org/Text)
- **Cardinality:** 1/many
- **Comments:** Often but not necessarily each [variableMeasured](https://schema.org/variableMeasured) will have an explicit representation as (or mapping to) an property such as those defined in Schema.org, or other RDF vocabularies and "knowledge graphs". In that case the subproperty of [variableMeasured](https://schema.org/variableMeasured) called [measuredProperty](https://schema.org/measuredProperty) is applicable.
- **Example:** `"variablesMeasured": "species cover"`

---

**[measurementTechnique](http://schema.org/measurementTechnique)**

- **Description:** A technique, method or technology used for measuring the corresponding variable(s) in the dataset. The [measurementTechnique](https://schema.org/measurementTechnique) property helps when extra clarification is needed about how a [measuredProperty](https://schema.org/measuredProperty) was measured.
- **Type:**
    - [DefinedTerm](https://schema.org/DefinedTerm)
    - [MeasurementMethodEnum](https://schema.org/MeasurementMethodEnum)
    - [Text](https://schema.org/Text)
    - [URL](https://schema.org/URL)
- **Cardinality:** 1/many
- **Comments:** If there are several [variableMeasured](https://schema.org/variableMeasured) properties recorded for some given data object, use a [PropertyValue](https://schema.org/PropertyValue) for each [variableMeasured](https://schema.org/variableMeasured) and attach the corresponding [measurementTechnique](https://schema.org/measurementTechnique). The value can also be from an enumeration, organized as a [MeasurementMetholdEnumeration](https://schema.org/MeasurementMetholdEnumeration).
- **Example:** `"measurementTechnique": "mass spectrometry"`

---

**[spatialCoverage](https://schema.org/spatialCoverage)**

- **Description:** The areas that the dataset applies to: a dataset of New York weather would have spatialCoverage which was the place: the state of New York. It is a subproperty of contentLocation.
- **Type:** [Place](https://schema.org/Place)
- **Cardinality:** 1/many
- **Comments:**
- **Example:** `"spatialCoverage": { "@id": "https://deims.org/6ae2f712-9924-4d9c-b7e1-3ddffb30b8f1"}`

---

**[temporalCoverage](https://schema.org/temporalCoverage)**

- **Description:** The relevant time period that the dataset applies to in a precise notation, either as a DateTime or as a textual string indicating a time period in [ISO 8601 time interval format](https://en.wikipedia.org/wiki/ISO_8601#Time_intervals).
- **Type:**
    - [DateTime](https://schema.org/DateTime)
    - [Text](https://schema.org/Text)
    - [URL](https://schema.org/URL)
- **Cardinality:** 1/many
- **Comments:** Open-ended date ranges can be written with ".." in place of the end date. For example, "2015-11/.." indicates a range beginning in November 2015 and with no specified final date. This is tentative and might be updated in future when ISO 8601 is officially updated.
- **Example:** `"temporalCoverage": "2023-11-01T00:00:00Z--2023-11-13T12:10:00Z"`

---

**[encodingFormat](https://schema.org/encodingFormat)**

- **Description:** Data type of the dataset files, typically expressed using a MIME format (see [IANA site](http://www.iana.org/assignments/media-types/media-types.xhtml) and [MDN reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)).
- **Type:**
    - [Text](https://schema.org/Text)
    - [URL](https://schema.org/URL)
- **Cardinality:** 1/many
- **Comments:** Unregistered or niche encoding and file formats can be indicated instead via the most appropriate URL, e.g. defining Web page or a Wikipedia/Wikidata entry.
- **Example:** `"encodingFormat": "text/csv"`

---

**[contentSize](https://schema.org/contentSize)**

- **Description:** The file size of the whole dataset in bytes.
- **Type:** [Text](https://schema.org/Text)
- **Cardinality:** 1/1
- **Comments:**
- **Example:** `"contentSize": "108MB"`

---

**[version](http://schema.org/version)**

- **Description:** The version number for this dataset.
- **Type:**
    - [Number](http://schema.org/Number)
    - [Text](http://schema.org/Text)
- **Cardinality:** 1/1
- **Comments:**
- **Example:** `"version": "8.0.1"`

---

**[publisher](http://schema.org/publisher)**

- **Description:** The publisher of the dataset, such as the research infrastructure providing access to it.
- **Type:**
    - [Organization](http://schema.org/Organization)
    - [Person](http://schema.org/Person)
- **Cardinality:** 0/1
- **Comments:** In BioDT, it will typically be one of the four research infrastructures involved in the project: GBIF, eLTER, DiSSCo, or LifeWatch ERIC.
- **Example:** `"publisher": {"@id": "https://ror.org/039kwqk96"}`

---

Apart from the mandatory attributes above, the previously mentioned profiles and standards include many other attributes that can be used to add further details when necessary.

#### Example Metadata File (`ro-crate-metadata.json`)

Below you can find an example RO-Crate metadata file conforming to the dataset profile. An empty template metadata file is also available through [this link](https://github.com/BioDT/biodt-fair/blob/main/docs/metadata_profiles/examples/dataset_template_ro-crate.json).

```json
{
    "@context": ["https://w3id.org/ro/crate/1.1/context"],
    "@graph": [
        {
            "@id": "ro-crate-metadata.json",
            "@type": "CreativeWork",
            "conformsTo": {
                "@id": "https://w3id.org/ro/crate/1.1"
            },
            "about": {
                "@id": "./"
            }
        },
        {
            "@id": "./",
            "@type": "Dataset",
            "identifier": "https://doi.org/10.23728/b2share.57315b8581cf45f6a5686b8ec1e0a788",
            "name": "Grassland Dynamics - Schrankogel (Austria) - 1994, 2004, 2014",
            "description": "Species cover according to the GLORIA Field Manual: https://gloria.ac.at/downloads/Manual_5thEd_ENG.pdf (p 38);%;1x1m plots arranged in transects at southern slopes of Mt. Schrankogel: https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.15290;visual estimate\n\nused for the Horizon Europe project \"Biodiversity Digital Twin for Advanced Modelling, Simulation and Prediction Capabilities\" (https://biodt.eu/).",
            "conformsTo": "https://biodt.github.io/biodt-fair/metadata_profiles/dataset",
            "license": {
                "@id": "http://hdl.handle.net/11304/8f7cb540-9eed-4298-b227-f3317a8a6e16"
            },
            "dateCreated": "2024-02-20",
            "creator": {
                "@id": "https://orcid.org/0000-0002-0655-3699"
            },
            "keywords": ["BioDT", "Grassland pDT"],
            "url": "https://doi.org/10.23728/b2share.57315b8581cf45f6a5686b8ec1e0a788",
            "variableMeasured": "Species cover",
            "measurementTechnique": {
                "@id": "http://hdl.handle.net/11304/8f7cb540-9eed-4298-b227-f3317a8a6e16"
            },
            "spatialCoverage": {
                "@id": "https://deims.org/6ae2f712-9924-4d9c-b7e1-3ddffb30b8f1"
            },
            "temporalCoverage": ["1994", "2004", "2014"],
            "contentSize": "3.9 MB",
            "version": "1",
            "publisher": {
                "@id": "https://ror.org/039kwqk96"
            },
            "hasPart": [
                {
                    "@id": "http://hdl.handle.net/11304/ed009f64-8cd2-4b5c-a9d4-6c3f7ee35110"
                },
                {
                    "@id": "http://hdl.handle.net/11304/8f7cb540-9eed-4298-b227-f3317a8a6e16"
                },
                {
                    "@id": "http://hdl.handle.net/11304/1ed9e403-6be6-4011-aa62-032641f40cf8"
                },
                {
                    "@id": "http://hdl.handle.net/11304/f3c2bc8d-fd70-4d90-bd7f-0875312d27d0"
                },
                {
                    "@id": "http://hdl.handle.net/11304/1691a59c-f8e8-4b28-ac76-fa90cf2bb5d8"
                }
            ]
        },
        {
            "@id": "https://deims.org/6ae2f712-9924-4d9c-b7e1-3ddffb30b8f1",
            "@type": "Place",
            "name": "GLORIA Master Site Schrankogel (AT-SCH), Stubaier Alpen - Austria",
            "description": "GLORIA Master Site.The 3497m-peak Mount Schrankogel belongs to the highest mountains of the Austrian Alps. Its northern and eastern side is surrounded by glaciers and glacier forelands. Its southern to western faces, however, are not interrupted by glacier Established in 1994 as the first comprehensive alpine to nival long-term monitoring site for high-altitude vegetation in the Alps, with ca. 1000 permanent plots of 1x1m arranged in transects of 30x3m or smaller ranging from 2900m to 3450m. Main purpose is ecological climate impact research. In 2001 it became a master site of the GLORIA network: e.g. method development and testing for species recording in 1x1m plots for GLORIA was partly conducted on Schrankogel. The first major resurvey of plots was made in 2004, the second resurvey was conducted in 2014. Besides long-term monitoring, several other research approaches were/are carried out at the Schrankogel site, such as species and vegetation modeling, vegetation mapping, phenological studies of alpine and nival plants, exclosure studies for grazing impacts at the lower altitudes of the site, soil studies, snow pattern studies (two permanent snow cameras), surface and soil-temperature measurements. In 2014, the the scope was extended to other organism groups such as soil microbiota, soil mesofauna (Oribatida and Collembola in particular), and surface-dwelling arthropods. Site setup, resurveys, or other activities were/are supported by: the Austrian Academy of Sciences through a national grant of the International Geosphere–Biosphere and the UNESCO MaB Programmes, by the Austrian and through the Institute of Mountain Research (IGF) of the Academy; by the Austrian Federal Ministry of Science and Research; the Austrian Federal Ministry of Agriculture, Forestry, Environment and Water Management; the Swiss MAVA Foundation; the Government of Tyrol; the project ALARM (Assessing Large-Scale Risks for Biodiversity with Tested Methods; No. GOCE-CT-2003-506675) in the FP-6 of the EU; the Austrian Climate Research Programme (ACRP: GZ B368633 ACRP6 - SCHRANKOGEL_20YEARS - KR13AC6K11076). For further details on Schrankogel_GLORIA see: http://www.gloria.ac.at/?a=42&b=56",
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": "47.041162",
                "longitude": "11.098057",
                "polygon": "11.098595 47.044335, 11.105804 47.043341, 11.108294 47.040182, 11.089754 47.035971, 11.091986 47.041118, 11.098595 47.044335",
                "name": "Latitude: 47.041162 Longitude: 11.098057"
            }
        },
        {
            "@id": "http://hdl.handle.net/11304/ed009f64-8cd2-4b5c-a9d4-6c3f7ee35110",
            "@type": "File",
            "name": "AT_Schrankogel_data_cover.csv",
            "description": "Species cover data and related variables as comma-separated values",
            "contentSize": "3.80 MB",
            "encodingFormat": "text/csv"
        },
        {
            "@id": "http://hdl.handle.net/11304/1ed9e403-6be6-4011-aa62-032641f40cf8",
            "@type": "File",
            "name": "AT_Schrankogel_method.csv",
            "description": "species cover according to the GLORIA Field Manual: https://gloria.ac.at/downloads/Manual_5thEd_ENG.pdf (p 38)",
            "contentSize": "349 B",
            "encodingFormat": "text/csv"
        },
        {
            "@id": "http://hdl.handle.net/11304/f3c2bc8d-fd70-4d90-bd7f-0875312d27d0",
            "@type": "File",
            "name": "AT_Schrankogel_reference.csv",
            "description": "List of taxa used for the species cover",
            "about": { "@id": "http://hdl.handle.net/11304/ed009f64-8cd2-4b5c-a9d4-6c3f7ee35110" },
            "contentSize": "9.33 KB",
            "encodingFormat": "text/csv"
        },
        {
            "@id": "http://hdl.handle.net/11304/1691a59c-f8e8-4b28-ac76-fa90cf2bb5d8",
            "@type": "File",
            "name": "AT_Schrankogel_station.csv",
            "description": "Details about the station where the data was collected",
            "about": { "@id": "http://hdl.handle.net/11304/ed009f64-8cd2-4b5c-a9d4-6c3f7ee35110" },
            "contentSize": "227.19 KB",
            "encodingFormat": "text/csv"
        },
        {
            "@id": "https://orcid.org/0000-0002-0655-3699",
            "@type": "Person",
            "name": "Christoph Wohner",
            "affiliation": [
                {
                    "@id": "https://ror.org/039kwqk96"
                },
                {
                    "@id": "https://ror.org/013vyke20"
                }
            ]
        },
        {
            "@id": "https://ror.org/039kwqk96",
            "@type": "Organisation",
            "name": "Long Term Ecological Research Network",
            "url": "https://lternet.edu/"
        },
        {
            "@id": "https://ror.org/013vyke20",
            "@type": "Organisation",
            "name": "Environment Agency Austria",
            "url": "http://www.umweltbundesamt.at/en/"
        },
        {
            "@id": "http://hdl.handle.net/11304/8f7cb540-9eed-4298-b227-f3317a8a6e16",
            "@type": ["File", "CreativeWork"],
            "name": "AT_Schrankogel_license.csv",
            "contentSize": "131 B",
            "encodingFormat": "text/csv"
        }
    ]
}
```
