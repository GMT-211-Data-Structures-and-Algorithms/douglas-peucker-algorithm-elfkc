from dp import *

input_file = 'second_test.geojson'
out_file = 'second_test_simplified.geojson'
epsilon = 0.0005
execute_douglas_peucker(input_file, out_file, epsilon)