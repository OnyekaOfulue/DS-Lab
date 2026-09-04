def sort_data(data, reverse=False):
	"""Return the data sorted in ascending or descending order."""
	return sorted(data, reverse=reverse)

def remove_null_values(data):
	"""Return the data with all None values removed."""
	return [value for value in data if value is not None]

def grade_student(score):
	"""Return a letter grade for a score from 0 to 100."""
	if not isinstance(score, (int, float)) or isinstance(score, bool):
		raise TypeError("Score must be a number.")
	if not 0 <= score <= 100:
		raise ValueError("Score must be between 0 and 100.")

	if score >= 90:
		return "A"
	if score >= 80:
		return "B"
	if score >= 70:
		return "C"
	if score >= 60:
		return "D"
	return "F"

if __name__ == "__main__":
	numbers = [64, 25, 12, 22, 11]
	print("Ascending:", sort_data(numbers))
	print("Descending:", sort_data(numbers, reverse=True))
	print("Without null values:", remove_null_values([1, None, 3, None, 5]))
	print("Student grade:", grade_student(85))

