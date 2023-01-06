def dp_test_case_id(test_case_name):
	test_case_id = None
	test_cases = {
		"field_label": 1010958,
		"discount_no_label": 1010960,
		"fixed_discount": 1010961,
		"percentage_discount": 1010968,
		"valid_discount_amount": 1010969,
		"invalid_discount_amount": 1010970,
		"min_max_qty_valid": 1010971,
		"min_max_qty_invalid": 1010973,
		"fixed_range": 1010977,
		"percentage_range": 1010979,
		"bulk_discount_amount_valid": 1010980,
	}
	if test_cases[test_case_name]:
		test_case_id = test_cases[test_case_name]

	return test_case_id