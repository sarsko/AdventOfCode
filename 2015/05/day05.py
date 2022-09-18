def two_same(string):
   for i in range(len(string)-1):
      if string[i] == string[i+1]:
         return True
   return False

def repeat_with_letter_between(string):
   for i in range(len(string)-2):
      if string[i] == string[i+2]:
         return True
   return False

def repeat_no_overlap(string):
   for i in range(len(string)-2):
       for j in range(i+2, len(string)-1):
           if string[i] == string[j] and string[i+1] == string[j+1]:
               return True
   return False

cnt = 0
cnt2= 0
for s in open("input.txt").read().strip().split("\n"):
    if two_same(s) and sum(map(s.count, "aeiou")) > 2:
        if "ab" in s or "cd" in s or "pq" in s or "xy" in s:
            pass
        else:
            cnt += 1
    if repeat_with_letter_between(s) and repeat_no_overlap(s):
        cnt2 += 1

print(cnt)
print(cnt2)

