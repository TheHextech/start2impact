import os
import shutil
import csv
import argparse


"""to make it work digit 'cd' and paste the absolute file path of this executable in the CMD."""



CWD = os.getcwd()
DESIRED_PATH = CWD + '/files'
os.chdir(DESIRED_PATH)


files_list = os.listdir()


extensions = {
    "image": [".jpg", ".jpeg", ".png"],
    "doc": [".doc", ".txt", ".odt"],
    "audio": [".mp3"]
}


item = argparse.ArgumentParser(description="This executable can move a single file inside the 'files' folder, into its parental folder, updating information into 'recap.csv' file. You have to digit file name, format included, you wish to move (e.g. 'textfile.txt').")

item.add_argument("target_file", type=str, choices=(files_list), help="Write name of the file to move, format included (e.g. 'audio.mp3').")

args = item.parse_args()


def move_file(target_file):
    with open('recap.csv', 'a') as csv_file:

        fieldnames = ['name', 'type', 'size(B)']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        if os.path.getsize('recap.csv') == 0:
            csv_writer.writeheader()

        if os.path.isfile(target_file) and target_file in files_list:
            filename, file_ext = os.path.splitext(target_file)
            file_size = os.path.getsize(target_file)

            for key in extensions:

                if file_ext in extensions[key]:
                    files_destination_folder = key

                    if not os.path.isdir(files_destination_folder):
                        os.mkdir(files_destination_folder)

                    file_details = [{
                        'name': filename,
                        'type': key,
                        'size(B)': file_size
                    }]

                    csv_writer.writerows(file_details)

                    print(
                        f"Successful operation. '{target_file}' file was moved into '{files_destination_folder}' folder and the recap file was updated.")

                    return shutil.move(target_file, f"{files_destination_folder}/{target_file}")

        else:
            return f"'{target_file}' file doesn't exist into 'files' fodler, or its extension may not have been explained (e.g. 'text.txt')."


move_file(args.target_file)
