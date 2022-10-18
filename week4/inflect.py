#inflect.py - Correctly generate plurals, singular nouns, ordinals,
# indefinite articles; convert numbers to words.

import inflect

p = inflect.engine()

print(
    p.plural_noun("I", N1),
    p.plural_verb("saw", N1),
    p.plural_adj("my", N2),
    p.plural_noun("saw", N2),
)