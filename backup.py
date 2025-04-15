import os 
import shutil 
import sys 
import time 

def backup_files(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.isdir(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        os.makedirs(source_dir)  
    
    # Check if destination directory exists, create if not
    if not os.path.isdir(dest_dir):
        print(f"Destination directory '{dest_dir}' does not exist. Creating it now...")
        os.makedirs(dest_dir)  
        
    # Loop through files in the source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        
        # Ensure it's a file, not a directory
        if os.path.isfile(source_file):
            dest_file = os.path.join(dest_dir, filename)
            
            # If file exists in destination, append timestamp
            if os.path.exists(dest_file):
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                name, ext = os.path.splitext(filename)
                dest_file = os.path.join(dest_dir, f"{name}_{timestamp}{ext}") 
            
            # Try copying the file
            try: 
                shutil.copy2(source_file, dest_file)
                print(f"File '{filename}' copied to '{dest_file}'.") 
            except Exception as e: 
                print(f"Error copying file '{filename}': {e}")

# Entry point
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)
