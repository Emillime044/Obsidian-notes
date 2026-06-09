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


## File Name Attribute

$FILE_NAME Attribute
$FILE_NAME (\$FN):
- Contiene filename in Unicode e altri set di MAC(b) timestamps;

Analogo a $STANDARD_INFO attribute ma:
- $STANDARD_INFO modificabile da utility in user space come timestamp
	- Potenzialmente non probante in fase di raccolta di informazioni;
- $FILE_NAME Attribute modificabile solo a livello kernel e non ci sono tool noti che lo possano fare.