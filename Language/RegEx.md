# Regular Expression

## MetaCharacters (Need to be escaped \)
.[{()\^$|?*+

## Single Character 
.       - Any Character
\d      - Digit (0-9)
\D      - Not Digit
\w      - word Character (a-z, A-Z, 0-9, _)
\W      - Not word Character
\s      - whitespace (space, tab, newline)
\S      - Not whitespace

\b      - word boundary (like \W but itself not included)
\B      - Not word boundary
^       - Beginning of a String
$       - End of a String

[]      - Character Set (any one match the set, not need \)
[1-7A-Z]   - Character Set Range
[^a-z]  - Characer Set NOT in the Range (Here ^ means not)

## Quantifiers
*       - 0 or more
+       - 1 or more
?       - 0 or One
{3}     - Excat Number
{3,4}   - Range of Number (min, max)

## Group
()      - Group 
|       - Either Or
(r|s|rs)    - r or s or rs

()()    - Group 1, 2 -> $1, $2 (Group 0 is the whole regex match)

## Special
(?i) ...        - case insensitive
(?i)...(?-i)    - only part case insensitive