import os
import logging

def setup_logging(log_file_name):
    """
    Sets up logging with a specified log file name.

    :param log_file_name: Name of the log file.
    """
    # Delete the log file if it already exists
    if os.path.exists(log_file_name):
        os.remove(log_file_name)

    logging.basicConfig(filename=log_file_name, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_files_in_directory(directory):
    """
    Logs all files in the specified directory and its subdirectories.

    :param directory: The root directory to scan for files.
    """
    if not os.path.isdir(directory):
        log_file_name = f"folder_map_{os.path.basename(directory.rstrip(os.sep))}_log.txt"
        setup_logging(log_file_name)
        
        logging.error(f"Directory does not exist: {directory}")
        print(f"The directory '{directory}' does not exist. No log file created.")
        return

    folder_name = os.path.basename(directory.rstrip(os.sep))
    log_file_name = f"folder_map_{folder_name}_log.txt"
    
    setup_logging(log_file_name)
    
    logging.info(f"Scanning directory: {directory}")
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            logging.info(f"File: {file_path}")

    logging.info("Directory scan completed.")
    print(f"Directory contents have been logged to {log_file_name}")

if __name__ == "__main__":
    directory_to_scan = "D:\\G"  # Replace with your target directory

    log_files_in_directory(directory_to_scan)
