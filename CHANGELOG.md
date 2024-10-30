# Changelog

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
