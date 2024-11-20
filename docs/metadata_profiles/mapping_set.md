---
layout: default
title: "Mapping Set Attributes"
permalink: /metadata_profiles/mapping_set
---

Unlike other FDOs considered here so far, mappings (and semantic artefacts, in general) are not critical to the functioning of digital twins, and instead are mostly a topic related to FAIR and open science. In that sense, the main goal here is to integrate the RO-Crate metadata profiles part with the mapping work done in the project (like [mapping.bio](https://mapping.bio/) and other related efforts).

The work done around mapping.bio is the starting point for this. Particularly, this initial [Mapping Set RO-Crate](https://mapping.bio/api/call?objectId=20.500.14269/aa2d56014fa6&method=getAsROCrate). Some slight modifications were applied to align it better with the Kernel Attributes in BioDT and the general RO-Crate guidelines. Since most of the terms don't have an equivalent in Schema.org, the [Simple Standard for Sharing Ontological Mappings (SSSOM)](https://mapping-commons.github.io/sssom/) is the main source used in this case.

## Mapping Set Attributes

Format: the name of each metadata attribute includes a link to [Schema.org](https://schema.org/) (or another vocabulary to which the property belongs), and is followed by a definition in the "Description" line. "Type" indicates the expected values for each property, while "Cardinality" specifies the amount and whether they are optional or mandatory. Lastly, additional remarks might be added as "Comments", and an example is given in the final line.

---

**[mapping_set_id](https://w3id.org/sssom/mapping_set_id)**

-   **Description:** A globally unique identifier for the mapping set (not each individual mapping).
-   **Type:** [URL](https://schema.org/URL)
-   **Cardinality:** 1/1
-   **Comments:** Should be IRI, ideally resolvable.
-   **Example:** `"mapping_set_id": "https://mapping.bio/api/objects/20.500.14269/aa2d56014fa6"`

---

**[mappings](https://w3id.org/sssom/mappings)**

-   **Description:** Contains a list of mapping objects.
-   **Type:** [Mapping](https://w3id.org/sssom/Mapping)
-   **Cardinality:** 1/many
-   **Comments:**
-   **Example:** `"mappings": [{"subject_id": "...", "predicate_id": "...", "object_id": "...", "mapping_justification": "...", "curation_rule": ["..."]}]`

---

**[subject_id](https://w3id.org/sssom/subject_id)**

-   **Description:** The ID of the subject of the mapping.
-   **Type:** [URL](https://schema.org/URL)
-   **Cardinality:** 1/1
-   **Comments:**
-   **Example:** `"subject_id": "http://purl.obolibrary.org/obo/HP_0009124"`

---

**[predicate_id](https://w3id.org/sssom/predicate_id)**

-   **Description:** The ID of the predicate or relation that relates the subject and object of this match.
-   **Type:** [URL](https://schema.org/URL)
-   **Cardinality:** 1/1
-   **Comments:**
-   **Example:** `"predicate_id": "skos:exactMatch"`

---

**[object_id](https://w3id.org/sssom/object_id)**

-   **Description:** The ID of the object of the mapping.
-   **Type:** [URL](https://schema.org/URL)
-   **Cardinality:** 1/1
-   **Comments:**
-   **Example:** `"object_id": "http://purl.obolibrary.org/obo/MP_0000003"`

---

**[mapping_justification](https://w3id.org/sssom/mapping_justification)**

-   **Description:** A mapping justification is an action (or the written representation of that action) of showing a mapping to be right or reasonable.
-   **Type:**
    -   [Text](https://schema.org/Text)
    -   [URL](https://schema.org/URL)
-   **Cardinality:** 1/1
-   **Comments:**
-   **Example:** `"mapping_justification": "semapv:ManualMappingCuration"`

---

**[curation_rule](https://w3id.org/sssom/curation_rule)**

-   **Description:** A curation rule is a (potentially) complex condition executed by an agent that led to the establishment of a mapping. Curation rules often involve complex domain-specific considerations, which are hard to capture in an automated fashion.
-   **Type:** [URL](https://schema.org/URL)
-   **Cardinality:** 1/many
-   **Comments:** The curation rule is captured as a resource rather than a string, which enables higher levels of transparency and sharing across mapping sets. The URI representation of the curation rule is expected to be a resolvable identifier which provides details about the nature of the curation rule.
-   **Example:** `"curation_rule": ["https://w3id.org/sssom/commons/disease/curation-rules/MPR2"]`

---

**[mapping_set_version](https://w3id.org/sssom/mapping_set_version)**

-   **Description:** A version string for the mapping.
-   **Type:**
    -   [Number](http://schema.org/Number)
    -   [Text](http://schema.org/Text)
-   **Cardinality:** 1/1
-   **Comments:** It is advised to follow the [semantic versioning](https://semver.org/) guidelines.
-   **Example:** `"version": "1.2.1"`

---

**[mapping_provider](https://w3id.org/sssom/mapping_provider)**

-   **Description:** URL pointing to the source that provided the mapping, for example an ontology that already contains the mappings, or a database from which it was derived.
-   **Type:** [URL](https://schema.org/URL)
-   **Cardinality:** 1/many
-   **Comments:**
-   **Example:** `"mapping_provider": "https://biodt.eu/wp5"`

---
