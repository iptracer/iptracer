#!/bin/bash

# Ensure the necessary Python script is present
if [ ! -f ip_location.py ]; then
    echo "ip_location.py not found! Please ensure the script is in the same directory."
    exit 1
fi

# Display a welcome message
figlet "IP Location Fetcher" | lolcat

# Prompt the user for an IP address
echo -n "Enter the IP address: "
read ip_address

# Run the Python script and capture the output
output=$(python ip_location.py $ip_address)

# Display the result
figlet "Result" | lolcat
echo "$output" | lolcat
