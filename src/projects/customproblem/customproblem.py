#!/usr/bin/env python3
"""
Custom Problem: Password/Data Management System
"""

from abc import ABC, abstractmethod
from getpass import getpass


class Vault(ABC):
    """Data Vault"""

    @abstractmethod
    def __init__(self, type_init: str, passwd_init: str = None):
        self._type = type_init

    @property
    def get_type(self):
        """Return name of the Vault"""
        return self._type


class Folder(Vault):
    """Folder containing list of data categorized"""

    def __init__(self, items_init: list,
                 passwd_init: str = None):
        super().__init__("Folder", passwd_init)
        for i in items_init:
            if not isinstance(i, Data):
                raise TypeError("items_init is not a type of data")
        self._items = items_init
        self._passwd = passwd_init

    @property
    def get_items(self):
        """Return items in the folder"""
        return self._items

    @property
    def get_passwd(self):
        """Return password to the folder"""
        return self._passwd


class Data(Vault):
    """Store of data"""

    @abstractmethod
    def __init__(self, type_init: str,
                 content_init: dict, note_init: str = None):
        super().__init__(type_init)
        self._content = content_init
        self._note = note_init

    @property
    def get_content(self):
        """Return content"""
        return self._content

    @property
    def get_note(self):
        """Return note"""
        return self._note


class Login(Data):
    """Login data type"""

    def __init__(self, username_init: str,
                 passwd_init: str, uri: str,
                 note_init: str = None):
        self._content = {
            "username": username_init,
            "password": passwd_init,
            "uri": uri,
            "note": note_init
        }
        super().__init__("Login", self._content, note_init)

    def __str__(self):
        typer = f"Type: {self._type}\n"
        username = f"Username: {self._content['username']}\n"
        password = f"Password: {self._content['password']}\n"
        uri = f"URI: {self._content['uri']}\n"
        note = f"Note: {self._note}"
        return typer + username + password + uri + note

    def __repr__(self):
        typer = f"{self._type}"
        user = f"{self._content['username']}"
        passwd = f"{self._content['password']}"
        uri = f"{self._content['uri']}"
        note = f"{self._note}"
        return f"{typer}('{user}', '{passwd}', '{uri}', '{note}')"

    def __eq__(self, other: object):
        if isinstance(other, Login):
            return self._content == other.get_content
        raise TypeError("Can not compare different types of classes.")

    @property
    def get_username(self):
        """Return the username"""
        return self._content["username"]

    @property
    def get_password(self):
        """Return the password"""
        return self._content["password"]

    @property
    def get_uri(self):
        """Return the URI"""
        return self._content["uri"]


class Card(Data):
    """Login data type"""

    def __init__(self, card_number_init: str,
                 security_code_init: str, expiration_date_init: str,
                 note_init: str = None):
        self._content = {
            "number": card_number_init,
            "security-code": security_code_init,
            "expiration": expiration_date_init,
            "note": note_init
        }
        super().__init__("Card", self._content, note_init)

    def __str__(self):
        typer = f"Type: {self._type}\n"
        number = f"Card Number: {self._content['number']}\n"
        security_code = f"Security Code: {self._content['security-code']}\n"
        expiration = f"Expiration Date: {self._content['expiration']}\n"
        note = f"Note: {self._note}"
        return typer + number + security_code + expiration + note

    def __repr__(self):
        typer = f"{self._type}"
        number = f"{self._content['number']}"
        security_code = f"{self._content['security-code']}"
        expiration = f"{self._content['expiration']}"
        note = f"{self._note}"
        return f"{typer}('{number}', '{security_code}', '{expiration}', '{note}')"

    def __eq__(self, other: object):
        if isinstance(other, Card):
            return self._content == other.get_content
        raise TypeError("Can not compare different types of classes.")

    @property
    def get_card_number(self):
        """Return the card number"""
        return self._content["number"]

    @property
    def get_security_code(self):
        """Return the security code"""
        return self._content["security-code"]

    @property
    def get_expiration(self):
        """Return the expiration date"""
        return self._content["expiration"]


def main():
    """Main"""
    test_login = Login(
        "mertad01",
        "carrot_on_a_stick123",
        "luther.edu",
        "Luther college norsekey login"
    )
    test_login_two = Login(
        "mertad01",
        "carrot_on_a_stick123",
        "luther.edu",
        "Luther college norsekey login"
    )
    test_card = Card(
        "5000 1234 5678 9010",
        "924",
        "2024/06/13"
    )
    test_card_two = Card(
        "1234 5678 9101 1121",
        "234",
        "2022/12/31"
    )
    print(test_login == test_login_two)
    print(test_card == test_card_two)

    test_folder = Folder([test_login, test_card])
    print(test_folder.get_items)


if __name__ == "__main__":
    main()
