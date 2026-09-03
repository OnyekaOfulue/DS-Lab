def sort_data(data, reverse=False):
	"""Return the data sorted in ascending or descending order."""
	return sorted(data, reverse=reverse)


if __name__ == "__main__":
	numbers = [64, 25, 12, 22, 11]
	print("Ascending:", sort_data(numbers))
	print("Descending:", sort_data(numbers, reverse=True))
