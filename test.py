import csv
from collections import OrderedDict

mapping_specification = {
    "CSV_File_1": {
        "Name": "Name",
        "Age": "Age",
        "Gender": {
            "map_to": "Active",
            "transformation": {
                "Female": True,
                "Male": False
            }
        }
    },
    "CSV_File_2": {
        "Full Name": {
            "map_to": "Name",
            "transformation": "split"
        },
        "Age Group": {
            "map_to": "Age",
            "transformation": "age_range"
        },
        "IsActive": "Active"
    }
}


def map_fields(csv_data, mapping_spec):
    mapped_data = []
    for row in csv_data:
        mapped_row = {}
        for csv_field, map_info in mapping_spec.items():
            if isinstance(map_info, str):
                for key, value in row:
                    if key == csv_field:
                        mapped_row[map_info] = value
                        break
            elif isinstance(map_info, dict):
                for key, value in row:
                    if key == csv_field:
                        if map_info['transformation'] == 'split':
                            mapped_row[map_info['map_to']] = value.split()[0]
                        elif map_info['transformation'] == 'age_range':
                            age_group = value.split('-')
                            mapped_row[map_info['map_to']] = (int(age_group[0]) + int(age_group[1])) // 2
                        else:
                            mapped_row[map_info['map_to']] = map_info['transformation'][value]
                        break
        mapped_data.append(mapped_row)
    return mapped_data


def read_csv(file_name):
    data = []
    with open(file_name, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        headers = next(csvreader)  # Read the header row
        for row in csvreader:
            row_data = dict(zip(headers, row))
            data.append([(key, row_data[key]) for key in headers])
    return data


if __name__ == '__main__':
    csv_file_1_data = read_csv('file1.csv')
    csv_file_2_data = read_csv('file2.csv')
    # Apply mapping
    mapped_csv_1 = map_fields(csv_file_1_data, mapping_specification["CSV_File_1"])
    mapped_csv_2 = map_fields(csv_file_2_data, mapping_specification["CSV_File_2"])

    print("Mapped CSV File 1:", mapped_csv_1)
    print("Mapped CSV File 2:", mapped_csv_2)
