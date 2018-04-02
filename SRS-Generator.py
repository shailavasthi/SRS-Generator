# Generates a random sample from a population list.
# Population lists must be CSV files with the headers formatted as follows: Last Name,Full Name,Current Grade,Gender
# CSV files must be in the same directory pathway as this script.
# If they are located elsewhere, a file path should be provided when calling get_list() for the list argument

import random, pandas as pd


def get_list(list, sample_size):
    def get_index(sample_size, population):
        # Generates a list of random integers to be used to index the population data frame
        # Length of list is the sample size
        # List contains randomly selected values from 0 to the size of the population minus 1
        index = []
        i = 1
        while i <= sample_size:
            randint = random.randint(0, population - 1)
            if randint not in index:
                index.append(randint)
                i += 1
            else:
                i += 0

        return index

    # CSV file is converted to a pandas data frame, and population size is determined
    df = pd.read_csv(list)
    population = df.shape[0]
    # List of random integers used to index data frame is generated
    index = get_index(sample_size, population)
    # List of randomly selected names is initiated
    sample_list = []
    # Full names are selected using the randomly generated index number and added to the sample
    for i in index:
        sample_list.append(df['Full Name'][i])

    return sample_list

print(get_list('Males.csv', 70))
print(get_list('Females.csv', 70))
print(get_list('Underclassmen.csv', 40))
print(get_list('Upperclassmen.csv', 40))