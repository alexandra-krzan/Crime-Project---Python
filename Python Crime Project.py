# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 18:45:25 2024

@author: Alex Krzan
"""

import csv
import json
import matplotlib.pyplot as plt



def read_crime_data(filename):
    """Read crime data from a CSV file."""
    crimeData = []
    with open(filename, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            crimeData.append(row)
    return crimeData  


def count_crimes_by_ncic(data):
    ncic_counts = {}
    for row in data:
        ncic_code = int(row['ucr_ncic_code'])
        count = (ncic_code // 1000) * 1000
        if count not in ncic_counts:
            ncic_counts[count] = 0
        ncic_counts[count] += 1
    return ncic_counts

def count_crimes_by_district(data):
    district_counts = {}
    for row in data:
        district = row['district']
        if district not in district_counts:
            district_counts[district] = 0
        district_counts[district] += 1
    return district_counts

def count_crimes_by_beat(data):
    beat_counts = {}
    for row in data:
        beat = row['beat'].strip()
        if beat not in beat_counts:
            beat_counts[beat] = 0
        beat_counts[beat] += 1
    return beat_counts

def save_report_to_json(report, month):
    with open(f"{month}.json", 'w') as json_file:
        json.dump(report, json_file, indent=4)


def display_crimes_for_beat(data, beat):
    """Display all crimes for a specific beat."""
    print(f"Crimes in Beat {beat}:")
    for row in data:
        if row['beat'].strip() == beat.strip():
            print(f"Description: {row['crimedescr']}, NCIC Code: {row['ucr_ncic_code']}")


def create_bar_chart(data, ncic_codes, title):
    counts = {str(code): 0 for code in ncic_codes}
    for row in data:
        ncic_code = str(row['ucr_ncic_code'])
        if ncic_code in counts:
            counts[ncic_code] += 1
    
    plt.bar(counts.keys(), counts.values(), color='blue')
    plt.xlabel('NCIC Code')
    plt.ylabel('Count')
    plt.title(title)
    plt.savefig(f"{title}.png")
    plt.show()


## MAIN CODE ##

filename = input("Enter the name of a file: ")
crimeData = read_crime_data(filename)

keepGoing = 'true'

while keepGoing == 'true':
    print("\nMenu:")
    print("1. Display Crime Report")
    print("2. Display Crimes by Beat")
    print("3. Create NCIC Bar Chart")
    print("4. Quit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        ncic_report = count_crimes_by_ncic(crimeData)
        district_report = count_crimes_by_district(crimeData)
        beat_report = count_crimes_by_beat(crimeData)
            
        report = {
            "ncic_report": ncic_report,
            "district_report": district_report,
            "beat_report": beat_report
        }
            
        month = input("Enter the month: ")
        save_report_to_json(report, month)
        print("Crime report saved to JSON file.")
    elif choice == '2':
        beat = input("Enter beat number: ")
        display_crimes_for_beat(crimeData, beat)
    elif choice == '3':
        ncic_codes = []
        for i in range(5):
            code = input(f"Enter NCIC code {i+1}: ")
            ncic_codes.append(code)
        title = input("Enter chart title: ")
        create_bar_chart(crimeData, ncic_codes, title)
    elif choice == '4':
        print("\n\nExiting program.")
        keepGoing = 'false'
    else:
        print("Invalid choice. Please try again.")
        
        
     

        
        
        
        






        
        
        


