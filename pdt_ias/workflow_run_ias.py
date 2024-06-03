"""
workflow_run_ias.py

Simple script to showcase the generation of an RO-Crate metadata file from Python code, with a higher granularity.
 This (mock) metadata file is centered around a specific workflow. In this case, there is a distinction between the
 conceptual workflow and the specific instances/executions. For example, at the conceptual level:
 - Workflow: Pydoit actions about feedback loops for corine data source (`Corine_feedbackloop_workflow.py`)
 - Input: Latest Corine dataset metadata/logfiles, in JSON format...
 - Output: Newer (if available) version of the Corine dataset, composed of a set of GeoTIFF images...

 While, at the execution level:
 - Action: #workflowrun-5a5970ab... (specific execution of `Corine_feedbackloop_workflow.py`).
 - Object: "/logs/feedback/corine", the latest instance of the Corine metadata file
 - Result: A link to the newly generated dataset

"""

from rocrate.rocrate import ROCrate
from rocrate.model import DataEntity, ContextEntity, Person
import datetime

# The "crate" is where we add all the elements we want to describe (the model, data sources, outputs...)
crate = ROCrate()

# Each entity will have its own entry, where details can be added
workflow = crate.add(DataEntity(crate, identifier="Corine_feedbackloop_workflow.py", properties={
    "@type": ["File", "SoftwareSourceCode", "ComputationalWorkflow"],
    "name": "Pydoit actions about feedback loops for corine data source",
}))

# Inputs and outputs
workflowInput = crate.add(ContextEntity(crate, identifier="#Corine_land_cover_metadata", properties={
    "@type": "FormalParameter",
    "additionalType": "File",
    "name": "Corine dataset metadata",
    "description": "Corine dataset metadata from the logs folder, needed to be compared against the latest one from "
                   "the CLMS API for recency",
    "encodingFormat": "application/json",
    "valueRequired": "False"
}))
workflow.append_to("input", workflowInput)

workflowOutput = crate.add(ContextEntity(crate, identifier="#Corine_land_cover_dataset", properties={
    "@type": "FormalParameter",
    "additionalType": "Dataset",
    "name": "CORINE Land Cover 2018 (vector/raster 100 m), Europe, 6-yearly",
    "description": "Provides pan-European CORINE Land Cover inventory for 44 thematic classes for..."

}))
workflow.append_to("output", workflowOutput)

# Contextual entities
author = crate.add(Person(crate, identifier="https://orcid.org/0000-0001-7833-5474", properties={
    "name": "Taimur Khan"
}))
workflow.append_to("creator", author)

programmingLanguage = crate.add(
    ContextEntity(crate, identifier="https://www.python.org/downloads/release/python-3123/", properties={
        "@type": "ComputerLanguage",
        "name": "Python 3.12.3",
        "url": "https://www.python.org/",
        "version": "3.12.3"
    }))
workflow.append_to("programmingLanguage", programmingLanguage)

# Now, we can add the instances of the previous things
action = crate.add(DataEntity(crate, identifier="#workflowrun-5a5970ab...", properties={
    "@type": "CreateAction",
    "name": "Corina feedback loop workflow run 5a5970ab..."
    # })).append_to("endTime", str(datetime.datetime.now()), "instrument", workflow)
}))
action.append_to("endTime", str(datetime.datetime.now()))
action.append_to("instrument", workflow)

metadata_file = crate.add(DataEntity(crate, identifier="/logs/feedback/corine", properties={
    "@type": "File",
    "description": "Latest metadata file from the logs folder about the Corine land cover dataset",
    "encodingFormat": "application/json"
}))
metadata_file.append_to("exampleOfWork", workflowInput)
workflowInput.append_to("workExample", metadata_file)
action.append_to("object", metadata_file)

updated_dataset = crate.add(DataEntity(crate, identifier="#Link-to-data-storage", properties={
    "@type": "Dataset",
    "description": "Latest/updated data from the Corine land cover dataset",
    "encodingFormat": "image/tiff"
}))
updated_dataset.append_to("exampleOfWork", workflowOutput)
workflowOutput.append_to("workExample", updated_dataset)
action.append_to("result", updated_dataset)

# Lastly, we can also add the profiles, licenses, and any other relevant information about the crate
profiles = [
    crate.add(ContextEntity(crate, identifier="https://w3id.org/ro/wfrun/process/0.4", properties={
        "@type": "CreativeWork",
        "name": "Process Run Crate",
        "version": "0.4"
    })),
    crate.add(ContextEntity(crate, identifier="https://w3id.org/ro/wfrun/workflow/0.4", properties={
        "@type": "CreativeWork",
        "name": "Workflow Run Crate",
        "version": "0.4"
    })),
    crate.add(ContextEntity(crate, identifier="https://w3id.org/workflowhub/workflow-ro-crate/1.0", properties={
        "@type": "CreativeWork",
        "name": "Workflow RO-Crate",
        "version": "1.0"
    })),
    crate.add(ContextEntity(crate, identifier="https://w3id.org/workflowhub/workflow-ro-crate/1.0", properties={
        "@type": "CreativeWork",
        "name": "Workflow RO-Crate",
        "version": "1.0"
    }))
]
crate.name = "Feedback Loop for Corine data source"
crate.metadata.append_to("conformsTo", profiles[2])
crate.root_dataset.append_to("conformsTo", profiles)
crate.root_dataset.append_to("mainEntity", workflow)
crate.root_dataset.append_to("mentions", action)

# This can be written as a json file
crate.write("./workflow_run_rocrate_IAS.json")
