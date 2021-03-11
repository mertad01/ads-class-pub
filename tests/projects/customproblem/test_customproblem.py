#!/usr/bin/env python3
"""
Testing customproblem
"""

import pytest
from src.projects.customproblem import Vault, Card, Data, Folder, Login

logins = [
    ("mertad01", "carrot_on_a_stick123", "katie.luther.edu", "login for katie"),
    ("johnja06", "Pa$$word115", "mail.google.com", "email account information")
]

login_one = Login("mertad01",
                  "carrot_on_a_stick123",
                  "katie.luther.edu",
                  "login for katie")

login_one_alt = Login("mertad01",
                  "carrot_on_a_stick123",
                  "katie.luther.edu",
                  "login for katie")

login_two = Login("johnja06",
                  "Pa$$word115",
                  "mail.google.com",
                  "email account information")

card_one = Card("5000 1234 5678 9010",
                "924",
                "2024/06/13",
                "Checking account card")

card_one_alt = Card("5000 1234 5678 9010",
                "924",
                "2024/06/13",
                "Checking account card")

card_two = Card("9410 2358 1205 9385",
                "234",
                "2022/12/31")


class TestCustomProblemMethods:
    """Testing module customproblem"""

    @pytest.fixture(scope="function", autouse=True)
    def folder(self):
        """Setting up"""
        return Folder("Cards", [card_one, card_two])

    def test_card_str(self):
        """Testing something"""
        assert str(card_one) == "Type: Card\nCard Number: 5000 1234 5678 9010\nSecurity Code: 924\nExpiration Date: 2024/06/13\nNote: Checking account card"
        assert str(card_two) != str(card_one)

    def test_login_str(self):
        """Testing something"""
        assert str(login_one) == "Type: Login\nUsername: mertad01\nPassword: carrot_on_a_stick123\nURI: katie.luther.edu\nNote: login for katie"
        assert str(login_two) != str(login_one)

    def test_login_error(self):
        """Testing errors with login"""

    def test_card_error(self):
        """Testing errors with cards"""

    def test_folder_error(self):
        """Testing errors with cards"""
        with pytest.raises(TypeError) as excinfo:
            test_folder = Folder("Test Name", [login_one, card_one, "test", 3])
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "items_init must only contain Cards or Logins"

    def test_card_equals(self):
        """Testing something"""
        assert card_two != card_one
        assert card_one == card_one_alt

    def test_login_equals(self):
        """Testing something"""
        assert login_two != login_one
        assert login_one == login_one_alt

    def test_content(self):
        """Testing something"""
        assert card_one.get_content['security-code'] == '924'

    def test_folders(self):
        """Testing something"""
        cards = Folder("Cards", [card_one, card_two])
        logins = Folder("Logins", [login_one, login_two], "secret-code")
        all_items = Folder("todos", [login_one, card_two, card_one, login_two])
        assert cards != logins
        assert all_items != cards
        assert cards.get_name == "Cards"
        assert logins.get_name == "Logins"
        assert all_items.get_name == "todos"



if __name__ == "__main__":
    pytest.main(["-vv", "test_customproblem.py"])
