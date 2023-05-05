import csv

# Generate performance testing data for SA algorithm
# Set up the CSV writer
with open('SA_1P_testingData.csv', mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # Write the headers
    writer.writerow(['Test_ID','numGames','numParlays','runtime','temp_threshold','SA_Correctnes', 'SA_Offset'])

    # Set up initial values for each attribute
    SA_Correctness = 0
    SA_Offset = 0
    temp_threshold = 0
    runtime = 0
    numGames = 0
    numParlays = 0 
    numTests = 1100
    test_id = 100

    # Loop through and generate each row of data
    for i in range(numTests):
        # Import numGames from outputfile
        numGames = input()

        # Import numParlays from outputfile
        numParlays = input()

        # Import runtime from outputfile
        runtime = input()

        # Import temp_threshold from outputfile
        temp_threshold = input()

        # Import SA_Correctness from outputfile
        SA_Correctness = input()

        # Import SA_Offset from outputfile
        SA_Offset = input()

        # Write the row
        writer.writerow([test_id, numGames, numParlays, runtime, temp_threshold, SA_Correctness, SA_Offset])

        # Increment the test_id
        test_id += 1