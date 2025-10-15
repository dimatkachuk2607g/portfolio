"""
Data Analysis Project

This project's aim is to clean a sample pokemon_data.csv file, taking care of blank rows,
duplicates, missing values and force the right type for each column mainly using pandas,
the key information is then displayed using matplotlib pie chart
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def load_csv_data():
    """Load the csv file and check for errors"""
    try:
        csv_path = Path(__file__).parent / "pokemon_data.csv"
        df = pd.read_csv(csv_path)
        return df
    except FileNotFoundError as error:
        raise RuntimeError(f'{error}')


def remove_duplicates_and_empty_rows(df):
    """Remove empty rows and duplicates from the dataframe"""
    df = df.dropna(how='all')
    df = df.drop_duplicates()
    return df


def fill_missing_values(df):
    """Fill any missing NA values"""
    df["Type2"] = df["Type2"].fillna("Doesn't exist")
    df["Height"] = df["Height"].fillna(df["Height"].median())
    df["Weight"] = df["Weight"].fillna(df["Weight"].median())
    return df


def force_correct_types(df):
    """Force the right variable type for each column"""
    df["Name"] = df["Name"].astype(str)
    df["Type1"] = df["Type1"].astype(str)
    df["Type2"] = df["Type2"].astype(str)
    df["Height"] = df["Height"].astype(float)
    df["Weight"] = df["Weight"].astype(float)
    df["Legendary"] = df["Legendary"].astype(int)
    return df


def create_clean_csv(df):
    """After cleaning is done, creates a new clean CSV file"""
    df.to_csv("pokemon_data_clean.csv", index=False)



def open_clean_csv():
    """Opens the new CSV file and check for errors"""
    try:
        df = pd.read_csv("pokemon_data_clean.csv")
        return df
    except FileNotFoundError as error:
        raise RuntimeError(f'{error}')


def create_type1_pie_chart(df):
    """Creates a pie chart for the Type1 category"""
    category_series = df["Type1"].value_counts()

    counts = np.array(category_series)
    labels = np.array(category_series.index)

    plt.figure(figsize=(8, 8)) # increase size of pie chart
    plt.pie(counts,
            labels=labels,
            autopct='%1.2f%%',
            textprops = {'fontweight': 'bold'},
    )

    plt.title("Pokémon Types Overview", fontsize=20, fontweight="bold")
    plt.show()





def main():
    """Activation of all functions to clean, create and open the new file,
    also creates a pie chart displaying the types by popularity"""
    df = load_csv_data() # load the CSV file
    df = remove_duplicates_and_empty_rows(df) # Remove duplicates and empty rows
    df = fill_missing_values(df) # fills any missing values with appropriate replacements
    df = force_correct_types(df) # Forces the type of each column to be correct
    create_clean_csv(df) # exports the cleaned dataframe to a new CSV file
    df = open_clean_csv() # opens the cleaned file to be used for plotting
    create_type1_pie_chart(df) # plots the Type1 column with a pie chart
    print(df) # print 10 rows from the clean dataframe
    # print(df.to_string()) # prints the entire dataframe (150 rows), remove initial # to run



if __name__ == "__main__":
    main()