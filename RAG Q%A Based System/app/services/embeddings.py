import math
import re

def tokenize(text):
    return re.findall(r"\w+", text.lower())

def text_to_vector(text):
    vector = {}
    for word in tokenize(text):
        vector[word] = vector.get(word, 0) + 1
    return vector

def cosine_similarity(v1, v2):
    common = set(v1) & set(v2)
    numerator = sum(v1[w] * v2[w] for w in common)
    denom1 = sum(v**2 for v in v1.values())
    denom2 = sum(v**2 for v in v2.values())

    if denom1 == 0 or denom2 == 0:
        return 0.0

    return numerator / math.sqrt(denom1 * denom2)
