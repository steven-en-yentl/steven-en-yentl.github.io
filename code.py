import sys
import hashlib

hasher = hashlib.md5

box_code = sys.argv[1]
keywords = sys.argv[2:-1]
youtube  = sys.argv[-1]

seed = "Zo makkelijk gaan we het niet maken he Steven."

to_digest = "".join(keywords)

goal_byte = map(ord,box_code+youtube)

print "var check_hash = %s;" % map(ord,hasher(to_digest).digest())
r_byte = map(ord,hasher(seed+to_digest).digest())
offset_byte = [ (j-i) % 256 for i,j in zip(r_byte,goal_byte)]
print "var offset = %s;" % str(list(offset_byte))

print  [ chr((i+j) % 256) for i,j in zip(r_byte,offset_byte)]




