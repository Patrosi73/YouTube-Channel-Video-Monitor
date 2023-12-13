import json

def find_json_differences(data1, data2, output_path):
    difference_from_file2 = [item for item in data2 if item not in data1]
    difference_from_file1 = [item for item in data1 if item not in data2]
    combined_difference = difference_from_file2 + difference_from_file1
    with open(output_path, 'w') as file:
        json.dump(combined_difference, file, indent=2)

    print(f"changes written to {output_path}")


