import csv

# Generate performance testing data for SA algorithm
# Set up the CSV writer
with open('SA_MP_testingData_g10+BF.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the headers
    writer.writerow(['Test_ID','numGames','numParlays','runtime'])

    # Set up initial values for each attribute
    SA_Correctness = 0
    SA_Offset = 0
    temp_threshold = 0
    runtime = 0
    numGames = 0
    numParlays = 0 
    numTests = 300
    test_id = 0
    SA_Best_Overlap = 0

    # Loop through and generate each row of data
    for i in range(numTests):
        # Import numParlays from outputfile
        numParlays = input()

        # Import numGames from outputfile
        numGames = input()

        # Import runtime from outputfile
        runtime = input()

        # Write the row
        writer.writerow([test_id, numGames, numParlays, runtime])

        # Increment the test_id
        test_id += 1