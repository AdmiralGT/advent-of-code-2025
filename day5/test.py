from day5 import FreshnessRange
import pytest

@pytest.mark.parametrize(
    "range1,range2,expected",
    [
        (FreshnessRange(start=5, end=10), FreshnessRange(start=1, end=3), False),
        (FreshnessRange(start=5, end=10), FreshnessRange(start=3, end=7), True),
        (FreshnessRange(start=5, end=10), FreshnessRange(start=3, end=15), True),
        (FreshnessRange(start=5, end=10), FreshnessRange(start=7, end=9), True),
        (FreshnessRange(start=5, end=10), FreshnessRange(start=7, end=15), True),
        (FreshnessRange(start=5, end=10), FreshnessRange(start=11, end=15), False),
        (FreshnessRange(start=5, end=10), FreshnessRange(start=5, end=12), True),
        (FreshnessRange(start=5, end=10), FreshnessRange(start=3, end=10), True),
    ]
)
def test_overlap(range1, range2, expected):
    assert range1.overlap(range2) == expected
    assert range2.overlap(range1) == expected

def test_extend():
    range1 = FreshnessRange(start=5, end=10)
    range2 = FreshnessRange(start=8, end=15)
    range1.extend(range2)
    assert range1.start == 5
    assert range1.end == 15

    range3 = FreshnessRange(start=1, end=4)
    range1.extend(range3)
    assert range1.start == 1
    assert range1.end == 15

@pytest.mark.parametrize(
    "range1,range2,expected",
    [
        (FreshnessRange(start=5, end=10), FreshnessRange(start=3, end=7), FreshnessRange(start=3, end=10)),
        (FreshnessRange(start=5, end=10), FreshnessRange(start=3, end=15), FreshnessRange(start=3, end=15)),
        (FreshnessRange(start=5, end=10), FreshnessRange(start=7, end=9), FreshnessRange(start=5, end=10)),
        (FreshnessRange(start=5, end=10), FreshnessRange(start=7, end=15), FreshnessRange(start=5, end=15)),
    ]
)
def test_extending(range1, range2, expected):
    range1.extend(range2)
    assert range1.start == expected.start
    assert range1.end == expected.end

@pytest.mark.parametrize(
    "freshness_range,count",
    [
        (FreshnessRange(start=5, end=10), 6),
        (FreshnessRange(start=1, end=1), 1),
        (FreshnessRange(start=100, end=200), 101),
    ]
)
def test_id_count(freshness_range, count):
    assert freshness_range.id_count() == count