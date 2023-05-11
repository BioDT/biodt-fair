"""
This file contains some Python examples of FAIR Digital Objects (FDOs) classes for the BioDT project.
"""

import json


class FDO:
    """
    Base class for representing FAIR Digital Objects (FDOs). It contains the fundamental properties and methods all FDOs should have.
    """

    def __init__(self, fdoProfile, fdoRecordLicense, digitalObjectType, digitalObjectName, pid):
        self.fdoProfile = fdoProfile
        self.fdoRecordLicense = fdoRecordLicense
        self.digitalObjectType = digitalObjectType
        self.digitalObjectName = digitalObjectName
        self.pid = pid

    def __iter__(self):
        """Returns an iterator object for the object."""

        for attr, value in self.__dict__.items():
            yield attr, value

    def __eq__(self, other):
        """Checks if two objects are equal."""

        return self.pid == other.pid


class DiSSCoFDO(FDO):
    """
    Class for representing DiSSCo FDOs. It extends the base class FDO and adds some DiSSCo specific properties.
    """

    def __init__(self, pid):
        super().__init__("https://hdl.handle.net/21.T11148/d8de0819e144e4096645",
                         "https://creativecommons.org/publicdomain/zero/1.0/",
                         "https://hdl.handle.net/21.T11148/894b1e6cad57e921764e", "digitalSpecimen", pid)
        self.referentName = "Sorex araneus"
        self.specimenHost = "https://ror.org/05xg72x27"
        self.specimenHostName = "Norwegian University of Science and Technology"

    @staticmethod
    def get_fdo_type():
        """Returns the FDO type definition."""

        # Open the JSON file that contains the FDO type definition
        with open('data/dissco_fdo_type.json') as json_file:
            return json.load(json_file)
