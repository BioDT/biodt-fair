# BioDT - FAIR tutorials and materials
This repository hosts some materials concerning the FAIR aspect of the data, software, and other digital objects within the Biodiversity Digital Twin (BioDT) project. While that mostly concerns WP5, other work packages and prototype digital twin teams (pDTs) can also find useful information here. So far, the Confluence wiki has remained as the main tool for collaboration, but this repository is meant to complement it with more technical information and tools, as well as open visibility for the wider community. 

## Content
### `examples/` directory
Currently, there is only a couple of Jupyter Notebook examples: 
- `dataset_ro-crate.ipynb`: It goes over how to turn an existing dataset into an RO-Crate, with descriptions on the main elements of RO-Crate and how some FAIR principles are achieved. To check it out, simply click on the file and go through the text.
- `fdo_examples_basic.ipynb`: Short illustration of what FDOs can enable within BioDT, developed as an example for the MS26 milestone. To be further extended with more content (e.g. an RO-Crate example for collection records).

To support the previous notebooks, there is another Python file with a very preliminary definition of an FDO. This will be further developed as the project progresses to reflect our understanding of how FDOs can function within BioDT.
- `fdo_definitions.py`: Example class definitions of FAIR Digital Objects (FDOs) classes for the BioDT project.

### Prototype Digital Twin (pDT) directories
Each pDT has its own directory, where we will store the materials related to the FAIR aspects of the pDT. For example, the metadata descriptions for the digital objects in development. Currently, we have the following pDTs:
- `pdt_ces/`: Prototype Digital Twin for Cultural Ecosystem Services (CES).
- `pdt_ias/`: Prototype Digital Twin for Invasive Alien Species (IAS).
- `pdt_rtbm/`: Prototype Digital Twin for Real-Time Bird Monitoring.
- `pdt_beehave/`: Prototype Digital Twin for Pollinators (using the [BEEHAVE model](https://beehave-model.net/)).

### `fdo_profiles/` directory
In this folder, we will store the profiles for the different FDO types that we will use in BioDT. Such profiles are expected to evolve over the course of the project, just like the format in which they will be presented. Currently, the following files populate this directory:
- `ro-crate_model_template.json`: an empty RO-Crate (hence "template") with the metadata attributes for BioDT models, as specified here. This can be used as a starting point to create new RO-Crates for BioDT models.
- `crate-o_model_profile.json`: a profile specification file following the format of [Crate-O](https://github.com/Language-Research-Technology/crate-o), containing the same attributes as discussed in the previous point.

## Other parts of the repository
This repository also hosts other tools helpful for collaboration. Although most sections don't have much content yet, their purpose is as follows:
- The [BioDT FAIR Roadmap](https://github.com/orgs/BioDT/projects/1): a planning tool in the Project tab where important tasks that are planned or actively being worked on are displayed. This is a good place to check what is going on in the FAIR side of BioDT.
- The [Issues](https://github.com/BioDT/biodt-fair/issues) and [Pull requests](https://github.com/BioDT/biodt-fair/pulls) tabs: as usual for any code git repository, this is aimed at collaborating in the development of the materials in this repository. 
- The [Discussions](https://github.com/BioDT/biodt-fair/discussions) tab: for topics that require interaction from other members of the project, such as feedback and alignment on the metadata profiles, etc.
- The [Wiki](https://github.com/BioDT/biodt-fair/wiki) tab: for more general information about the FAIR aspects of BioDT, such as previous decisions made in the project. This used to take place in the Confluence wiki, but the goal is to have here content related to FAIR for its usefulness beyond the BioDT project and for the wider community.

## License
[MIT](https://choosealicense.com/licenses/mit/)
