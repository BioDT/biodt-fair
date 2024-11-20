# BioDT - FAIR tutorials and materials

This repository hosts some materials concerning the FAIR aspect of the data, software, and other digital objects within the [Biodiversity Digital Twin (BioDT) project](https://cordis.europa.eu/project/id/101057437). While the [Confluence wiki](https://wiki.eduuni.fi/display/cscRDIcollaboration/BioDT?src=contextnavpagetreemode) remains the main tool for collaboration within the project, this repository is meant to complement it with more technical information and tools, as well as open visibility for the wider community —also ensuring that these resources remain accessible after the sunset of the project.

## Content

The information on this repository is distributed as follows:

-   The [Documentation](https://biodt.github.io/biodt-fair/) page: for detailed information about some of the FAIR aspects of BioDT, such as the RO-Crate metadata profiles.
-   The [Issues](https://github.com/BioDT/biodt-fair/issues) and [Pull requests](https://github.com/BioDT/biodt-fair/pulls) tabs: as usual for any code git repository, this is aimed at collaborating in the development of the materials in this repository. Issues can be opened to start a discussion for any topic concerning FAIR in BioDT, while Pull Requests capture discussions around specific code contributions.
-   The [BioDT FAIR Roadmap](https://github.com/orgs/BioDT/projects/1): a planning tool in the Projects tab where important tasks that are planned or actively being worked on are displayed.

### Prototype Digital Twin (pDT) directories

Each pDT has its own directory, where we will store the materials related to the FAIR aspects of the pDT. For example, the metadata descriptions for the digital objects in development. Currently, we have the following pDTs:

-   `pDTs/ces/`: Prototype Digital Twin for Cultural Ecosystem Services (CES).
-   `pDTs/cwr/`: Prototype Digital Twin for Crop Wild Relatives (CWR).
-   `pDTs/grassland/`: Prototype Digital Twin for Grassland Biodiversity Dynamics.
-   `pDTs/ias/`: Prototype Digital Twin for Invasive Alien Species (IAS).
-   `pDTs/pollinators/`: Prototype Digital Twin for Pollinators.
-   `pDTs/rtbm/`: Prototype Digital Twin for Real-Time Bird Monitoring (RTBM).

### `fdo_profiles/` directory

In this folder, we will store the metadata profiles (and related materials) that we will use in BioDT —which are closely related to the FAIR Digital Objects (FDO) and RO-Crate frameworks. Such profiles are expected to evolve over the course of the project (see the [documentation for the metadata profiles](https://biodt.github.io/biodt-fair/metadata_profiles). So far, the profile work has been focused on:

-   Kernel attributes: this is about the attributes that apply to all digital objects in BioDT, regardless of their purpose. It covers fundamental metadata such as IDs, type, author, license...
-   Model attributes: the `models/` subdirectory covers the metadata for the main software from each pDT.
-   Dataset attributes: the `datasets/` subdirectory includes the profiles for the different types of data used in BioDT.
-   Workflow attributes: the `workflows/` subdirectory focuses on the elements that bring everything together (connecting the data to the models, sending jobs to HPC, etc).
-   Mapping Set attributes: the `mapping-sets/` subdirectory contains resources for mappings between semantic artefacts.
-   Additionally, other auxiliary resources can be found in the `other/` directory.

### `examples/` directory

This directory contains some materials that have been developed mainly for illustrative purposes. For example:

-   `leipzig_workshop/`: This subdirectory contains a Jupyter notebook and some metadata files used during the BioDT workshop in Leipzig, Nov 2023. It aims to give an introduction to FAIR and RO-Crate in the context of data for BioDT.
-   `dataset_ro-crate.ipynb`: It goes over how to turn an existing dataset into an RO-Crate, with descriptions on the main elements of RO-Crate and how some FAIR principles are achieved. To check it out, simply click on the file and go through the text.
-   `fdo_examples_basic.ipynb`: Short illustration of what FDOs can enable within BioDT, developed as an example for the MS26 milestone. To be further extended with more content (e.g. an RO-Crate example for collection records).
-   `fdo_definitions.py`: To support the previous notebooks, this contains some example class definitions of FAIR Digital Objects (FDOs) classes for BioDT. This will be further developed as the project progresses to reflect our understanding of how FDOs can function within BioDT.

### Usage

This repo contains mostly JSON metadata files and isolated Python scripts taken from other code repositories. Any relevant software dependencies needed to run such scripts can be installed using [Poetry](https://python-poetry.org/) (see `pyproject.toml`).

## License

[European Union Public Licence v. 1.2](https://eupl.eu/1.2/en/)
