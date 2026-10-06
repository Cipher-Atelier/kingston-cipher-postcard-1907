# Read this investigation

[Repository overview](README.md) · [Technical verification](verification/README.md)

## Understand the document

A personal cipher postcard dated 8 December 1907, catalogued as HCP1193. Its geometric symbols can be related to letter positions on a grid.

Start with the [source catalogue or manuscript](https://crypto.hcportal.eu/dashboard/cryptograms/1193). It identifies the historical object. The source image is the evidence; the tables in this repository are recorded readings of that evidence.

## Read the current result

The proposed English reading addresses Helen, mentions an expected letter that has not arrived, and expresses affection. It assigns letters at 213 of 222 cipher positions; the remaining signs and some ordinary handwriting are unresolved.

Open [Literal postcard reading](verification/readings/evidence/HCP1193_Verified_Reading/literal_reading.txt) and the [research account](kingston-1907/README.md). A literal preserves the recorded output before making it smoother to read. An English explanation or translation adds interpretation and should not silently repair it.

Example:

```text
well helen my [27] i did
```

[27] is an unexplained symbol position in the proposed key, not a decoded number or a recovered word.

213/222 measures how many cipher positions receive a letter under the recorded rules. It is not a 95.9% correctness score. The German-like phrase, sign 27 and closing wording remain unresolved; the writer’s identity is not established by this reading.

## Check one example by hand

1. Open the [position table](verification/readings/evidence/HCP1193_Verified_Reading/transcription_and_reading.tsv) and the [key](verification/readings/evidence/HCP1193_Verified_Reading/geometry_key.json). A position such as `r01c01` means row 1, cipher position 1 within that row. Shape labels identify recorded geometric classes.

| Position | Recorded class | Output |
| --- | --- | --- |
| `r01c01` | `TLBR3` | `w` |
| `r01c02` | `TLBR1` | `e` |
| `r01c12` | `TL3` | `[27]` |

2. The first two assignments give `we`; the full first row begins `well helen my [27] i did`. `TL3` has `null` in the key, meaning no established letter value. The replay preserves it as `[27]`.
3. Compare these shapes with the [original cipher-side image](https://api.hcportal.eu/media/3639/cpc_1907-12-08_USA_Kingston,-NY_USA_New-York__pic.jpg). Do not infer an unclear shape merely because a particular letter would make an English word.

The table separates original and later reviewed source classes. A masked sign emits `?` even if another interpretation looks attractive. Ordinary handwriting fragments and the uncertain final region are separate from the 222-position cipher count.

## Choose the check you want

- **Understand the result:** read the literal/test result beside the research account. You can do this in GitHub without installing anything.
- **Check the calculation:** follow the example above, then [run the supported Python check](verification/README.md). This verifies the saved transformation or declared model.
- **Check the source:** compare recorded signs with the original image and retain disagreements. Scans/crops are not included; obtain access under the provider’s terms. Original coordinates, when present, refer to the specified image version.
- **Evaluate the historical reading:** examine alternative signs, key evidence, language, document boundaries and prior readings. A successful calculation does not settle these questions.

To report a problem, use [Work on existing research](https://github.com/Cipher-Atelier/kingston-cipher-postcard-1907/issues/new?template=research.yml). Give the file, row/position, source reference, your observation, and what changes in the output. Distinguish a different source reading from a changed key or an editorial interpretation.

## What the files mean

| Open this | It contains |
| --- | --- |
| [Research account](kingston-1907/README.md) | Historical context, method, interpretation, credits and limits |
| [Literal postcard reading](verification/readings/evidence/HCP1193_Verified_Reading/literal_reading.txt) | The saved text or bounded test result |
| [One row per cipher position](verification/readings/evidence/HCP1193_Verified_Reading/transcription_and_reading.tsv) | The recorded input/assignments used in the example |
| [Geometric symbol-to-letter key](verification/readings/evidence/HCP1193_Verified_Reading/geometry_key.json) | The proposed transformation, historical key, or tested assumptions |
| [Technical verification](verification/README.md) | Setup, command, expected output and what the check covers |
| [Source scope](verification/TOPIC_SCOPE_INDEX.json) | Machine-readable release boundaries and omitted material |
| [Publication provenance](SOURCE_PROVENANCE.json) | Where this package came from and what documentation changed |

CSV and TSV are tables: GitHub or a spreadsheet can display them. TSV uses tabs between columns. JSON stores named fields and lists; `null` means no value in that field, and its interpretation depends on the record. You do not need to start by reading every JSON file.

## Terms used in the research

- **Ciphertext:** the recorded encrypted signs or letters.
- **Key/mapping:** the rule assigning output to a cipher sign. It may be a hypothesis, a surviving historical key, or an assumption in a test; those are different kinds of evidence.
- **Literal reading:** the saved output with gaps and awkward wording retained, before editorial translation or repair.
- **Coverage:** how many recorded positions receive a value. It does not measure how many values are historically correct.
- **Frozen:** saved unchanged at a particular stage so a later correction cannot replace an earlier test result.
- **Replay:** applying saved rules to saved inputs again. It checks reproducibility within the declared scope.
- **Training/heldout:** material used to fit a rule, and material excluded from that fitting. Prior viewing or later correction can limit how independent a heldout test is; read the case-specific account.
