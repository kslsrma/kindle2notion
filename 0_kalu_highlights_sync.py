import shutil
import os
from datetime import datetime

def get_user_choice():
    choice = input("Do you want to download a new file from the Kindle? (yes/no): ").strip().lower()
    return choice == 'yes'

def download_new_file(source_file, destination_dir):
    # Ensure the destination directory exists
    os.makedirs(destination_dir, exist_ok=True)

    # Determine the new file name with today's date
    today_date = datetime.today().strftime('%Y-%m-%d')
    new_file_name = f"My Clippings_kalu {today_date}.txt"
    destination_file = os.path.join(destination_dir, new_file_name)

    # Copy and rename the file
    shutil.copy(source_file, destination_file)
    return destination_file

def get_most_recent_file(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory)]
    
    if not files:  # Check if the list is empty
        raise FileNotFoundError(f"No files found in the directory: {directory}")
    
    return max(files, key=os.path.getctime)

def main():
    source_file = '/Volumes/Kindle/documents/My Clippings.txt'
    destination_dir = '/Users/kushal/Documents/kindle_words_highlights/highlights_kindle/kalu'

    if get_user_choice():
        kindle_clippings_file = download_new_file(source_file, destination_dir)
    else:
        try:
            kindle_clippings_file = get_most_recent_file(destination_dir)
        except FileNotFoundError as e:
            print(e)
            return  # Exit the script if no file is found

    # Step 4: Run the command with the correct path
    notion_auth_token = "secret_dVaMtOuZfk4tfzVMinXnPEmyKwbGm0b3iVbNnjRSLw0"
    notion_table_id = "9a1835a053064b06a1ce0af4ef26335d"
    
    command = f'kindle2notion "{notion_auth_token}" "{notion_table_id}" "{kindle_clippings_file}"'
    os.system(command)

if __name__ == "__main__":
    main()