def merge_sort(arr):
	
	if len(arr) > 1:
		left_arr = arr[:len(arr) //  2]
		right_arr = arr[len(arr) // 2:]

		# Recursion part
		merge_sort(left_arr)
		merge_sort(right_arr)

		# Merging elements, where i -> left_arr index, j -> right_arr index, k -> merged_arr index
		i = 0
		j = 0
		k = 0

		# Merging two parts into the main array
		while i < len(left_arr) and j < len(right_arr):
			if left_arr[i] < right_arr[j]:
				arr[k] = left_arr[i]
				i += 1
			else:
				arr[k] = right_arr[j]
				j += 1
			k += 1

		# If there are elements left in left_arr, add them as well
		while i < len(left_arr):
			arr[k] = left_arr[i]
			i += 1
			k += 1

		# If there are elements left in rigt_arr, add them as well
		while j < len(right_arr):
			arr[k] = right_arr[j]
			j += 1
			k += 1


my_list = [2, 6, 5, 7, 4, 3]
merge_sort(my_list)
print(my_list)
