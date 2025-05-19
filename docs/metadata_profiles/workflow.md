---
layout: default
title: "Workflow Attributes"
permalink: /metadata_profiles/workflow
---

Workflows might be one of the less intuitive FDOs and can be understood in different ways. Nonetheless, they play an important role in bringing the different components of a digital twin together in an automated way. The distinction between a software script and a workflow can be fuzzy, but it's likely that scripts are more prevalent (even if they are fulfilling the role of a workflow). We follow [RO-Crate's guidelines for distinguishing between scripts and workflows](https://www.researchobject.org/ro-crate/1.1/workflows.html#describing-scripts-and-workflows):

> Here are some indicators for when a script should be considered a _workflow_:
>
> - It performs a series of steps (_pipeline_)
> - The executed steps are mainly external tools or services
> - The main work is performed by the steps (script is not algorithmic)
> - The steps exchange data in a _dataflow_, typically file inputs/outputs
> - The script has well-defined _inputs_ and _outputs_, e.g. file arguments
>
> Here are some counter-indicators for when a script might **not** be a workflow:
>
> - The script contains mainly algorithms or logic
> - Data is exchanged out of bands, e.g. a SQL database
> - The script relies on a particular state of the system (e.g. appends existing files)
> - An interactive user interface that controls the actions

##### Computational Workflows

Following RO-Crate's guidelines, we are using [Bioschema's `ComputationalWorkflow`](https://bioschemas.org/profiles/ComputationalWorkflow/1.0-RELEASE) as the base profile for workflows. They include mandatory, recommended and optional attributes. From the mandatory ones, some of them are already part of the [Kernel Attributes](kernel). The remaining ones that are mandatory but exclusive to workflows are shown below.

RO-Crate requires alignment with `ComputationalWorkflow`, but it also extends it with some additional features in the [Workflow Profile](https://about.workflowhub.eu/Workflow-RO-Crate/). These are mostly specific to how the RO-Crate should be structured. Lastly, there are some more specialised profiles, like those from [Workflow Run RO-Crate](https://www.researchobject.org/workflow-run-crate/). These go beyond the general RO-Crate guidelines and include 3 separate profiles for capturing the provenance of an execution of a computational workflow with increasing granularity:

- [Process Run Crate](https://www.researchobject.org/workflow-run-crate/profiles/process_run_crate) can be used to describe the execution of one or more tools that contribute to the same computation;
- [**Workflow Run Crate**](https://www.researchobject.org/workflow-run-crate/profiles/workflow_run_crate) is similar to Process Run Crate, but assumes that the coordinated execution of the tools is driven by a `ComputationalWorkflow`;
- [Provenance Run Crate](https://www.researchobject.org/workflow-run-crate/profiles/provenance_run_crate) extends Workflow Run Crate with guidelines for describing the internal details of each step of the workflow.

From the previous three profiles, **Workflow Run Crate** is probably the right balance. **Process** doesn't necessarily align with the `ComputationalWorkflow`, while **Provenance** adds too much detailed and and might hinder implementation.

Moreover, the finer details of the workflow execution might need to be captured through the [LEXIS](https://portal.beta.lexis.tech/login) platform, which relies on [Apache Airflow](https://airflow.apache.org/). In order to achieve interoperability between the different workflow systems mentioned so far, we will use the [Common Workflow Language (CWL)](https://www.commonwl.org/) as a central translation point, since it is well supported in the RO-Crate ecosystem and also through different tools (see [`cwl-airflow`](https://github.com/Barski-lab/cwl-airflow) for a connector from CWL to Airflow).

## Workflow Attributes

Format: the name of each metadata attribute includes a link to [Schema.org](https://schema.org/) (or another vocabulary to which the property belongs), and is followed by a definition in the "Description" line. "Type" indicates the expected values for each property, while "Cardinality" specifies the amount and whether they are optional or mandatory. Lastly, additional remarks might be added as "Comments", and an example is given in the final line.

---

**[input](https://bioschemas.org/properties/input)**

- **Description:** An input required to use the computational workflow (eg. Excel spreadsheet, BAM file)
- **Type:** [FormalParameter](https://bioschemas.org/FormalParameter/)
- **Cardinality:** 1/many
- **Comments:** This could be a dataset, some files, or some parameters.
- **Example:** `{ "@type": "FormalParameter", "name": "filter_rrna", "dct:conformsTo": "https://bioschemas.org/profiles/FormalParameter/1.0-RELEASE", "valueRequired": true }`

---

**[output](https://bioschemas.org/properties/output)**

- **Description:** The result produced by the execution of the workflow.
- **Type:** [FormalParameter](https://bioschemas.org/FormalParameter/)
- **Cardinality:** 1/many
- **Comments:**
- **Example:** `{ "@type": "FormalParameter", "dct:conformsTo": "https://bioschemas.org/profiles/FormalParameter/1.0-RELEASE", "name": "x1" }`

---

**[version](http://schema.org/version)**

- **Description:** The version of the workflow instance.
- **Type:**
    - [Number](http://schema.org/Number)
    - [Text](http://schema.org/Text)
- **Cardinality:** 1/1
- **Comments:** It is advised to follow the [semantic versioning](https://semver.org/) guidelines.
- **Example:** `"version" : 1`

---

**[programmingLanguage](https://schema.org/programmingLanguage)**

- **Description:** The computer programming language the code is written in.
- **Type:**
    - [ComputerLanguage](http://schema.org/ComputerLanguage)
    - [Text](http://schema.org/Text)
- **Cardinality:** 1/many
- **Comments:**
- **Example:** `"programmingLanguage": "Galaxy"`

---

**[url](http://schema.org/url)**

- **Description:** Link to the repository or repositories where the un-compiled, human-readable code is located.
- **Type:** [URL](http://schema.org/URL)
- **Cardinality:** 1/1
- **Comments:**
- **Example:** `"url": "https://covid19.workflowhub.eu/workflows/10"`

---

**[sdPublisher](http://schema.org/sdPublisher)**

- **Description:** The host site for the ComputationalWorkflow.
- **Type:**
    - [Organization](http://schema.org/Organization)
    - [Person](http://schema.org/Person)
- **Cardinality:** 1/1
- **Comments:** Useful to make explicit the cases where the structured data is derived automatically from existing published content.
- **Example:** `"sdPublisher": ["https://www.workflowhub.eu"]`

---

Apart from the mandatory attributes above, the [`ComputationalWorkflow` profile](https://bioschemas.org/profiles/ComputationalWorkflow/1.0-RELEASE) from Bioschemas includes many other recommended and optional attributes that add further details. Likewise, the [Workflow Run Crate](https://www.researchobject.org/workflow-run-crate/profiles/workflow_run_crate) provide a more fitting profile for capturing the _execution_ of a workflow. We refer to the official profiles for those.

#### Example Metadata File (`ro-crate-metadata.json`)

Below you can find an example RO-Crate metadata file conforming to the workflow profile. An empty template metadata file is also available through [this link](https://github.com/BioDT/biodt-fair/blob/main/docs/metadata_profiles/examples/workflow_template_ro-crate.json).

```json
{
    "@context": ["https://w3id.org/ro/crate/1.1/context"],
    "@graph": [
        {
            "@type": "CreativeWork",
            "@id": "ro-crate-metadata.json",
            "about": {
                "@id": "./"
            },
            "conformsTo": {
                "@id": "https://w3id.org/ro/crate/1.1"
            }
        },
        {
            "@id": "https://github.com/uio-mana/CWR-Hackathon/tree/main/ModGP",
            "@type": "Dataset",
            "hasPart": [{ "@id": "ModGP.R" }]
        },
        {
            "@id": "ModGP.R",
            "@type": ["File", "SoftwareSourceCode", "ComputationalWorkflow"],
            "conformsTo": "https://bioschemas.org/profiles/ComputationalWorkflow/1.0-RELEASE",
            "name": "ModGP.R",
            "description": "BioDT CWR - ModGP",
            "dateCreated": "2023-01-23",
            "license": {
                "@id": "https://creativecommons.org/licenses/by/4.0/"
            },
            "creator": [
                {
                    "@id": "https://orcid.org/0000-0002-4984-7646"
                },
                {
                    "@id": "https://orcid.org/0000-0002-8045-6950"
                }
            ],
            "keywords": "SDM, crop wild relatives, genomics",
            "url": "https://github.com/uio-mana/CWR-Hackathon/blob/main/ModGP",
            "programmingLanguage": { "@id": "#R" },
            "version": "0.1.0",
            "sdPublisher": "#workflow-repo",
            "input": [
                {
                    "@id": "X - Functions-Data.R"
                },
                {
                    "@id": "X - Functions-Outputs.R"
                },
                {
                    "@id": "X - Functions-SDM.R"
                }
            ],
            "output": { "@id": "#Species distribution output" }
        },
        {
            "@id": "X - Functions-Data.R",
            "@type": ["File", "SoftwareSourceCode"],
            "name": "GBIF data download functionality",
            "description": "Bioclimativ Variable Climatology creation for qsoil1 anbd qsoil2 combined",
            "programmingLanguage": { "@id": "#R" }
        },
        {
            "@id": "X - Functions-Outputs.R",
            "@type": ["File", "SoftwareSourceCode"],
            "name": "SDM Output",
            "description": "SDM Output Visualisation and posthoc summaries",
            "programmingLanguage": { "@id": "#R" }
        },
        {
            "@id": "X - Functions-SDM.R",
            "@type": ["File", "SoftwareSourceCode"],
            "name": "Species Distribution Model (SDM)",
            "description": "SDM Functionality: Data Preparation and Model Execution",
            "programmingLanguage": { "@id": "#R" }
        },
        {
            "@id": "#Species distribution output",
            "@type": "Dataset",
            "name": "Lathyrus aphaca distribution",
            "description": "ModGP output for Lathyrus aphaca",
            "studySubject": ["http://eurovoc.europa.eu/632"]
        },
        {
            "@id": "#workflow-repo",
            "@type": "Organization",
            "name": "WorkflowHub space for BioDT CWR pDT",
            "url": "https://workflowhub.eu/projects/133"
        },
        {
            "@type": "Person",
            "@id": "https://orcid.org/0000-0002-8045-6950",
            "name": "Desalegn Chala Gelete",
            "affiliation": { "@id": "https://ror.org/01xtthb56" }
        },
        {
            "@id": "https://orcid.org/0000-0002-4984-7646",
            "@type": "Person",
            "name": "Erik Kusch",
            "affiliation": { "@id": "https://ror.org/01xtthb56" }
        },
        {
            "@id": "https://ror.org/01xtthb56",
            "@type": "Organization",
            "name": "University of Oslo",
            "url": "http://www.uio.no/english/"
        },
        {
            "@id": "#R",
            "@type": "ProgrammingLanguage",
            "name": "R",
            "url": "https://www.r-project.org/about.html",
            "version": "4.3.2"
        },
        {
            "@id": "https://creativecommons.org/licenses/by/4.0/",
            "@type": "CreativeWork",
            "name": "Creative Commons Attribution 4.0 International",
            "description": "You are free to:\nShare — copy and redistribute the material in any medium or format for any purpose, even commercially.\nAdapt — remix, transform, and build upon the material for any purpose, even commercially.\nThe licensor cannot revoke these freedoms as long as you follow the license terms."
        }
    ]
}
```
