def is_valid_sample(sample_quality):
    """Test if the sample quality is acceptable.

    Returns True if the sample quality is high enough for valid test results
    and, False if it is not.
    """
    if sample_quality >= .95:
        return True
    else:
        return False

def is_valid_calibration(calibration_time):
    """Test if the calibration is acceptable.

    Returns True if the calibration time is low enough for valid results, and
    False if it is not.
    """
    if calibration_time < 5:
        return True
    else:
        return False

def main():
    total_tests = 0
    positive_tests = 0
    negative_tests = 0
    demographic_data = []

    while True:
        answer = input("Test positive? [y,n or stop]: ")
        if answer == "stop":
            break

        if answer == "y":
            test_result = True
        else:
            test_result = False

        q = float(input("Sample quality: "))
        t = int(input("Hours since last calibration: "))
        

        total_tests += 1
        
        
        if not (is_valid_sample(q) and is_valid_calibration(t)):
            print("Error: Invalid sample quality or calibration time.")
            return
        
        race = input("Race: ")
        gender = input("Gender: ")
        income = input("Income: ")

        demographic_data.append({
            "race": race,
            "gender": gender,
            "income": income,
            "test_result": test_result
             })
        
        if test_result:
            positive_tests += 1
        else:
            negative_tests += 1

    print()
    print("Total tests: ", total_tests)
    print("Positive: ", positive_tests)
    print("Negative: ", negative_tests)

    print("\nDemographic Data:")
    for entry in demographic_data:
        print(entry)

main()

import pytest
from exercise_3_covid_testing import is_valid_sample, is_valid_calibration

def test_is_valid_sample():
    assert is_valid_sample(0.95) == True
    assert is_valid_sample(0.96) == True
    assert is_valid_sample(1.0) == True
    assert is_valid_sample(0.94) == False
    assert is_valid_sample(0.0) == False

def test_is_valid_calibration():
    assert is_valid_calibration(4) == True
    assert is_valid_calibration(0) == True
    assert is_valid_calibration(4.9) == True
    assert is_valid_calibration(5) == False
    assert is_valid_calibration(6) == False

if __name__ == "__main__":
    pytest.main()


