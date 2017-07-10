"""
These are all test constants used for the test_create_regex_matches() method
"""

valid_firstname_1 = 'Daniel'
valid_firstname_2 = 'Daniel T.'
invalid_firstname_1 = 'daniel'
invalid_firstname_2 = 'daniel t.'
invalid_firstname_3 = 'Daniel T'

valid_lastname_1 = 'Zhang'
invalid_lastname_1 = 'zhang'
invalid_lastname_2 = 'T. Zhang'

valid_fullname_1 = 'Daniel Zhang'
valid_fullname_2 = 'Daniel T. Zhang'
invalid_fullname_1 = 'Daniel'
invalid_fullname_2 = 'daniel zhang'
invalid_fullname_3 = 'Daniel t Zhang'
invalid_fullname_4 = 'Daniel t. Zhang'

valid_phone1_1 = '(111)-222-3333'
valid_phone1_2 = '(123)-234-1234'
invalid_phone1_1 = '111-222-3333'
invalid_phone1_2 = '1112223333'
invalid_phone1_3 = '111 222 3333'
invalid_phone1_4 = '(111)-222-333333'

valid_phone2_1 = '111 222 3333'
valid_phone2_2 = '123 234 1234'
invalid_phone2_1 = '111-222-3333'
invalid_phone2_2 = '1112223333'
invalid_phone2_3 = '(111)-222-3333'
invalid_phone2_4 = '111 222 333333'

valid_color_1 = 'grey'
valid_color_2 = 'space grey'
invalid_color_1 = '60647'
invalid_color_2 = 'Daniel'

valid_zipcode_1 = '60647'
valid_zipcode_2 = '61820'
invalid_zipcode_1 = '312'
invalid_zipcode_2 = '312555'
invalid_zipcode_3 = 'blue'
invalid_zipcode_4 = 'Daniel Zhang'