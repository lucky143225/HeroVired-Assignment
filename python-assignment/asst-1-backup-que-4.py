import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    """
    Backup files from source directory to destination directory.
    """
    try:
        # Check if source directory exists
        if not os.path.exists(source_dir):
            print("Error: Source directory does not exist.")
            return

        # Create destination directory if it does not exist
        if not os.path.exists(dest_dir):
            print("Dist_dir does not exit, creating....")
            os.makedirs(dest_dir)
            print(f"Dist_dir has created: {dest_dir}")

        # Iterate over files in the source directory
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            dest_file = os.path.join(dest_dir, filename)

            # Check if destination file already exists
            if os.path.exists(dest_file):
                # Append timestamp to the filename to ensure uniqueness
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                dest_file = os.path.join(dest_dir, f"{os.path.splitext(filename)[0]}_{timestamp}{os.path.splitext(filename)[1]}")

            # Copy the file to the destination directory
            shutil.copy2(source_file, dest_file)

            print(f"Copied: {source_file} -> {dest_file}")

        print("Backup completed successfully.")

    except FileNotFoundError:
        print("Error: Source directory or destination directory not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Check if source directory and destination directory are provided as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python backup.py /path/to/source /path/to/destination")
        sys.exit(1)

    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]

    # Perform backup
    backup_files(source_dir, dest_dir)

