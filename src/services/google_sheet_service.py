from src.connectors.google_sheet_connector import download_google_sheet


def download_google_sheet(sheet_url):
    output_file = "data.csv"
    download_google_sheet(sheet_url)

