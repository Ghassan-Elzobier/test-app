from streamlit.testing.v1  import AppTest
import pytest

@pytest.mark.parametrize(
        "username,password",
        [["hacker123","password123"],["viewer01","password"],["wrongUsername","wrongpass"]]
)
# Negative Username test
def test_incorrect_username_password(username:str, password:str):
    """Tests that login fails when username and/or password is incorrect"""
    at = AppTest.from_file("login.py").run()
    at.text_input[0].set_value(username).run()
    at.text_input[1].set_value(password).run()
    at.button[0].click().run()
    assert at.get("form")[0].children[3].value.startswith("Login Failed")
    assert at.sidebar.get("button") == []




@pytest.mark.parametrize(
    "username,password,role",
    [["johndoe","password123","admin"],["janedoe","securepass456","editor"],["viewer01","viewonly789","viewer"]]
)
def test_login_and_role(username:str, password:str, role:str):
    at = AppTest.from_file("login.py").run()
    at.text_input[0].set_value(username).run()
    at.text_input[1].set_value(password).run()
    at.button[0].click().run()
    assert at.sidebar.get("success")[0].value == f"Welcome **{username}** ({role}) :wave:"
    assert at.sidebar.get("button")[0].label == "Logout"

def test_logout():
    """Tests that clicking the logout button shows the login form and hides logout button"""
    at = AppTest.from_file("login.py")
    at.session_state.role = "viewer"
    at.run()
    at.sidebar.button[0].click().run()

    login_form_elements = at.get("form")[0].children

    assert login_form_elements[0].label == "Username"
    assert login_form_elements[0].value == ""

    assert login_form_elements[1].label == "Password"
    assert login_form_elements[1].value == ""

    assert login_form_elements[2].label == "Login"
    