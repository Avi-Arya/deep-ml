def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	def calc_mean(row):
		return sum(row) / len(row)
	if mode == 'row':
		return [calc_mean(row) for row in matrix]
	else:
		return [calc_mean(list(col)) for col in zip(*matrix)]