# Knuth-Morris-Pratt-searcher
The Knuth-Morris-Pratt (KMP) algorithm is a linear-time string-matching algorithm that efficiently searches for occurrences of a pattern in a text. It improves upon the naive approach by preprocessing the pattern to create a partial match table (failure function or lps array), which helps skip unnecessary comparisons.


The Knuth-Morris-Pratt (KMP) algorithm is a linear-time string-matching algorithm that efficiently searches for occurrences of a pattern in a text. It improves upon the naive approach by preprocessing the pattern to create a partial match table (failure function or lps array), which helps skip unnecessary comparisons.

**Key Idea**:
The **KMP algorithm** avoids re-checking characters that have already been matched by utilizing the longest prefix which is also a suffix (LPS) information from the pattern.

It ensures that the algorithm runs in O(n + m) time, where:

n = length of the text,

m = length of the pattern.

Steps in KMP Algorithm:
1. Preprocess the Pattern (Compute LPS Array)
The LPS array (lps[i]) stores the length of the longest proper prefix of pattern[0..i] that is also a suffix.

Proper prefix means the prefix cannot be the entire string.

**Example**:
For the pattern "ABABC", the LPS array is:

Copy
Pattern: A B A B C  
LPS:    [0, 0, 1, 2, 0]
lps[3] = 2 because "AB" is the longest prefix-suffix match for "ABAB".

2. Search the Pattern in the Text
Traverse the text and pattern using two pointers:

* i for the text, j for the pattern. If characters match, increment both pointers.

*If they don’t match: If j > 0, set j = lps[j-1] (skip already matched prefix).

*Else, increment i.
