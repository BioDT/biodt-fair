---
layout: default
title: "BioDT RO-Crate Metadata Profiles Documentation"
permalink: /
---

![BioDT Logo]({{ '/assets/images/biodt-logo-colour.png' | relative_url }}){: .center-image width="600"}

The [Biodiversity Digital Twin (BioDT) project](about) has produced several outputs in different formats. This site provides documentation on the main [RO-Crate metadata profiles](metadata_profiles) used within the project.

### Context

BioDT aims to push the current boundaries of predictive understanding of biodiversity dynamics by developing digital twins providing advanced modelling, simulation and prediction capabilities. As defined by the [Digital Twin Consortium](https://www.digitaltwinconsortium.org/):

> A digital twin is a virtual representation of real-world entities and processes, synchronised with real-world data at a specified frequency and fidelity. In turn, digital twinning refers to the process of designing and developing digital twins, and integrating them into their wider operational environment.

To that end, the project deals with heterogeneous use cases, each involving different data, models, and workflows. Rather than a single biodiversity digital twin, several _prototype digital twins_ (pDTs) are being developed in parallel within the project (see the [Building Biodiversity Digital Twins](https://doi.org/10.3897/rio.coll.240) topical collection for details). This heterogeneity is also reflected in the volume and type of data sources the pDTs need, as well as the underlying software and workflows they rely on.

Inherent to the concept of a digital twin is its ability to remain synchronised, which might involve updating certain components (i.e. updating some of its data sources or software packages). Those changes and dependencies must be captured to provide reliable provenance about how the digital twin's outputs were produced. In this context, the FAIR principles play an important role for the digital twin's future sustainability. Specifically, the [FAIR Digital Objects](https://fairdo.org/) (FDO) initiative provided a lower-level implementation framework that helped structure the different elements that compose a digital twin:

> A FAIR digital object is structured in a way that is interpretable by computer systems, and having as essential elements an assigned globally unique and persistent identifier (PID), a type definition for the object as a whole and typically a metadata description of the properties of the object, making the whole findable, accessible, interoperable and reusable both by humans and computers for the reliable interpretation of the data represented by the object.

FDOs can be implemented in several ways. Given the distributed nature of BioDT, a lightweight and adaptable metadata format would be a great fit. That role is fulfilled by RO-Crate, a mature specification for packaging research data with their metadata (based on Schema.org annotations in JSON-LD).

### About RO-Crate

[RO-Crate](https://www.researchobject.org/ro-crate/about_ro_crate) is a community effort to establish a lightweight approach to packaging research data with their metadata.

An RO-Crate is a Research Object (or _RO_) formed of a collection of data (a _crate_) and a special `ro-crate-metadata.json` file which describes the collection. The collection may contain any kind of research data - papers, data files, software, references to other research, and so on. It may be a folder full of files, an abstract grouping of connected references, or a combination of both.

The `ro-crate-metadata.json` file (also known as the _RO-Crate Metadata Document_) is a plain text file, readable by humans and machines, that includes metadata for each item within the collection - the authors, license, identifier, provenance, and so on. Any folder can be turned into an RO-Crate by adding an `ro-crate-metadata.json` file.

### Metadata profiles

While the flexibility offered by RO-Crate is a great feature, some mechanism is needed to achieve harmonisation across different pDTs. Several metadata profiles were designed for linking and describing the different kinds of digital objects present in the project, such as the interactions between data, models and workflows to compose digital twins:

-   [Kernel Attributes]({{ '/metadata_profiles/kernel' | relative_url }}) cover all the general information that is common to any digital object. While they are described independently here, they don't constitute a separate profile themselves, and instead are present in all of the other profiles.
-   [Dataset]({{ '/metadata_profiles/dataset' | relative_url }}) is used to describe the data sources, either as discrete datasets or continuous data streams that keep being updated with newer data.
-   [Model]({{ '/metadata_profiles/model' | relative_url }}) is a computational representation of a problem or a process that can be executed to simulate, solve, or analyse the behaviour of a system. Typically, they depend on one or multiple datasets for an accurate representation.
-   [Workflow]({{ '/metadata_profiles/workflow' | relative_url }}) captures multi-step methods involving different tools to collect, process and analyse data, which typically result in a certain output.
-   [Mapping Set]({{ '/metadata_profiles/mapping_set' | relative_url }}) represents a set of individual mappings between certain terms, typically describing the translation between two particular semantic artefacts.

Beyond the metadata profiles, this site is not meant to provide extensive documentation or resources related to the project. For a more general and up-to-date view on developments around FAIR and Open Science within the BioDT project, check the [`biodt-fair`](https://github.com/BioDT/biodt-fair) GitHub repo.

### Project Acknowledgements

_This study has received funding from the European Union's Horizon Europe research and innovation programme under grant agreement No 101057437 (BioDT project, [https://doi.org/10.3030/101057437](https://doi.org/10.3030/101057437)). Views and opinions expressed are those of the author(s) only and do not necessarily reflect those of the European Union or the European Commission. Neither the European Union nor the European Commission can be held responsible for them._

![Funded by the European Union]({{ '/assets/images/eu-flag.png' | relative_url }}){:width="400px"}

### License

[MIT](https://choosealicense.com/licenses/mit/)
