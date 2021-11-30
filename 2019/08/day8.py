wide = 25
tall = 6
step = wide * tall
inp = open("input.txt", "r").read().strip()
prev = 0
minimum = step
out = 0
image = inp[0:step]
for i in range(len(inp)//step):
    idx = step * (i+1)
    haystack = inp[prev:idx]
    zero_count = haystack.count("0")
    if zero_count < minimum:
        out = haystack.count("1") * haystack.count("2")
        minimum = zero_count
    prev = idx
    new_img = []
    for l1, l2 in zip(image, haystack):
        if l1 == "2":
            new_img.append(l2)
        else:
            new_img.append(l1)
    image = new_img
image = "".join(image)
image = image.replace("0", " ")
image = image.replace("1", "#")
print(out)
for i in range(tall):
    print("".join(image[i*wide:(i+1)*wide]))
