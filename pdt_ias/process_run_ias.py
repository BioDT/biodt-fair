"""
process_run_ias.py

Simple script to showcase the generation of an RO-Crate metadata file from Python code.
 This (mock) metadata file is centered around a specific action (i.e., executing the model with `$ singularity run ...`)
 and links together the different components involved:
 - The model/software used.
 - The data sources and parameters needed for execution.
 - The resulting output from the execution.
 - Other entities such as the author, metadata profiles, etc...

"""

from rocrate.rocrate import ROCrate
from rocrate.model import DataEntity, ContextEntity, Person
import datetime

# The "crate" is where we add all the elements we want to describe (the model, data sources, outputs...)
crate = ROCrate()

# Each entity will have its own entry, where details can be added
workflow = crate.add(DataEntity(crate, identifier="#create_IAS_grid", properties={
    "@type": "CreateAction",
    "name": "Produce grid map of predicted IAS",
    "description": "singularity run --bind \"$PWD\" iasdt-modelling-containers_0.0.1.sif"
    # Other properties are possible, like...
    # "startTime": "",
    # "containerImage": "",
    # "actionStatus": "FailedActionStatus",
    # "error": "Traceback (most recent call last):\n  File \"<stdin>\", line 4, in <module>\nRuntimeError"
}))
# We can also update an entity's properties based on the execution of other parts of the code
workflow.append_to("endTime", str(datetime.datetime.now()))

# We can capture the relations between entities. Like what input, model, parameters, etc, have been used for a
# specific workflow, and what are its results.

# First, we define those entities
model = crate.add(DataEntity(crate, identifier="#IAS-pDT-Model", properties={
    "@type": "SoftwareApplication",
    "url": "https://git.ufz.de/biodt/IASDT.R",
    "name": "Invasive Alien Species Prototype Digital Twin",
    "softwareVersion": "0.1.0"
    # "softwareRequirements": ""
}))
# Then, we make the connection. In this case, the model has been added as the "instrument" of the workflow
workflow.append_to("instrument", model)

dataSource1 = crate.add(DataEntity(crate, identifier="#Species_observations", properties={
    "@type": "Dataset",
    "name": "European Alien Species Information Network (EASIN)",
    "description": "EASIN provides spatial data on 14,000 alien species..."
}))
dataSource2 = crate.add(DataEntity(crate, identifier="#Corine_land_cover", properties={
    "@type": "Dataset",
    "name": "..."
}))
dataSource3 = crate.add(DataEntity(crate, identifier="#Railway_intensity", properties={
    "@type": "Dataset",
    "name": "..."
}))
workflow.append_to("object", [dataSource1, dataSource2, dataSource3])

environmentVariables = crate.add(ContextEntity(crate, identifier="#grid_size_param", properties={
    "@type": "PropertyValue",
    "name": "DP_R_CHELSA_Gridsize",
    "value": "10"
}))
workflow.append_to("environment", environmentVariables)

output = crate.add(DataEntity(crate, identifier="#IAS_Grid_map", properties={
    "@type": "File",
    "name": "Gridded IAS number per habitat type",
    "description": "NetCDF file with the number of invasive alien species per habitat type, shown in a grid according "
                   "to the reference...",
    "encodingFormat": "application/netcdf"
}))
workflow.append_to("result", output)

author = crate.add(Person(crate, identifier="https://orcid.org/0000-0001-7833-5474", properties={
    "name": "Taimur Khan"
}))
workflow.append_to("agent", author)

profile = crate.add(ContextEntity(crate, identifier="https://w3id.org/ro/wfrun/process/0.4", properties={
    "@type": "CreativeWork",
    "name": "Process Run Crate",
    "version": "0.4"
}))

# We can also add information about the crate itself (represented by the "root dataset")
crate.name = "IAS pDT model/dashboard execution #?"
crate.root_dataset.append_to("mentions", workflow)
crate.root_dataset.append_to("conformsTo", profile)

# This can be written to disk as a json file
crate.write("./process_run_rocrate_IAS.json")
