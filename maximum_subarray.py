
def max_subarray_sum(nums):
    sum = 0
    maxsum = -10**10

    for i, n in enumerate(nums):
        if sum <= 0 and n > sum:
            sum = n
        else:
            sum += n
        maxsum = max(maxsum, sum)

    return maxsum


def max_subarray(nums):
    sum = 0
    maxsum = -10**10
    si, ei = 0, 0

    for i, n in enumerate(nums):
        if sum <= 0 and n > sum:
            sum = n
            si = i
        else:
            sum += n
        if sum > maxsum:
            ei = i
            maxsum = sum

    return nums[si:ei+1]


if __name__ == '__main__':
    assert(max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6)
    assert(max_subarray_sum([-2,-3,-1,-5]) == -1)
    assert(max_subarray_sum([6,4,1,2,5,3]) == 21)
    assert(max_subarray_sum([-2,-3,0,-5]) == 0)
    assert(max_subarray_sum([6,4,1,0,2,5,3]) == 21)
