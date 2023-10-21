# connect to google spreadsheets and add new entries
import gspread
from oauth2client.service_account import ServiceAccountCredentials


async def add_user(userid:str,passoutyear:int,department:str, college:str):
    # Define the scope and credentials
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials.json", scope)

    # Authorize the client with the credentials
    client = gspread.authorize(creds)

    # Open the spreadsheet by its title
    spreadsheet = client.open("Community Roster")

    # Select the first worksheet within the spreadsheet
    worksheet = spreadsheet.get_worksheet(0)

    # Append a new row to the worksheet
    new_entry = [userid,passoutyear,department,college]
    worksheet.append_row(new_entry)