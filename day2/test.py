from day2 import determine_if_invalid_id

def test_determine_if_invalid_id():
    assert determine_if_invalid_id(11) == True
    assert determine_if_invalid_id(1212) == True
    assert determine_if_invalid_id(123123) == True
    assert determine_if_invalid_id(12341234) == True
    assert determine_if_invalid_id(123123123) == True
    assert determine_if_invalid_id(1234123412341234) == True
    assert determine_if_invalid_id(12312) == False
    assert determine_if_invalid_id(1112) == False
    assert determine_if_invalid_id(72501581) == False