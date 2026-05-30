import math
import json

def calculate_distance(p, p1, p2):
# p: Calculated point [x, y]
# p1: Inıtial point [x, y]
# p2: Final Point [x, y]
    x0, y0 = p[0], p[1]
    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    
    # Distance between p1 to p2 
    denominator = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # If p1 and p2 same place. 
    if denominator == 0:
        return math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
        
    # distance point to line 
    numerator = abs((x2 - x1) * (y1 - y0) - (x1 - x0) * (y2 - y1))
    
    return numerator / denominator


def douglas_peucker(line, epsilon):
    if len(line) <= 2:
        return line

    dmax = 0.0
    index = 0
    
    start_point = line[0]
    end_point = line[-1]

    for i in range(1, len(line) - 1):
        d = calculate_distance(line[i], start_point, end_point)
        if d > dmax:
            index = i
            dmax = d

    if dmax > epsilon:
        left_line = douglas_peucker(line[:index+1], epsilon)
        right_line = douglas_peucker(line[index:], epsilon)
        return left_line[:-1] + right_line
    else:
        return [start_point, end_point]
    

def convert_coordinates_to_line(file_path):
    """
    read cooordinates in .txt files and return a list in float format
    """
    line = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for row in f:
            parts = row.strip().split()
            if len(parts) >= 2:
                # covert float and save cooordinates values
                line.append([float(parts[0]), float(parts[1])])
    return line

def execute_douglas_peucker(input_file, out_file, epsilon):
    """
    Read GeoJSON and txt files, and applied Douglas-Peucker algorithm  
    Saved new  GeoJSON file.
    """
# IF  READS GeoJSON FİLES 
    if input_file.endswith('.geojson'):
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        coordinates = data['features'][0]['geometry']['coordinates']
        simplified_coords = douglas_peucker(coordinates, epsilon)
        data['features'][0]['geometry']['coordinates'] = simplified_coords
        
        with open(out_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
            
        print(f"Epsilon: {epsilon}")
        print(f"Original Coor.: {len(coordinates)} -> Simplified Coor.: {len(simplified_coords)}")

# IF READS FİLES 
    elif input_file.endswith('.txt'):
        coordinates = convert_coordinates_to_line(input_file)
        simplified_coords = douglas_peucker(coordinates, epsilon)
        
        # write outputs in new txt file
        with open(out_file, 'w', encoding='utf-8') as f:
            for pt in simplified_coords:
                f.write(f"{pt[0]} {pt[1]}\n")
                
        print(f" Epsilon: {epsilon}")
        print(f"Originalo Coor.: {len(coordinates)} -> Simplified Coor.: {len(simplified_coords)}")
        
    else:
        print("error wrong file format ")