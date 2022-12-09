from titanic_utils.utils import is_adult

def test_is_adult():
    '''Test that the titanic_utils.is_adult() function behaves correctly on three different ages.'''

    ages = [5, 20, 35]
    threshold = 18

    results = [is_adult(age, threshold) for age in ages]
    assert(results == [False, True, True])

