import os
from setuptools import setup


setup(
    version="5.1.0",
    name="dcm-ip-builder-api",
    description="specification of the DCM IP Builder API",
    author="LZV.nrw",
    license="MIT",
    install_requires=[
    ],
    packages=[
        "dcm_ip_builder_api"
    ],
    package_data={
        "dcm_ip_builder_api": [
            "dcm_ip_builder_api/openapi.yaml",
        ],
    },
    include_package_data=True,
)
