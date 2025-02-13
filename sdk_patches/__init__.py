
from .ambiguous_job_data_schema import ambiguous_job_data_schema


def patch(sdk):
    ambiguous_job_data_schema(sdk)
