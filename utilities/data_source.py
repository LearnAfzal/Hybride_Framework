from utilities import read_utils

"""test_invalid_login_data=[
        ("john","john123","Invalid credentials"),
        ("jack","jack123","Invalid credentials")
    ]"""

test_add_valid_employee_data=[
    ["Admin","admin123","john","j","wick","john wick","john"],
    ["Admin","admin123","peter","j","son","peter son","peter"]
]

# reading data from a csv file

test_invalid_login_data=read_utils.get_csv_as_list("../test_data/test_invalid_login_data.csv")
print(test_invalid_login_data)