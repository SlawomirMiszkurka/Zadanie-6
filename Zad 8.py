nums=[-15, 8, -31, 47, -2, 19]
maximum=nums[1]
minimum=nums[1]
for i in nums:
    if i>maximum:
        maximum=i
print(f'Max={maximum}')
for i in nums:
    if i<minimum:
       minimum=i
print(f'Min=:{minimum}')
        
    