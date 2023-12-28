## File-Handling

### Reading CSV Files (`read_csv` function):

The `read_csv` function:
- Utilizes `csv.DictReader` to read CSV files and extract data row by row.
- Represents each row as a dictionary where keys correspond to column headers.

### Mapping Fields (`map_fields` function):

The `map_fields` function:
- Takes CSV data (list of dictionaries) and a mapping specification (`mapping_spec`).
- Iterates through each row of the CSV data.
- Traverses the `mapping_spec` to map fields based on provided instructions.
- Performs transformations:
  - If a mapping is a string, it directly maps the field to the specified name.
  - For dictionaries, it handles specific transformations like splitting values or converting age ranges.
- Stores mapped rows in `mapped_data`.

### Mapping Specification (`mapping_specification`):

This dictionary:
- Defines field mappings from CSV files to a common schema.
- Specifies mappings for different CSV files ("CSV_File_1", "CSV_File_2") with field mappings and transformations.

### Execution (`if __name__ == '__main__':`):

- Reads data from two CSV files (`file1.csv` and `file2.csv`) using `read_csv`.
- Applies mapping specified for each CSV file using `map_fields` and corresponding `mapping_spec`.
- Stores mapped data for each file in `mapped_csv_1` and `mapped_csv_2`.
- Prints the mapped data for both CSV files.

### Project Objective:

This project demonstrates a mapping mechanism that transforms various CSV file structures into a unified schema. The mapping rules enable transformations and renaming of fields to ensure consistency across different data sources.

## Understanding File Schema and Mapping Specification

### File 1 (file1.csv):

Name, Age, Gender  
Alice, 25, Female  
Bob, 30, Male  

#### Schema Inference:
- **Fields:**
    - `Name`: Represents the name of individuals.
    - `Age`: Denotes the age of each person.
    - `Gender`: Specifies the gender (Male/Female).

### File 2 (file2.csv):

Full Name, Age Group, IsActive  
Alice Johnson, 20-30, True  
Bob Smith, 30-40, False  

#### Schema Inference:
- **Fields:**
    - `Full Name`: Represents the full name of individuals.
    - `Age Group`: Defines an age range.
    - `IsActive`: Indicates if the person is active (True/False).

### Mapping Specification (mapping_specification):

#### For CSV_File_1:
- `Name`: Maps directly to the field `Name`.
- `Age`: Maps directly to the field `Age`.
- `Gender`: Maps to `Active`, with a transformation specified to convert `Female` to `True` and `Male` to `False`.

#### For CSV_File_2:
- `Full Name`: Splits into `Name`, considering the first part before the space.
- `Age Group`: Converts the range to an average age.
- `IsActive`: Directly maps to `Active` field, using the given boolean values.

The schema inference is based on the sample content provided in `file1.csv` and `file2.csv`. The `mapping_specification` is designed to transform and unify these varying schemas into a common schema that standardizes the representation of fields across different files.
