def decreasing_monotonic_stack(arr):
	stack=[]
	for i in arr:
		while stack and stack[-1]<=i:
			stack.pop()
		stack.append(i)
	return stack

arr = [3, 1, 4, 1, 5, 9, 2, 6]
result = decreasing_monotonic_stack(arr)
print("Monotonic decreasing stack:", result)