# Kingston HCP1193: geometry checks, 8–9 October 2026

The one-side error model produced no unique new reading. A subsequent visual audit preserved unresolved alternatives. A new local connectivity test then supported a bounded geometric observation at r12c12: the long lower stroke and central slanted stroke connect within the tested region, while the selected upper and left strokes do not connect to that group at the two admitted thresholds. No new letter was accepted.

## Source and public baseline

The [HCP1193 catalogue](https://crypto.hcportal.eu/dashboard/cryptograms/1193) and [cipher-side JPEG](https://api.hcportal.eu/media/3639/cpc_1907-12-08_USA_Kingston,-NY_USA_New-York__pic.jpg) identify the source. The local JPEG is 3468 × 2298 RGB, SHA256 `d2f76e4e4d387fad96727d2b7be65704709753c43f5b4a9257b8c87a42d5e617`. It carries the HCPortal watermark; these bytes are not established as a new or better museum scan. Images and crops remain outside this publication.

The fixed key and transcription were taken from the [public record at commit eea4c98](https://github.com/Cipher-Atelier/kingston-cipher-postcard-1907/tree/eea4c98284934af70a5f399e441cbf93c2f27574/verification/readings). Its 213 mapped positions, eight unresolved masks and unexplained slot [27] remain unchanged. Coverage is not historical accuracy.

## 8 October: finite error model and visual audit

The model enumerated fixed-key classes at side-set distance zero or one, with the modifier held fixed. Every supported unknown position had multiple candidates; the position with unknown modifier was outside the main model. Of 104 synthetic single-side perturbations, 104 included the true class but zero identified it uniquely. This truth inclusion follows from the radius definition and checks implementation, not handwriting accuracy. Even intact classes had multiple candidates under the error allowance. The previously known text had been seen, so this was retrospective rather than a blind holdout.

Two separately tasked AI readers then inspected nine source regions with neutral labels, without the key or each other's responses. Their alternatives were retained rather than converted into accepted letters. Both supported TL3 geometry for the unexplained slot, but its meaning remained open. At r12c12, right and lower strokes were visible; ownership of upper/left strokes and neighboring sign boundaries remained uncertain. Several other regions retained faded strokes or disagreement between modifiers 2 and 3. The coordinator had seen the earlier reading; this was limited-input AI review, not independent human palaeography.

## 9 October: local pixel connectivity

The frozen region was `[1935,1880,2160,2010]` in the source JPEG. The method used Pillow grayscale, inclusive thresholds 80/100/120/140/160/180, eight-neighbor connectivity, and deterministic seed snapping within three original pixels. It used no smoothing, morphology or repair. Coordinates were adjusted during source-only inspection before review and scoring; they were unchanged after results.

Eight control pairs elsewhere in the same JPEG comprised four visibly joined and four visibly separated pairs. A fresh AI reader assessed their labels without the target or key. Four pairs were calibration controls and four were checks. Some controls shared glyphs within the same split; these are not eight independent historical samples.

| Threshold | Calibration supported/correct | Check supported/correct | Admitted |
| --- | ---: | ---: | --- |
| 80 | 0/4 | 0/4 | No |
| 100 | 1/4 | 1/4 | No |
| 120 | 2/4 | 1/4 | No |
| 140 | 4/4 | 3/4 | No |
| 160 | 4/4 | 4/4 | Yes |
| 180 | 4/4 | 4/4 | Yes |

The target did not select thresholds. At both admitted thresholds:

- J1, lower stroke `[2040,1980]` to central slanted stroke `[2088,1929]`: connected.
- J2, upper stroke `[2030,1911]` to central stroke: disconnected within the region.
- J3, left stroke `[1977,1940]` to lower stroke: disconnected within the region.

All admitted target seeds were already dark pixels. At 160, the J1 component contained 2480 pixels and the measured target components did not touch the region boundary. At 180, J1 contained 2995 pixels and touched the boundary, so the negative connectivity finding is particularly limited by the crop at that threshold.

## Interpretation and remaining work

This provides a reason to test the lower/central group in a later segmentation study. Connected JPEG pixels do not establish a historical cipher unit; gaps can reflect pen lifts, fading or lost weak lines. Paths outside the region, all neighboring boundaries and modifier ownership remain untested. BR3, TLBR3 and any corresponding letter remain hypotheses.

The next task is independent source review of neighboring sign boundaries and modifiers. A source copy with real additional detail could help resolve weak strokes; enlarged versions of these bytes cannot do so. These results do not rule out other error models or decipherment procedures.

## Publication checks and access limits

This publication pass checked saved control qualification and target outcomes against the local report. It did not rerun the image analysis or regenerate visual readings. The retained research record reports nine connectivity tests and a portable replay matching 90 output files; that is procedural reproducibility, not historical validation.

Local record identifiers (bytes retained privately):

- One-side report SHA256: `0a30bca67af4e1b0584b8454464856e280fa03d5e927fba6807af1948ab9bcea`.
- Visual-audit report SHA256: `04104ef3561448cb3b7898a8dd5fb36945507ea811ecc52822cd94c395808962`.
- Connectivity report SHA256: `e945c2f946bc6d2a67aa455064787e6a184939de159d742fa01c5cf86d9d9e6d`.
- Connectivity results SHA256: `19560bcbdc039bea1a5723bd41e18f69fadb4a71d31c5441a8755771b46ed98f`.

This text-only update provides findings and limits. Full replay requires retained experiment code, metadata and image inputs, which are outside this update. No full-code publication or new licence is claimed. Codex assisted the analysis and summary; AI review is not human expert verification.
