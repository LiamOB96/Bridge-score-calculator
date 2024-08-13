from project import validate_contract, validate_vulnerability, validate_tricks_made, calculate_score
import pytest

def test_validate_contract():
    # Valid contracts
    assert validate_contract("4H") == ("4", "H", False, False)
    assert validate_contract("1DXX") == ("1", "D", False, True)
    assert validate_contract("5HX") == ("5", "H", True, False)

    # Invalid contracts
    with pytest.raises(ValueError):
        validate_contract("8H")
    with pytest.raises(ValueError):
        validate_contract("2X")

def test_validate_vulnerability():
    # Valid vulnerabilities
    assert validate_vulnerability("V") == "V"
    assert validate_vulnerability("NV") == "NV"

    # Invalid vulnerabilities
    with pytest.raises(ValueError):
        validate_vulnerability("X")
    with pytest.raises(ValueError):
        validate_vulnerability("")

def test_validate_tricks_made():
    # Valid tricks
    assert validate_tricks_made(0) == 0
    assert validate_tricks_made(6) == 6
    assert validate_tricks_made(13) == 13

    # Invalid tricks
    with pytest.raises(ValueError):
        validate_tricks_made(-1)
    with pytest.raises(ValueError):
        validate_tricks_made(14)


def test_calculate_score():
    #Test a simple game
    assert calculate_score(4, "H", False, False, "NV", 10) == 420

    #Test a doubled game
    assert calculate_score(4, "S", True, False, "NV", 11) == 690

    # Test a small slam in NT
    assert calculate_score(6, "NT", False, False, "V", 12) == 1440  # 690 for contract, 750 slam bonus

    # Test a grand slam in NT
    assert calculate_score(7, "NT", False, False, "NV", 13) == 1520  # 520 for contract, 1000 grand slam bonus

    # Test a failed 5D contract (undertricks)
    assert calculate_score(5, "D", False, False, "V", 7) == -400  # 6 undertricks

    #Test a failed doubled contract
    assert calculate_score(5, "D", True, False, "V", 9) == -500
