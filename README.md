# Digital Curation Manager - IP Builder API

The 'DCM IP Builder'-API provides functionality to convert Intellectual Entities (IEs) into Information Packages (IPs) and validate IP-format (metadata and payload structure).
This repository contains the corresponding OpenAPI-document.
For the associated implementation, please refer to the sibling package [`dcm-ip-builder`](https://github.com/lzv-nrw/dcm-ip-builder).

The contents of this repository are part of the [`Digital Curation Manager`](https://github.com/lzv-nrw/digital-curation-manager).

## Building an SDK-package
Some dcm-applications rely on pre-built sdk-packages, i.e., python clients for specific APIs.

Consider using the corresponding packages available via the extra-index-url `https://zivgitlab.uni-muenster.de/api/v4/projects/9020/packages/pypi/simple`.
In order to manually build these packages, perform the following actions:

1. Get the OpenAPI Generator-archive, e.g., by running
   ```
   wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.5.0/openapi-generator-cli-7.5.0.jar -O openapi-generator-cli.jar
   ```
1. Create a JSON-file `config.json` with the package information
   ```json
   {
     "packageName": "dcm_ip_builder_sdk",
     "projectName": "dcm-ip-builder-sdk",
     "packageVersion": "<VERSION>"
   }
   ```
1. Run the generator
   ```
   java -jar ../openapi-generator-cli.jar generate -i dcm_ip_builder_api/openapi.yaml -g python -o sdk -c config.json
   ```
1. Apply available patches by running
   ```
   /bin/bash apply_patch.sh sdk/dcm_ip_builder_sdk
   ```

# Contributors
* Sven Haubold
* Orestis Kazasidis
* Stephan Lenartz
* Kayhan Ogan
* Michael Rahier
* Steffen Richters-Finger
* Malte Windrath
* Roman Kudinov