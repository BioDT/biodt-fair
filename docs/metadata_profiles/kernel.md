---
layout: default
title: "Kernel Attributes"
permalink: /metadata_profiles/kernel
---

The _kernel attributes_ are common to all BioDT FAIR digital objects (FDOs) regardless of their type, and contain fundamental information such as their licence, author or the date of publication. If some metadata attribute is of high importance but does not apply to all FDOs, it is reserved for the type-specific metadata profiles. The kernel attributes have been kept to a minimum for the sake of implementation within the pDTs and the rest of the technical architecture of the project, but more attributes can be incorporated as they are needed (i.e., the list is not exclusive).

## Kernel Attributes

Format: the name of each metadata attribute includes a link to [Schema.org](https://schema.org/) (or another vocabulary to which the property belongs), and is followed by a definition in the "Description" line. "Type" indicates the expected values for each property, while "Cardinality" specifies the amount and whether they are optional or mandatory. Lastly, additional remarks might be added as "Comments", and an example is given in the final line.

---

**[conformsTo](http://purl.org/dc/terms/conformsTo)**

-   **Description:** The profile that a certain metadata description follows.
-   **Type:** [URL](https://schema.org/URL)
-   **Cardinality:** 1/1
-   **Comments:** For now, we can refer to these documentation pages for the profiles.
-   **Example:** `"conformsTo": "https://biodt.github.io/biodt-fair/metadata_profiles/dataset"`

---

**[license](http://schema.org/license)**

-   **Description:** License for the FDO the metadata description is about.
-   **Type:** [URL](https://schema.org/URL)
-   **Cardinality:** 1/1
-   **Comments:** The FDO might have a certain license, however, the metadata file should have a CC0 license.
-   **Example:** `"license": {"@id": "https://creativecommons.org/licenses/by/4.0/"}`

---

**[@id](https://www.w3.org/TR/json-ld/#node-identifiers) / [identifier](https://schema.org/identifier)**

-   **Description:** An identifier for the FDO. Ideally, a globally unique, persistent and resolvable identifier.
-   **Type:** [IRI](https://datatracker.ietf.org/doc/html/rfc3987#section-2)
-   **Cardinality:** 1/1
-   **Comments:** As an alternative for `"@id"` (for example, for other serialisations), [`"identifier"`](http://schema.org/identifier) can be used in addition to it in order to specify a PID.
-   **Example:** `"@id": "https://doi.org/10.1111/1365-2664.12222"`

---

**[@type](https://www.w3.org/TR/json-ld/#specifying-the-type) / [additionalType](https://schema.org/additionalType)**

-   **Description:** The nature of the object the metadata describes. In BioDT, we currently consider [Dataset](https://schema.org/Dataset), [SoftwareApplication](https://schema.org/SoftwareApplication) (for computational models), [ComputationalWorkflow](https://bioschemas.org/profiles/ComputationalWorkflow) and [MappingSet](https://mapping-commons.github.io/sssom/MappingSet/).
-   **Type:** [Text](https://schema.org/Text)
-   **Cardinality:** 1/many
-   **Comments:** `"@type"` is a reserved term in JSON-LD and there are certain restrictions to its usage. Here, apart from complying with JSON-LD and RO-Crate, we use that attribute to determine the digital object type. `additionalType` might be used for that purpose.
-   **Example:** `"@type": ["File", "SoftwareSourceCode", "ComputationalWorkflow"]`

---

**[name](https://schema.org/name)**

-   **Description:** Name of the FDO.
-   **Type:** [Text](https://schema.org/Text)
-   **Cardinality:** 1/1
-   **Comments:**
-   **Example:** `"name": "BEEHAVE model"`

---

**[description](http://schema.org/description)**

-   **Description:** Short description of what the FDO is.
-   **Type:** [Text](https://schema.org/Text)
-   **Cardinality:** 1/1
-   **Comments:**
-   **Example:** `"description": "BEEHAVE is a computer model to simulate the development of a honeybee colony and its nectar and pollen foraging behavior in different..."`

---

**[dateCreated](http://schema.org/dateCreated)**

-   **Description:** The date on which the FDO was created or the item was added to a DataFeed.
-   **Type:**
    -   [Date](http://schema.org/Date)
    -   [DateTime](http://schema.org/DateTime)
-   **Cardinality:** 1/1
-   **Comments:** `"datePublished"` and `"dateModified"` can also be included to add further details.
-   **Example:** `"dateCreated": "2020-04-07 13:16:09 UTC"`

---

**[creator](http://schema.org/creator)**

-   **Description:** Creator of the FDO.
-   **Type:**
    -   [Organization](http://schema.org/Organization)
    -   [Person](http://schema.org/Person)
-   **Cardinality:** 1/many
-   **Comments:** If possible, use an ORCiD or ROR ID, otherwise use full name in natural order. Closely related to the [author](http://schema.org/author) attribute; it can be used interchangeably.
-   **Example:** `"creator": [{"@id": "http://orcid.org/0000-0003-0791-7164"}, {"@id": "http://orcid.org/0000-0002-3221-9512"}, {"@id": "http://orcid.org/0000-0003-2338-4636"}],`

---

**[keywords](https://schema.org/keywords)**

-   **Description:** A comma-separated list of keywords or tags used to describe some item.
-   **Type:** [Text](https://schema.org/Text)
-   **Cardinality:** 1/many
-   **Comments:**
-   **Example:** `"keywords": ["bioacoustics", "bird sound recognition", "deep learning"]`

---

#### Example Metadata File (`ro-crate-metadata.json`)

_Note: simplified from the [Dataset](dataset) example by excluding dataset-specific attributes._

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
            "conformsTo": "https://biodt.github.io/biodt-fair/metadata_profiles/kernel",
            "license": {
                "@id": "http://hdl.handle.net/11304/8f7cb540-9eed-4298-b227-f3317a8a6e16"
            },
            "dateCreated": "2024-02-20",
            "creator": {
                "@id": "https://orcid.org/0000-0002-0655-3699"
            },
            "keywords": ["BioDT", "Grassland pDT"],
            "publisher": {
                "@id": "https://ror.org/039kwqk96"
            }
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
