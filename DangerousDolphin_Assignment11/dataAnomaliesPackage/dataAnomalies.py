# Name: Sarah Mahan, Luke Ransick, Josh Klingelhafer, Henry Gruber
# email:  mahansa@mail.uc.edu, ransiclg@mail.uc.edu, klingejh@mail.uc.edu, gruberhw@mail.uc.edu
# Assignment Number: Assignment 11
# Due Date:   11/21/24
# Course #/Section:   IS4010 001
# Semester/Year:   Fall 2024
# Brief Description of the assignment:   Clean a csv file, store it in a new place.
# Brief Description of what this module does. What this module does is that it's a class, and inside this class is a function that filters anomalies, in this case it's filtering pepsi out of the fuel type column. It then writes the rows with pepsi as fuel type into a new csv caled dataAnomalies and gets stored in the Data folder. 
# Citations:
# Anything else that's relevant: Using (allowed) AI, Copilot

# dataAnomalies/filter_anomalies.py
import csv
from CSVPackage.CSVProcessor import CSVProcessor

class RemoveAnomaliesInColumn:
    """
    Removes anomalies in rows from the fuel column.
    """
    def __init__(self, csv_processor):
        """
        Constructor
        
        Args:
            csv_processor (CSVProcessor): An instance of the CSVProcessor class.
        """
        self.csv_processor = csv_processor

    def filter_anomalies(self, anomalies_file):
        """
        Filters out rows where 'fuel type' is 'Pepsi'.
        
        Args:
            anomalies_file (str): The path to save the anomalies CSV file.
        """
        data = self.csv_processor.process()
        header = data[0]
        rows = data[1:]

        with open(anomalies_file, 'w', newline='') as anomaliesfile:
            writer = csv.writer(anomaliesfile)
            writer.writerow(header)
            
            cleaned_data = [header]  # Keep the header in the cleaned data
            for row in rows:
                if row[5].lower() == 'pepsi':  # Assuming 'fuel type' is the 5th column
                    writer.writerow(row)
                else:
                    cleaned_data.append(row)
        
        # Optionally, save cleaned data to a new file
        cleaned_file = 'Data/cleaned_data.csv'
        with open(cleaned_file, 'w', newline='') as cleanedfile:
            writer = csv.writer(cleanedfile)
            writer.writerows(cleaned_data)

    def __str__(self):
        """
        @return String: A human-readable basic representation of the current object. 
        """
        return "csv_processor is: " + self.__csv_processor

    def __repr__(self):
        """
        @return String: A string containing code that can be executed to create a copy of the current object
        """
        return f"csv_processor is('{self.__csv_processor}')" 
        