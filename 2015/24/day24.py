nums = list(map(int, open("input.txt").read().strip().split("\n")))
goal = sum(nums)//3

# All weights are odd, we need 6 packages.
# i.e: 113+109+107+97+89+1

# Always include 1, and look for 5 packages
goal -= 1
nums = nums[1:]
nums = nums[::-1]

def quantum_entanglement(numrem, currw, i, quant):
    if i >= len(nums):
        return 9999999999999999
    if currw > goal:
        return 9999999999999999
    if currw == goal:
        return quant
    if numrem <= 0:
        return 9999999999999999
    return min(quantum_entanglement(numrem, currw, i + 1, quant),
               quantum_entanglement(numrem-1, currw + nums[i], i + 1, quant * nums[i]))

print(quantum_entanglement(5, 0, 0, 1))


nums = list(map(int, open("input.txt").read().strip().split("\n")))
goal = sum(nums)//4

# All weights are odd, we need 5 packages

nums = nums[::-1]

def quantum_entanglement2(numrem, currw, i, quant):
    if currw > goal:
        return 9999999999999999
    if currw == goal:
        return quant
    if i >= len(nums):
        return 9999999999999999
    if numrem <= 0:
        return 9999999999999999
    return min(quantum_entanglement2(numrem, currw, i + 1, quant),
               quantum_entanglement2(numrem-1, currw + nums[i], i + 1, quant * nums[i]))

print(quantum_entanglement2(5, 0, 0, 1))
