"""hexadecimal-fn-hexa-conformance-oracle -- deterministic CONFORMANCE oracle for `hexadecimal` (python).

WHAT THIS DECIDES: given a candidate callable and one canonical input, it decides whether the candidate
agrees with the proven reference. It is a *conformance* decider over a fixed, published corpus -- it does
not decide correctness in general, and it says nothing about inputs outside the corpus.

SCOPE (declared, so the boundary is visible rather than discovered): the corpus is the canonical Exercism
test data for this task, 8 input/output pairs, listed in `probes/probes.jsonl`. Inputs outside that
set are simply not covered; `decide` answers only about the input it is given.

PROVENANCE: the reference body comes from the Exercism reference solution for `hexadecimal` (MIT, Exercism);
the type annotations were added by harvest, the body is unchanged (checked at AST level). The capability
was PROVEN by the exercism testsuite (pin=62bbbc465abb9bc6) and re-executed by harvest in a sealed sandbox
(unshare -rn) -- verify-not-relay, not a copied ledger label.
"""

TASK = "hexadecimal"
CWE = "hexadecimal"          # a publish-motor egyseges mezonevet var; itt a feladat azonositoja


def decide(fn, value, expect):
    """PASS iff fn(value) == expect. Determinista, nincs halozat, nincs allapot."""
    try:
        return "PASS" if fn(value) == expect else "FAIL"
    except Exception:                                      # noqa: BLE001
        return "FAIL"


from functools import reduce

def hexa(hex_string: str) -> int:
    hex_string = hex_string.lower()
    if set(hex_string) - set('0123456789abcdef'):
        raise ValueError('Invalid hexadecimal string')
    digits = [ord(letter) - ord('a') + 10 if letter in 'abcdef' else ord(letter) - ord('0') for letter in hex_string]
    return reduce(lambda var_1, var_2: var_1 * 16 + var_2, digits, 0)

REFERENCE = hexa
