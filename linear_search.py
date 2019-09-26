#LinearSearch Implmentation
def linear_search(items, item):
	for i in range(len(items)):
		if item == items[i]:
			return '{} is on the list at index {}\n'.format(item, items.index(item))

	return '{} is not on the list\n'.format(item)

print([i for i in range(100) if i%4==0], '\n')
print(linear_search([i for i in range(100) if i%4==0], 88))
