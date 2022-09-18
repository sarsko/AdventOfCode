import hashlib

key = "yzbqklnj"

cntr = 0
result = ""

while not hashlib.md5((key + str(cntr)).encode("ascii")).hexdigest().startswith("00000"):
    cntr += 1

print(cntr)

while not hashlib.md5((key + str(cntr)).encode("ascii")).hexdigest().startswith("000000"):
    cntr += 1

print(cntr)
