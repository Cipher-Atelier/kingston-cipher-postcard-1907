# Kingston cipher postcard (8 December 1907)

A personal cipher postcard dated 8 December 1907, catalogued as HCP1193. Its geometric symbols can be related to letter positions on a grid.

## What has been found?

The proposed English reading addresses Helen, mentions an expected letter that has not arrived, and expresses affection. It assigns letters at 213 of 222 cipher positions; the remaining signs and some ordinary handwriting are unresolved.

A small example from the recorded result:

```text
well helen my [27] i did
```

[27] is an unexplained symbol position in the proposed key, not a decoded number or a recovered word.

## Start reading

1. [Read the plain-language guide](READING_GUIDE.md): the document, result, file meanings and one worked check. No programming is required.
2. Open [Literal postcard reading](verification/readings/evidence/HCP1193_Verified_Reading/literal_reading.txt) to inspect the saved text or test result itself.
3. Read the [research account](kingston-1907/README.md) for historical context, methods, earlier work and unresolved questions.

## How can I check it?

Follow the worked example in [the reading guide](READING_GUIDE.md#check-one-example-by-hand). It connects a source record, a key or model assumption, and the saved output. For an independent source check, use the [original-source entry](https://crypto.hcportal.eu/dashboard/cryptograms/1193); images are linked, not redistributed here.

If you use Python, follow the [complete verification instructions](verification/README.md), including download/setup, expected results and troubleshooting. The command from this repository’s top-level folder is:

```sh
python3 verification/check_all.py
```

A successful run means the published files and declared calculation reproduce. It does not establish that every source sign or historical interpretation is correct.

## Precise research scope

Partial geometric-key reading: 213 mapped out of 222 positions, eight masks and unexplained slot 27. Coverage is not accuracy; retain original and later corrections.

This is part of [Cipher-Atelier](https://github.com/Cipher-Atelier), founded by [Maxim Egorov](https://github.com/cayde-6). Explore the [research index](https://github.com/Cipher-Atelier/research-index), [contribution guide](https://github.com/Cipher-Atelier/.github/blob/main/CONTRIBUTING.md), and [step-by-step research workflow](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md).

Source credit and item-specific restrictions remain in the research records. Scans, crops, restricted materials and private correspondence are excluded. No new blanket licence is asserted. AI-assisted work requires evidence checking and does not constitute external human expert review.

[Publication provenance](SOURCE_PROVENANCE.json) records the source commit, retained file hashes and deliberate code/navigation adaptations. The original repository history remains intact.

## Contribute to this investigation

Read the current result and source limitations, then coordinate a bounded task in an existing issue or use [Work on existing research](https://github.com/Cipher-Atelier/kingston-cipher-postcard-1907/issues/new?template=research.yml). Fork the repository and submit a focused pull request with your evidence and checks. Independent replication and constructive alternative readings are welcome. See [Start here](https://github.com/Cipher-Atelier/research-index/blob/main/START_HERE.md) for the shared workflow.
