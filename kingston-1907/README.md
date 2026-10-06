# Kingston 1907: a partial reading of HCP1193

Research status as of 5 October 2026: **coherent English reading with a German-like phrase; 213/222 position coverage is not an accuracy score.**

## Research task

Recover the personal message on the Kingston postcard catalogued as HCP1193, dated 8 December 1907, while preserving damaged or ambiguous signs. The text addresses Helen and is affectionate in tone. No identification of the writer, relationship between named people, or historical delivery address is needed for the cryptanalytic result. [HCPortal catalogue](https://crypto.hcportal.eu/dashboard/cryptograms/1193).

## Tests completed

The first 158 cipher signs were used for key recovery, with the final 64 reserved. The key was fixed before the heldout portion was transcribed. It established 20 ordinary letter mappings; an extra position labelled 27 remained unexplained.

A geometric rule on a 3 × 3 grid was fixed before heldout evaluation. Among the tested geometric rules, it alone agreed with those 20 learned correspondences. It predicted F, K and V, three classes absent from training, at seven heldout positions.

At first evaluation, the learned key covered 53/64 heldout positions; the geometric extension covered 60/64. Four heldout positions remained ambiguous. A later key-blind source inspection corrected `mhss` to `miss` without altering the key, and preserved additional source doubts.

An initial method control failed on a Bill/Kill error. After observed word spacing was incorporated, while retaining the language corpus, four fresh synthetic texts gave 623/624 correct training letters and 251/251 correct covered heldout letters, with one heldout position uncovered. These control scores do not prove every letter of the postcard.

## Literal reading

The following preserves the 13 lines and uncertainty. The two bracketed handwriting fragments are outside the assigned cipher alphabet; `[27]` labels an unexplained key position, not a decoded number.

```text
well helen my [27] i did
not get the letter i
expected tonight was
ist los?en mit dir well
sweetheart as i will be
there almost as soon as
?his card i will only
?ell you how much i miss
you [handwritten fragment A] how much i will
love you to make up for
it ?hen i see ?ou so good
?ight love [handwritten fragment B] ki?s es your
fett?ock [uncertain final region]
```

The main sense is that an expected letter has not arrived, the writer expects to arrive almost as soon as the card, and expresses affection. This summary does not resolve the uncertain letter forms.

## Coverage and unresolved readings

The corrected count is 222 cipher positions, not the earlier provisional 221. The current conditional geometric reading assigns 213/222: 154 in training and 59 in heldout. Eight signs are ambiguous and `[27]`, which occurs after *my* in the training portion, remains unexplained. The revised heldout accounting leaves five of its 64 positions unassigned. This supersedes the initial 60/64 coverage and its four unresolved positions. The ordinary handwriting and final region are accounted for separately. The historical plaintext is unknown, so **95.9% coverage must not be reported as 95.9% accuracy**.

The German-like `was ist los?en mit dir` contains a six-sign uncertain word. Reducing it to ordinary German *was ist los mit dir* would delete material and is only an editorial hypothesis. The closing `fett?ock` remains untranslated; reading it as *Fettsack* would require an unsupported vowel change. Likewise, `?ight` is not a securely recovered *night*: the retained source alternatives do not establish n. The handwritten fragments must not silently become *and*, and `ki?s es` requires interpretation before it can become *kisses*.

## Public sources and earlier-work credit

- [HCPortal HCP1193](https://crypto.hcportal.eu/dashboard/cryptograms/1193) and its [cipher-side image](https://api.hcportal.eu/media/3639/cpc_1907-12-08_USA_Kingston,-NY_USA_New-York__pic.jpg). Metadata checked on 5 October 2026 credits Tobias Schrödel's postcard collection and still labels the language unknown and the solution “Not solved.”
- Nicholas Gessler's [“Collections in Cryptology – Paper Alphabets”](https://people.duke.edu/~ng46/collections/crypto-paper.htm), item G, publicly presents the Kingston encrypted postcard. This is a known teaching and collecting source, not a newly found manuscript.
- Tobias Schrödel, [“Cryptographic postcards”](https://ecp.ep.liu.se/index.php/histocrypt/article/view/166), HistoCrypt 2021, DOI 10.3384/ecp183166, provides the collection context linked by HCPortal.

No global-priority claim or complete error-free decipherment is made. Public source availability does not itself grant permission to redistribute the photographs.
