# Recording Lifecycle Auditor — Draft Contract

- Date: 1405-07-04
- Calendar: Jalali (Solar Hijri), YYYY-MM-DD
- Status: Practiced draft; not implemented or executed

## Purpose and scope

Inspect the lifecycle of requested recordings and determine whether each recording was created, finalized, stored in the location configured by the environment, and playable after saving.

This first version ends at successful saving and playback. Upload, retry, and deletion behavior are outside its scope.

## Required inputs and dependencies

- Recording identifier.
- Lifecycle logs or records covering creation and finalization, with statuses and timestamps.
- Expected save location from environment configuration.
- Actual saved-file path and file metadata.
- Permission to inspect the saved file.
- An approved media-inspection tool for a non-modifying decode or playback check.

The media-inspection tool is a dependency, not source evidence. Missing evidence must not be invented.

## Workflow

1. Validate the recording ID, lifecycle records, configured save location, file access, and media-inspection capability.
2. Filter lifecycle records by the requested recording ID.
3. Order the records by timestamp and evaluate creation and finalization independently.
4. Resolve the expected file path from configuration and recording data.
5. Check whether the file exists and whether basic metadata, such as file size, is plausible.
6. When the file exists, inspect or decode it without modifying it.
7. Report each stage, its supporting evidence, and uncertainty independently.

These workflow steps were consolidated with substantial coaching and do not yet demonstrate independent workflow authoring.

## Safety constraints

- Do not modify or delete recordings.
- Do not expose full sensitive paths, credentials, access tokens, or unnecessary video contents in reports.
- Use a recording ID, filename, redacted path, safe relative path, or sanitized playback URL when evidence must be identified.

The learner independently supplied the first two core safety boundaries; reporting refinements were coach-provided.

## Expected output

For each requested recording, report:

- overall result;
- separate creation, finalization, storage, and playability results;
- evidence supporting each result; and
- missing evidence, uncertainty, or checks that could not be performed.

One stage must not substitute for another. For example, a playable file does not prove that a finalization event was recorded.

## Evaluation cases

### Case 1 — Complete successful lifecycle

- Situation: Creation and finalization events exist, the file exists at the configured location, and media inspection succeeds.
- Expected stages: Creation Passed; Finalization Passed; Storage Passed; Playability Passed.
- Expected overall result: Passed.
- Safety: Report only safe references; do not modify the file or expose secrets.

### Case 2 — Stored but corrupted

- Situation: Creation and finalization events exist and the file exists, but media inspection cannot decode or play it.
- Expected stages: Creation Passed; Finalization Passed; Storage Passed; Playability Failed.
- Expected overall result: Failed.
- Safety: Report the inspection failure without modifying, repairing, or deleting the file.

### Case 3 — Missing finalization evidence

- Situation: A creation event exists, no finalization event is available, and the correctly located file is playable.
- Expected stages: Creation Passed; Finalization Unknown/Unverified; Storage Passed; Playability Passed.
- Expected overall result: Failed or Incomplete under the contract's requirement for complete lifecycle evidence.
- Finding: Report missing or unavailable finalization evidence and recommend investigation; do not claim a specific defect without supporting evidence.

The scenarios and conclusions were completed through guided practice. Independent transfer remains to be assessed before this contract is treated as demonstrated.
