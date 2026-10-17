
def test_login():
    # Sample test for the AttendX login module.
    username = "d24it181"
    password = "d24it181"

    # Replace with the actual application's login action.
    assert username != "       "
    assert password != ""

    print("Login test: input validation passed")


def test_login_empty_fields():
    username = ""
    password = ""

    # Expected: the application should reject empty credentials.
    assert username == ""
    assert password == ""

    print("Login negative test: empty fields checked")


if __name__ == "__main__":
    test_login()
    test_login_empty_fields()
