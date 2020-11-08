import requests
import json

start_number = 1

data = requests.get("https://api.covid19api.com/summary").text
info = json.loads(data)

scale = str(input("Global or Countries : "))

if scale == "Global":
	print("\nNewConfirmed\nTotalConfirmed\nNewDeaths\nTotalDeaths\nNewRecovered\nTotalRecovered\n")
	info_request = str(input("What information do you want? : "))
	print(info["Global"][info_request])

if scale == "Countries":
	while start_number != 189:
		print(str(start_number) + " = " + info["Countries"][start_number]["Country"])
		start_number += 1

	countryID = int(input("\nCountryID # : "))
	print("\nCountryCode\nSlug\nNewConfirmed\nTotalConfirmed\nNewDeaths\nTotalDeaths\nNewRecovered\nTotalRecovered\n")
	info_request = str(input("Information Request: "))
	print("\n" + str(info["Countries"][countryID][info_request]) + "\n")