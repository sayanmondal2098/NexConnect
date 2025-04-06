import requests

def download_google_sheet(sheet_url, output_file):
    try:
        # Convert the Google Sheet URL to the CSV export URL
        if "edit#gid=" in sheet_url:
            base_url = sheet_url.split("/edit#gid=")[0]
            csv_url = base_url + "/export?format=csv"
        else:
            raise ValueError("Invalid Google Sheet URL format")

        # Fetch the CSV data from the public Google Sheet
        response = requests.get(csv_url)
        response.raise_for_status()  # Raise HTTPError for bad responses

        # Save the data to a local file
        with open(output_file, "wb") as file:
            file.write(response.content)

        print(f"Google Sheet data downloaded successfully and saved to '{output_file}'")

    except Exception as e:
        print(f"An error occurred: {e}")

