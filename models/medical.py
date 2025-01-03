"""
module medical: implements medical records - vaccinations, treatments
"""
from base_model import BaseModel


class MedicalRecord(BaseModel):
    """
    A medical record entry
    """
    name = None
    date_administered = None


class Vaccination(MedicalRecord):
    """
    A vaccination
    """
    dosage = 0


class Treatment(MedicalRecord):
    """
    A treatment for an ailment or disease
    """
    description = None
    