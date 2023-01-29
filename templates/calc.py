import csv

def average():
    """
    open()
    readline()
    """
    list_of_states = ["CA", "MN", "WA"]
    # opening the CSV file
    with open('crime_vs_income.csv', mode ='r')as file:
    
        # reading the CSV file
        csvFile = csv.reader(file)
        
        # displaying the contents of the CSV file
        for row in csvFile:
            state = row[3]
            if state == :
            # print(f"total_violent_crime: {row[0]}, household_income: {row[1]}")
                print(f"{row}")

    # go through each column to search for the county and gather to each state

def group_county_to_state():
    pass


if __name__ == "__main__":
    average()