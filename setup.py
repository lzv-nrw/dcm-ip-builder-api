import os
from setuptools import setup

setup(
    version="3.1.0",
    name="dcm-ip-builder-api",
    description="api for ip-builder-containers",
    author="LZV.nrw",
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
