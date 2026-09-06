from collections.abc import Sequence


def sort_data(data: Sequence, reverse: bool = False) -> list:
	"""Return the data sorted in ascending or descending order."""
	return sorted(data, reverse=reverse)


def remove_null_values(data: Sequence) -> list:
	"""Return the data with all None values removed."""
	return [value for value in data if value is not None]


def grade_student(score: int | float) -> str:
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


def separate_columns(text: str, separator: str = ",") -> list[str]:
	"""Split a column string into separate items using the given separator."""
	if not isinstance(text, str):
		raise TypeError("text must be a string.")
	if not isinstance(separator, str) or not separator:
		raise ValueError("separator must be a non-empty string.")
	return [item.strip() for item in text.split(separator)]


def build_regression_model(
	x_values: Sequence[float], y_values: Sequence[float]
) -> tuple[float, float]:
	"""Build a simple linear regression model: y = m*x + b."""
	if len(x_values) != len(y_values):
		raise ValueError("x_values and y_values must be the same length.")
	if len(x_values) < 2:
		raise ValueError("At least two data points are required.")
	if not all(isinstance(value, (int, float)) and not isinstance(value, bool)
			   for value in (*x_values, *y_values)):
		raise TypeError("x_values and y_values must contain only numbers.")

	x_mean = sum(x_values) / len(x_values)
	y_mean = sum(y_values) / len(y_values)

	numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_values, y_values))
	denominator = sum((x - x_mean) ** 2 for x in x_values)

	if denominator == 0:
		raise ValueError("All x values are the same, so the model cannot be calculated.")

	slope = numerator / denominator
	intercept = y_mean - slope * x_mean
	return slope, intercept


if __name__ == "__main__":
	numbers = [64, 25, 12, 22, 11]
	print("Ascending:", sort_data(numbers))
	print("Descending:", sort_data(numbers, reverse=True))
	print("Without null values:", remove_null_values([1, None, 3, None, 5]))
	print("Student grade:", grade_student(85))
	print("Separated values:", separate_columns("Alice, Bob, Charlie"))

	x = [1, 2, 3, 4, 5]
	y = [2, 4, 5, 4, 5]
	slope, intercept = build_regression_model(x, y)
	print(f"Regression model: y = {slope:.2f}x + {intercept:.2f}")
	print("Predicted value for x = 6:", slope * 6 + intercept)

