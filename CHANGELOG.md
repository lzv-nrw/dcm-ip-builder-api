# Changelog

## [6.2.0] - 2025-12-05

### Added

- introduced BagIt-profile store to give control over accepted profiles for validation

## [6.1.0] - 2025-11-04

### Added

- added IP-/Bag-Info-metadata to the report of a validation-job

## [6.0.0] - 2025-09-09

### Changed

- **Breaking:** updated `SelfDescription`-schema regarding new `orchestra`-package of `dcm-common`

### Removed

- **Breaking:** removed obsolete broadcast- & requeue-options in abort

## [5.1.0] - 2025-08-20

### Added

- added optional submission token

## [5.0.0] - 2025-07-25

### Added

- **Breaking:** added `requestType` to `JobData`-schemas for better sdk-support
- added IP-identifiers to `JobData`-schemas (to be collected from source metadata)
- added `build.validation` option to build-requests

### Removed

- removed unused sdk-patch mechanism
- dropped property `BuildJobData.build_plugin` (replaced by `requestType`)
- dropped property `SelfDescription.configuration.build.do_validation`

## [4.0.0] - 2025-02-13

### Changed

- **Breaking:** replace `build.configuration` by `mappingPlugin` (in `POST-/build`-requestBody)
- **Breaking:** migrated to plugin-system for validation-requests
- **Breaking:** renamed `validate/ip` endpoint to `validate`

### Added

- added sdk-patch mechanism

### Removed

- **Breaking:** removed `dcm-object-validator` dependency

## [3.1.1] - 2024-11-21

### Changed

- updated package metadata and README

## [3.1.0] - 2024-10-11

### Added

- added /build- and /validation-DELETE endpoints for abort mechanism 

## [3.0.0] - 2024-09-05

### Changed

- **Breaking:** update SelfDescription for scalable orchestration (`498703c1`)
- **Breaking:** rename JobToken field 'token' to 'value' (`2a2bdff7`)

## [2.1.0] - 2024-07-19

### Changed

- added field `do_validation` to `SelfDescription.configuration.settings.build` (`e130d836`)

### Fixed

- fixed format of `SelfDescription.configuration.settings.validation.object_validator_timeout` (`51de6fce`)
- fixed name and description of `metadata_plugins` in `SelfDescription.configuration.settings.validation` (`b2441034`)

## [2.0.0] - 2024-07-17

### Changed

- **Breaking:** refactored /identify-GET response to common DCM-format (`e54a8c6d`)
- **Breaking:** removed requirement for `JobData.valid` (`b65fa422`)

## [1.0.0] - 2024-04-25

### Changed

- **Breaking:** renamed schema `DateTime` to `ISODateTime` (reserved by swagger codegen) (`c24766bc`)
- **Breaking:** termination callback body now contains entire JobToken (`97f273c8`)
- **Breaking:** changed requestBody format for job submissions (`a08cdb95`, `cf535749`)
- **Breaking:** renamed validation endpoint  (`1acbcfd6`)
- **Breaking:** improved Report schema, now supports custom job output data format and Reports of child processes (`4de52936`, `ce52a33f`, `2b3cc186`, `c0147e40`)
- made "path" in BuildJobData schema optional (`db8ba581`)
- **Breaking:** migrated to OpenAPI-generator for SDK generation (`bd776ff9`)

## [0.3.0] - 2024-01-25

### Added

- added metadata-mapper-package availability and version to /identify-GET endpoint (`c1f60f1e`)
- added extra html response status codes (`9463f7f5`)

### Fixed

- update with the specifications for the configuration property (`1f4e92d2`)
- fixed the list of required properties in schemata (`552ece4d`)
- update descriptions regarding validation (`77859b51`)
- fix externalDocs url, now points to correct project (`6f225273`)

## [0.1.0] - 2024-01-18

### Changed

- initial release of dcm-ip-builder-api
