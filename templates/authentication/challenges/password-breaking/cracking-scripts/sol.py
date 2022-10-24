#!/usr/bin/python3

import sys
from hashlib import sha256
import itertools
import string

def dummy_module(hashes):
    hashes_to_crack = list(hashes)
    cracked_hashes = []

    guess = "dummy" # `guess` is your current guess and you will look for sha256(guess) in the `hashes` list
    encoded_guess = guess.encode('utf-8') # encode it just to respect parameter types
    hash_to_match = sha256(encoded_guess).hexdigest()

    # if sha256(guess) is found in the input list, then you just cracked a hash
    if hash_to_match in hashes_to_crack:
        # append (hash, input) to the list of cracked hashes
        cracked_hashes.append((hash_to_match, encoded_guess.decode('ascii')))
        # remove the cracked hash from the input list
        hashes_to_crack.remove(hash_to_match)

    return (hashes_to_crack, cracked_hashes)

def dictionary_module(hashes):
    hashes_to_crack = list(hashes) # make a copy of `hashes`
    cracked_hashes = []

    for s in [line.strip() for line in open("../dict/words")]:
        s = ''.join(s).encode('utf-8')
        # TODO

    return (hashes_to_crack, cracked_hashes)

def hybrid_module(hashes):
    hashes_to_crack = list(hashes) # make a copy of `hashes`
    cracked_hashes = []

    for s in [line.strip() for line in open("../dict/words")]:
        s = ''.join(s)
        # TODO

    return (hashes_to_crack, cracked_hashes)

def extended_hybrid_module(hashes):
    hashes_to_crack = list(hashes) # make a copy of `hashes`
    cracked_hashes = []

    for s in [line.strip() for line in open("../dict/words")]:
        s1 = ''.join(s).encode('utf-8')
        # TODO

    return (hashes_to_crack, cracked_hashes)

def salt_module(hashes):
    hashes_to_crack = list(hashes) # make a copy of `hashes`
    cracked_hashes = []

    for s in [line.strip() for line in open("../dict/words")]:
        s = ''.join(s)
        # TODO

    return (hashes_to_crack, cracked_hashes)

def extended_salt_module(hashes):
    hashes_to_crack = list(hashes) # make a copy of `hashes`
    cracked_hashes = []

    for s in [line.strip() for line in open("../dict/words")]:
        s = ''.join(s)
        # TODO

    return (hashes_to_crack, cracked_hashes)

def brute_force_module(hashes):
    hashes_to_crack = list(hashes) # make a copy of `hashes`
    cracked_hashes = []

    for s in itertools.product(string.printable, repeat=4):
        s = ''.join(s).encode('utf-8')
        # TODO

    return (hashes_to_crack, cracked_hashes)

def main():
    hashes = [line.strip() for line in sys.stdin]
    cracked_hashes = []

    (to_crack, cracked) = dummy_module(hashes)
    cracked_hashes += cracked
    (to_crack, cracked) = dictionary_module(to_crack)
    cracked_hashes += cracked
    (to_crack, cracked) = hybrid_module(to_crack)
    cracked_hashes += cracked
    (to_crack, cracked) = extended_hybrid_module(to_crack)
    cracked_hashes += cracked
    (to_crack, cracked) = salt_module(to_crack)
    cracked_hashes += cracked
    (to_crack, cracked) = extended_salt_module(to_crack)
    cracked_hashes += cracked
    (to_crack, cracked) = brute_force_module(to_crack)
    cracked_hashes += cracked

    for c in cracked_hashes:
        print("{} -> {}".format(c[0], c[1]))

    for c in to_crack:
        print("{}".format(c))

if __name__ == "__main__":
    sys.exit(main())
