# BioDT - FAIR tutorials and materials
This repository hosts some materials concerning the FAIR aspect of the data, software, and other digital objects within the [Biodiversity Digital Twin (BioDT) project](https://cordis.europa.eu/project/id/101057437). While that mostly concerns WP5, other work packages and prototype digital twin teams (pDTs) can also find useful information here. While the [Confluence wiki](https://wiki.eduuni.fi/display/cscRDIcollaboration/BioDT?src=contextnavpagetreemode) remains as the main tool for collaboration within the project, this repository is meant to complement it with more technical information and tools, as well as open visibility for the wider community. 

## Content

### Prototype Digital Twin (pDT) directories
Each pDT has its own directory, where we will store the materials related to the FAIR aspects of the pDT. For example, the metadata descriptions for the digital objects in development. Currently, we have the following pDTs:
- `pdt_beehave/`: Prototype Digital Twin for Pollinators (using the [BEEHAVE model](https://beehave-model.net/)).
- `pdt_ces/`: Prototype Digital Twin for Cultural Ecosystem Services (CES).
- `pdt_cwr/`: Prototype Digital Twin for Crop Wild Relatives (CWR)
- `pdt_ias/`: Prototype Digital Twin for Invasive Alien Species (IAS).
- `pdt_rtbm/`: Prototype Digital Twin for Real-Time Bird Monitoring (RTBM).

### `fdo_profiles/` directory
In this folder, we will store the metadata profiles (and related materials) that we will use in BioDT. This is closely related to the FAIR Digital Objects (FDO) and RO-Crate frameworks. Such profiles are expected to evolve over the course of the project. So far, the profile work has been focused on:
- Kernel attributes: this is about the attributes that apply to all digital objects in BioDT, regardless of their purpose. It covers fundamental metadata such as IDs, type, author, license...
- Model attributes: the `models/` subdirectory covers the metadata for the main software from each pDT.
- Dataset attributes: the `datasets/` subdirectory includes the profiles for the different types of data used in BioDT.
- Workflow attributes: the `workflows/` subdirectory focuses on the elements that bring everything together (connecting the data to the models, sending jobs to HPC, etc).
- Additionally, other auxiliary resources can be found in the `other/` directory.

### `examples/` directory
This directory contains some materials that have been developed mainly for illustrative purposes. For example: 
- `leipzig_workshop/`: This subdirectory contains a Jupyter notebook and some metadata files used during the BioDT workshop in Leipzig, Nov 2023. It aims to give an introduction to FAIR and RO-Crate in the context of data for BioDT. 
- `dataset_ro-crate.ipynb`: It goes over how to turn an existing dataset into an RO-Crate, with descriptions on the main elements of RO-Crate and how some FAIR principles are achieved. To check it out, simply click on the file and go through the text.
- `fdo_examples_basic.ipynb`: Short illustration of what FDOs can enable within BioDT, developed as an example for the MS26 milestone. To be further extended with more content (e.g. an RO-Crate example for collection records).
- `fdo_definitions.py`: To support the previous notebooks, this contains some example class definitions of FAIR Digital Objects (FDOs) classes for BioDT. This will be further developed as the project progresses to reflect our understanding of how FDOs can function within BioDT.

## Other parts of the repository
This repository also hosts other tools helpful for collaboration. Although most sections don't have much content yet, their purpose is as follows:
- The [BioDT FAIR Roadmap](https://github.com/orgs/BioDT/projects/1): a planning tool in the Project tab where important tasks that are planned or actively being worked on are displayed. This is a good place to check what is going on in the FAIR side of BioDT.
- The [Issues](https://github.com/BioDT/biodt-fair/issues) and [Pull requests](https://github.com/BioDT/biodt-fair/pulls) tabs: as usual for any code git repository, this is aimed at collaborating in the development of the materials in this repository. 
- The [Discussions](https://github.com/BioDT/biodt-fair/discussions) tab: for topics that require interaction from other members of the project, such as feedback and alignment on the metadata profiles, etc.
- The [Wiki](https://github.com/BioDT/biodt-fair/wiki) tab: for more general information about the FAIR aspects of BioDT, such as previous decisions made in the project. This used to take place in the Confluence wiki, but the goal is to have here content related to FAIR for its usefulness beyond the BioDT project and for the wider community.

## License
[MIT](https://choosealicense.com/licenses/mit/)
