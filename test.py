import unittest
import percolate
import test_helper as t


class TestPercolateApplication(unittest.TestCase):

    def test_get_entries_from_file(self):
        """
        test if entries from the data.in file were read successfully
        test if each entry string was successfully formatted into a list and if each comma was stripped correctly
        """
        entries = percolate.get_entries_from_file('data/data.in')
        self.assertIsNotNone(entries)

        for entry in entries:
            s = 'daniel'
            self.assertIsInstance(entry, list)
            self.assertFalse(s.__contains__(', '))

    def test_normalize_entries_and_update_data(self):
        """
        test if the normalize_entries method returns a correctly formatted dictionary object based on the readme_instructions
        test if the _update_data method is correctly updating our data/entries dictionary given the entry
        """
        test_entries = []
        test_entry_input_format_1 = ['Zhang', 'Daniel T.', '(111)-222-3333', 'aqua', '60647']
        test_entry_input_format_2 = ['Daniel T. Zhang', 'aqua marine', '61820', '012 345 6789']
        test_entry_input_format_3 = ['Daniel', 'Zhang', '60654', '312 555 9876', 'turquoise']
        test_entry_incorrect_input_format = ['Daniel t', '60649', '111222333444', 'blue', 'zhang']

        test_entries.append(test_entry_input_format_1)
        test_entries.append(test_entry_input_format_2)
        test_entries.append(test_entry_input_format_3)
        test_entries.append(test_entry_incorrect_input_format)

        entries = percolate.normalize_entries(test_entries)  # normalize_entries method calls the _update_data method

        self.assertTrue(len(entries['entries']) == 3)
        self.assertTrue(len(entries['errors']) == 1)

    def test_create_regex_matches(self):
        """
        test each regular expression in the created regex dictionary
        """
        rx = percolate._create_regex_matches()

        self.assertIsNotNone(rx['firstname'].match(t.valid_firstname_1))
        self.assertIsNotNone(rx['firstname'].match(t.valid_firstname_2))
        self.assertIsNone(rx['firstname'].match(t.invalid_firstname_1))
        self.assertIsNone(rx['firstname'].match(t.invalid_firstname_2))
        self.assertIsNone(rx['firstname'].match(t.invalid_firstname_3))

        self.assertIsNotNone(rx['lastname'].match(t.valid_lastname_1))
        self.assertIsNone(rx['lastname'].match(t.invalid_lastname_1))
        self.assertIsNone(rx['lastname'].match(t.invalid_lastname_2))

        self.assertIsNotNone(rx['fullname'].match(t.valid_fullname_1))
        self.assertIsNotNone(rx['fullname'].match(t.valid_fullname_2))
        self.assertIsNone(rx['fullname'].match(t.invalid_fullname_1))
        self.assertIsNone(rx['fullname'].match(t.invalid_fullname_2))
        self.assertIsNone(rx['fullname'].match(t.invalid_fullname_3))
        self.assertIsNone(rx['fullname'].match(t.invalid_fullname_4))

        self.assertIsNotNone(rx['phone1'].match(t.valid_phone1_1))
        self.assertIsNotNone(rx['phone1'].match(t.valid_phone1_2))
        self.assertIsNone(rx['phone1'].match(t.invalid_phone1_1))
        self.assertIsNone(rx['phone1'].match(t.invalid_phone1_2))
        self.assertIsNone(rx['phone1'].match(t.invalid_phone1_3))
        self.assertIsNone(rx['phone1'].match(t.invalid_phone1_4))

        self.assertIsNotNone(rx['phone2'].match(t.valid_phone2_1))
        self.assertIsNotNone(rx['phone2'].match(t.valid_phone2_2))
        self.assertIsNone(rx['phone2'].match(t.invalid_phone2_1))
        self.assertIsNone(rx['phone2'].match(t.invalid_phone2_2))
        self.assertIsNone(rx['phone2'].match(t.invalid_phone2_3))
        self.assertIsNone(rx['phone2'].match(t.invalid_phone2_4))

        self.assertIsNotNone(rx['color'].match(t.valid_color_1))
        self.assertIsNotNone(rx['color'].match(t.valid_color_2))
        self.assertIsNone(rx['color'].match(t.invalid_color_1))
        self.assertIsNone(rx['color'].match(t.invalid_color_2))

        self.assertIsNotNone(rx['zipcode'].match(t.valid_zipcode_1))
        self.assertIsNotNone(rx['zipcode'].match(t.valid_zipcode_2))
        self.assertIsNone(rx['zipcode'].match(t.invalid_zipcode_1))
        self.assertIsNone(rx['zipcode'].match(t.invalid_zipcode_2))
        self.assertIsNone(rx['zipcode'].match(t.invalid_zipcode_3))
        self.assertIsNone(rx['zipcode'].match(t.invalid_zipcode_4))

    def test_normalize_phone_number(self):
        """
        test if valid phone number strings are transformed into the correct format based in the PDF
        invalid phone number strings should not return a transformed phone number
        """
        test_valid_phone_number_1 = '(111)-222-3333'
        test_valid_phone_number_2 = '321 432 9876'
        test_invalid_phone_number_1 = '111222333333444'
        test_invalid_phone_number_2 = '(111-222-3333'

        self.assertEqual(percolate._normalize_phone_number(test_valid_phone_number_1), '111-222-3333')
        self.assertEqual(percolate._normalize_phone_number(test_valid_phone_number_2), '321-432-9876')
        self.assertEqual(percolate._normalize_phone_number(test_invalid_phone_number_1), '111222333333444')
        self.assertEqual(percolate._normalize_phone_number(test_invalid_phone_number_2), '(111-222-3333')
