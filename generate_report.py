#!/usr/bin/env python3
# Please find the example csv file (employees.csv) with this script.
# The purpose of this script is to read a CSV file, count how many entries in each 
# category (employee directory), and then generate a report.
import csv
# reads CSV file
def read_employees(csv_file_location):
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
        employee_list = []
        for data in employee_file:
                employee_list.append(data)
        return employee_list
employee_list = read_employees('/source_of_CSV_files/employees.csv')
# appends employee data
def process_data(employee_list):
        department_list = []
        for employee_data in employee_list:
                department_list.append(employee_data['Department'])
        department_data = {}
        for department_name in set(department_list):
                department_data[department_name] = department_list.count(department_name)
        return department_data
dictionary = process_data(employee_list)
# Outputs a report file as reports.txt
def write_report(dictionary, report_file):
        with open(report_file, "w+") as f:
                for k in sorted(dictionary):
                        f.write(str(k)+':'+str(dictionary[k])+'\n')
                f.close()
write_report(dictionary, '/place_reports_here/test_report.txt')