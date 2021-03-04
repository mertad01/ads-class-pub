#!/usr/bin/env python3
"""
`bank` implementation

@author:
"""

from abc import ABC, abstractmethod


class Address:
    """Address class"""

    def __init__(
        self, street_init: str, city_init: str, state_init: str, zip_init: str
    ):
        """__init__"""
        self._street = street_init
        self._city = city_init
        self._state = state_init
        self._zip = zip_init

    def get_street(self):
        """Return Street Name"""
        return self._street

    def get_city(self):
        """Return City Name"""
        return self._city

    def get_state(self):
        """Return State Name"""
        return self._state

    def get_zip(self):
        """Return Zip Code"""
        return self._zip

    street = property(get_street)
    city = property(get_city)
    state = property(get_state)
    zip = property(get_zip)

    def __eq__(self, other: object):
        """Compare 2 addresses"""
        if isinstance(other, Address):
            return bool(
                self._street == other.street and
                self._city == other.city and
                self._state == other.state and
                self._zip == other.zip
            )
        raise TypeError("Can only compare Address")

    def __str__(self):
        """__str method"""
        return f"{self._street}\n{self._city}, {self._state} {self._zip}"


class Customer:
    """Customer class"""

    def __init__(self, name_init: str, dob_init: str, address_init: object):
        """Constructor"""
        self._name = name_init
        self._dob = dob_init
        self._address = address_init

    def get_name(self):
        """Return Name"""
        return self._name

    def get_dob(self):
        """Return Date of Birth"""
        return self._dob

    def get_address(self):
        """Return Address"""
        return self._address

    name = property(get_name)
    dob = property(get_dob)
    address = property(get_address)

    def move(self, new_address: object):
        """Change address"""
        if isinstance(new_address, Address):
            self._address = new_address
        else:
            raise TypeError("Can only change to another Address")

    def __str__(self):
        """__str"""
        return f"{self._name} ({self._dob})\n{self._address}"


class Account(ABC):
    """Account class"""

    @abstractmethod
    def __init__(self, owner_init: object, balance_init: float = 0):
        """Constructor"""
        self._owner = owner_init
        self._balance = balance_init

    def get_owner(self):
        """Return Owner"""
        return self._owner

    def get_balance(self):
        """Return Balance"""
        return self._balance

    owner = property(get_owner)
    balance = property(get_balance)

    def deposit(self, amount: float):
        """Add money"""
        if amount <= 0:
            raise ValueError("Must deposit positive amount")
        self._balance += amount

    def close(self):
        """Close account"""
        self._balance = 0

    def __str__(self):
        """__str__"""
        raise NotImplementedError


class CheckingAccount(Account):
    """CheckingAccount class"""

    def __init__(
            self,
            owner_init: object,
            fee_init: float,
            balance_init: float = 0
    ):
        """Constructor"""
        super().__init__(owner_init, balance_init)
        self._insufficient_funds_fee = fee_init

    def process_check(self, amount: float):
        """Process a check"""
        if amount > self._balance:
            self._balance -= self._insufficient_funds_fee
        else:
            self._balance -= amount

    def __str__(self):
        """__str__"""
        return f"Checking account\nOwner: {self._owner}\nBalance: {self._balance:.2f}"


class SavingsAccount(Account):
    """CheckingAccount class"""

    def __init__(
        self, owner_init: object, interest_rate_init: float, balance_init: float = 0
    ):
        """Constructor"""
        raise NotImplementedError

    def yield_interest(self):
        """Yield annual interest"""
        raise NotImplementedError

    def __str__(self):
        """__str__"""
        raise NotImplementedError


def main():
    """Main"""
    addr = Address("700 College Dr", "Decorah", "IA", "52101")
    cstmr = Customer("John Doe", "1861-09-01", addr)
    chk = CheckingAccount(cstmr, 15, 25)
    chk.process_check(30)
    print(chk)


if __name__ == "__main__":
    main()
