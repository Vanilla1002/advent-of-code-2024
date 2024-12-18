def recursive_function(list_of_nums, needed_sum, current_sum=0, index=1):
    if index == len(list_of_nums):
        return current_sum == needed_sum
    next_int = list_of_nums[index]
    return recursive_function(list_of_nums, needed_sum, current_sum + next_int,index+1) or recursive_function(list_of_nums, needed_sum, current_sum*next_int,index+1)










result = 0
with open ('./day7/input7.txt') as f:
    for line in f:
        line = line.split()
        needed_sum = int(line[0][:-1])
        list_of_nums = [int(i) for i in line[1:]]
        print(list_of_nums)
        if recursive_function(list_of_nums, needed_sum,list_of_nums[0]):
            result += needed_sum

print(result)
        
        