# Name: Sanan Kafeel Khan
# Roll No: TRN-2026-000336
# Date: 2026-11-06
# Part 12 Challenge - pytest tests for BankAccount using a fixture

import pytest

from bank_account import BankAccount


@pytest.fixture
def account():
    """A fresh account with Rs 1000 for EVERY test, so tests don't affect each other."""
    return BankAccount("Sanan", 1000)


def test_deposit_increases_balance(account):
    account.deposit(500)
    assert account.balance == 1500


def test_withdraw_decreases_balance(account):
    account.withdraw(300)
    assert account.balance == 700


def test_history_records_transactions(account):
    account.deposit(200)
    account.withdraw(100)
    assert account.history == [("deposit", 200, 1200), ("withdraw", 100, 1100)]


def test_negative_amount_raises(account):
    with pytest.raises(ValueError):
        account.deposit(-50)
    with pytest.raises(ValueError):
        account.withdraw(-50)


def test_overdraw_raises_and_balance_unchanged(account):
    with pytest.raises(ValueError, match="insufficient"):
        account.withdraw(5000)
    assert account.balance == 1000
    assert account.history == []
