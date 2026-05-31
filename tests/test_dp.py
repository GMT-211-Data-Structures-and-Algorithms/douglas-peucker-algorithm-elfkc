import pytest
# Importing the douglas_peucker function from your actual structure
from dp.dp_algo import douglas_peucker 

def test_straight_line():
    """Three collinear points within the epsilon should be reduced to two endpoints."""
    points = [[0, 0], [5, 0], [10, 0]]
    # Fixed parameter name from tolerance=1.0 to epsilon=1.0
    result = douglas_peucker(points, epsilon=1.0)
    
    assert len(result) == 2
    assert result[0] == [0, 0]
    assert result[-1] == [10, 0]

def test_sharp_spike():
    """A sharp spike that exceeds the epsilon must be preserved."""
    points = [[0, 0], [5, 10], [10, 0]]
    result = douglas_peucker(points, epsilon=1.0)
    
    # Since the spike (5,10) is well outside the 1.0 epsilon, all 3 points should remain
    assert len(result) == 3

def test_empty_input():
    """An empty input list should return an empty list safely without crashing."""
    assert douglas_peucker([], epsilon=1.0) == []