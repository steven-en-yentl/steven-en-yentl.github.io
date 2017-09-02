import sys
code = sys.argv[1]
keywords = sys.argv[2:]
seed = "Zo makkelijk gaan we het niet maken he Steven."

digest = "".join(keywords)

print "check", hash(digest)
print "" hash(seed+digest)
