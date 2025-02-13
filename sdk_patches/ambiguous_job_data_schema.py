import sys


def ambiguous_job_data_schema(sdk):
    """
    IP Builder SDK - "Multiple matches" for JobData-schemas

    sdk-patch required to mitigate problems with deserialization of
    JobData-variants: since the sdk ignores unknown input, an incomplete
    (but valid) BuildJobData-object (e.g., missing 'path') is falsely
    deemed a correct ValidationJobData-object (although 'build_plugin'
    is present)
    """

    print(
        "\033[0;31mRUNNING IPB-SDK-PATCH 'ambiguous_job_data_schema'\033[0m",
        file=sys.stderr,
    )

    unpatched_from_dict = (
        sdk.models.validation_job_data.ValidationJobData.from_dict
    )

    class PatchedValidationJobData(
        sdk.models.validation_job_data.ValidationJobData
    ):
        """Patched `ValidationJobData`-model."""

        @classmethod
        def from_dict(cls, obj):
            """Patched `from_dict` that does not accept unknown keys."""
            if any(
                key not in ["valid", "success", "details"]
                for key in obj.keys()
            ):
                return None

            return unpatched_from_dict(obj)

    sdk.models.validation_job_data.ValidationJobData.from_dict = (
        PatchedValidationJobData.from_dict
    )
