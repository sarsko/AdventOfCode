print(sum((ord(max({*x[:len(x)//2]}&{*x[len(x)//2:]})))%58for x in open("i")))
print(sum((ord(max(x&y&z))-96)%58for x,y,z in zip(*[map(set,open("i"))]*3)))
