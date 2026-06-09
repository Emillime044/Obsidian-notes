MAC(B) rappresenta i quattro timestamp principali che descrivono la vita di un file in NTFS.
Analisi degli attributi del file MAC(B).

- Modified
- Accessed
- Changed ($MFT (Master File Table) Modified)
- Birth (file creation time)

La B è tra parentesi perché non tutti i file system registrano la nascita temporalmente parlando.

## MFT: Standard Info Attribute

$STANDARD_INFO Attribute

$STANDARD_INFO (\$SI) contiene:
- file metadata, come flags;
- file SID;
- file owner;
- set di MAC(b) timestamps;

$STANDARD_INFO: timestamp raccolto (e modificabile) da Windows Explorer, fls, mactime, timestomp, find e le altre utility legate alla visualizzate di timestamp.