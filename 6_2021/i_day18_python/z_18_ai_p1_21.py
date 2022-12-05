"""The following python code can be used to solve the problem:
"""
import sys

def add_pairs(p1, p2):
    return [p1, p2]

def explode(nums):
    while True:
        found_pair = False
        for i in range(1, len(nums)-3):
            if isinstance(nums[i], list) and isinstance(nums[i-1], int) and isinstance(nums[i+1], int) and isinstance(nums[i+2], list) and isinstance(nums[i+3], list):
                nums = nums[:i-1] + [nums[i-1] + nums[i][0]] + [0] + [nums[i+1] + nums[i][1]] + nums[i+4:]
                found_pair = True
                break
        if not found_pair:
            break
    return nums

def split(nums):
    for i in range(len(nums)):
        if isinstance(nums[i], int) and nums[i] >= 10:
            nums = nums[:i] + [[nums[i]//2, (nums[i] + 1)//2]] + nums[i+1:]
    return nums

def reduce(nums):
    while True:
        old_nums = nums
        nums = explode(nums)
        nums = split(nums)
        if old_nums == nums:
            break
    return nums

def add(nums1, nums2):
    nums = add_pairs(nums1, nums2)
    nums = reduce(nums)
    return nums

def from_input_string(input_string: str) -> 'Tuple':
    lines = input_string.strip().split('\n')
    return (from_output_string(lines[0]), from_output_string(lines[1]))

def from_output_string(output_string: str) -> 'Any':
    output_string = output_string.strip()
    if not output_string:
        return []
    if output_string[0] == '[':
        return [from_output_string(x) for x in output_string[1:-1].split(',')]
    return int(output_string)

def to_input_string(inputs: 'Tuple') -> str:
    return to_output_string(inputs[0]) + '\n' + to_output_string(inputs[1])

def to_output_string(output: 'Any') -> str:
    if isinstance(output, list):
        return '[' + ','.join([to_output_string(x) for x in output]) + ']'
    return str(output)

if __name__ == '__main__':
    with open(sys.argv[1], 'r') as f:
        inputs = from_input_string(f.read())
    result = add(*inputs)
    print(to_output_string(result))
""""""