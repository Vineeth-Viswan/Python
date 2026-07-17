def verify_card_number(card_number):
	cleaned = card_number.replace(" ", "").replace("-", "")

	if not cleaned.isdigit() or len(cleaned) == 0:
		return "INVALID!"

	total = 0
	reversed_digits = cleaned[::-1]

	for index, char in enumerate(reversed_digits):
		digit = int(char)

		if index % 2 == 1:
			digit *= 2
			if digit > 9:
				digit -= 9

		total += digit

	if total % 10 == 0:
		return "VALID!"

	return "INVALID!"
