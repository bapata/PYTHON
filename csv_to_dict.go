package main

// convert file of the following format to a dictionary/JSON
// LOCATION,VIP1,VIP2
// location1,vip1a,vip1b
// location2,vip2a,vip2b
// TO
// { 'location1': { 'LOCATION':'location1','VIP1':'vip1a' ..}, 'location2': {'LOCATION':'location2':'vip2a' ..} }

// OR
// LOCATION,VIP1,VIP2,VIP3
// location1,vip1a,vip1b,vip1c
// location2,vip2a,vip2b,vip1c




import (
	"encoding/csv"
	"encoding/json"
	"fmt"
	"io"
	"os"
)

func main() {
	// Open the CSV file
	file, err := os.Open("myvalues.csv")
	if err != nil {
		fmt.Println("Error opening file:", err)
		return
	}
	defer file.Close()

	// Create a new CSV reader
	reader := csv.NewReader(file)

	// Read the header line of the CSV file
	header, err := reader.Read()
	if err != nil {
		fmt.Println("Error reading header:", err)
		return
	}

	// Create a map to store the data
	data := make(map[string]map[string]string)

	// Loop over the remaining rows of the CSV file
	for {
		// Read the next record
		record, err := reader.Read()
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Println("Error reading record:", err)
			return
		}

		// Create a map to store the values for this record
		values := make(map[string]string)

		// Loop over the fields in the record
		for i, field := range record {
			// Store the field in the values map using the header as the key
			values[header[i]] = field
		}

		// Store the values map in the data map using the first field as the key
		data[record[0]] = values
	}

	// Print the data map
	fmt.Println(data)
	// Convert the map to a JSON string
	jsonData, err := json.Marshal(data)
	if err != nil {
		fmt.Println("Error marshaling JSON:", err)
		return
	}
	fmt.Println(string(jsonData))
}
