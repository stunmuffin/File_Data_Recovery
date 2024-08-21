import os
import shutil
import logging
from datetime import datetime
import sys
import ctypes

# Increase recursion limit for deeply nested directories
sys.setrecursionlimit(10000)

def setup_logging(file_name, file_extension=None):
    """
    Sets up logging with a file name based on the file extension.

    :param file_name: Base name for the log file.
    :param file_extension: Optional file extension to include in the log file name.
    """
    log_file = f"recovery_log_{file_name}{file_extension}.txt" if file_extension else f"recovery_log_{file_name}.txt"
    logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def recover_single_file(source_file, dest_dir):
    """
    Recovers a single file from the source to the destination directory.
    
    :param source_file: The file to be recovered.
    :param dest_dir: The directory where the recovered file should be placed.
    """
    if not os.path.isfile(source_file):
        logging.error(f"Source file does not exist: {source_file}")
        return

    # Check if there's at least 100 MB of free space on the destination drive
    if not check_free_space(dest_dir, 100):
        logging.error("Not enough free space on the destination drive. Please ensure there is at least 100 MB of free space.")
        return

    setup_logging(".file")  # Use a unique log file for file recovery

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    dest_file = os.path.join(dest_dir, os.path.basename(source_file))
    dest_file = generate_unique_filename(dest_file)
    dest_file = shorten_path(dest_file)
    
    try:
        shutil.copy2(source_file, dest_file)
        logging.info(f"Recovered: {source_file} -> {dest_file}")
        print("File recovery completed successfully.")  # Print completion message
    except Exception as e:
        logging.error(f"Failed to recover: {source_file}. Error: {e}")
        print("File recovery failed.")  # Print failure message


def generate_unique_filename(dest_file):
    """
    Generates a unique filename by appending a timestamp or counter to avoid overwriting.
    
    :param dest_file: The path to the file where a unique name is needed.
    :return: A unique file name.
    """
    base, ext = os.path.splitext(dest_file)
    counter = 1
    while os.path.exists(dest_file):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dest_file = f"{base}_{timestamp}{ext}"
        counter += 1
    return dest_file

def get_relative_path(source_dir, file_path):
    """
    Gets the relative path of a file with respect to the source directory.
    
    :param source_dir: The source directory.
    :param file_path: The full path of the file.
    :return: The relative path of the file.
    """
    return os.path.relpath(file_path, source_dir)

def shorten_path(path, max_length=255):
    """
    Shortens a path to fit within the maximum path length limit.
    
    :param path: The original path to shorten.
    :param max_length: The maximum allowed length of the path.
    :return: A shortened path.
    """
    if len(path) <= max_length:
        return path
    
    head, tail = os.path.split(path)
    head = shorten_path(head, max_length - len(tail) - 1)
    return os.path.join(head, tail)

def check_free_space(directory, required_space_mb):
    """
    Checks if the drive containing the specified directory has enough free space.
    
    :param directory: Directory to check.
    :param required_space_mb: Required space in MB.
    :return: True if there's enough space, False otherwise.
    """
    if os.name == 'nt':  # For Windows
        free_bytes = ctypes.c_ulonglong(0)
        total_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(directory, None, ctypes.pointer(total_bytes), ctypes.pointer(free_bytes))
        free_space_mb = free_bytes.value / (1024 * 1024)  # Convert bytes to MB
        return free_space_mb >= required_space_mb
    else:  # For Unix-like systems
        statvfs = os.statvfs(directory)
        free_space_mb = (statvfs.f_frsize * statvfs.f_bavail) / (1024 * 1024)  # Convert bytes to MB
        return free_space_mb >= required_space_mb

def recover_files(source_dir, dest_dir, file_extensions=None):
    """
    Recovers files from the source directory to the destination directory.
    
    :param source_dir: Directory where the files to be recovered are located.
    :param dest_dir: Directory where recovered files should be placed.
    :param file_extensions: List of file extensions to filter by.
    """
    if not os.path.isdir(source_dir):
        logging.error(f"Source directory does not exist: {source_dir}")
        return

    # Check if there's at least 5 GB of free space on the destination drive
    if not check_free_space(dest_dir, 5000):
        logging.error("Not enough free space on the destination drive. Please ensure there is at least 5 GB of free space.")
        return

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    try:
        shutil.copy2(src_file, dest_file)
        logging.info(f"Recovered: {src_file} -> {dest_file}")
        files_recovered += 1
    except Exception as e:
        logging.error(f"Failed to recover: {src_file}. Error: {e}\n{traceback.format_exc()}")
    
    if file_extensions:
        for ext in file_extensions:
            # Create subfolders based on each file extension
            main_folder = os.path.join(dest_dir, f"Recovered {ext.upper()} Files")
            setup_logging(ext)
            
            if not os.path.exists(main_folder):
                os.makedirs(main_folder)
            
            logging.info(f"Recovery process started for {ext.upper()} files from {source_dir} to {main_folder}")
            
            files_recovered = 0
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    if file.endswith(ext):
                        src_file = os.path.join(root, file)
                        relative_path = get_relative_path(source_dir, src_file)
                        file_folder = os.path.join(main_folder, os.path.dirname(relative_path))
                        
                        # Create the necessary directories
                        if not os.path.exists(file_folder):
                            os.makedirs(file_folder)
                        
                        dest_file = os.path.join(file_folder, file)
                        
                        # Ensure unique file name
                        dest_file = generate_unique_filename(dest_file)
                        
                        # Shorten path if necessary
                        dest_file = shorten_path(dest_file)
                        
                        try:
                            shutil.copy2(src_file, dest_file)
                            logging.info(f"Recovered: {src_file} -> {dest_file}")
                            files_recovered += 1
                        except Exception as e:
                            logging.error(f"Failed to recover: {src_file}. Error: {e}")
            
            logging.info(f"Recovery process completed for {ext.upper()} files. Total files recovered: {files_recovered}")

def log_directory_contents(root_dir, log_prefix):
    """
    Logs the directory structure and files within the specified root directory.
    
    :param root_dir: The root directory to log.
    :param log_prefix: Prefix for the log file to identify the type of content being logged.
    """
    setup_logging(log_prefix)
    logging.info(f"Logging directory contents for: {root_dir}")

    for root, dirs, files in os.walk(root_dir):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            logging.info(f"Directory: {os.path.relpath(dir_path, root_dir)}")
        
        for file_name in files:
            file_path = os.path.join(root, file_name)
            logging.info(f"File: {os.path.relpath(file_path, root_dir)}")

def recover_folder(source_folder, dest_folder):
    """
    Recovers an entire folder from the source directory to the destination directory,
    maintaining the original folder structure and logging details.
    
    :param source_folder: Folder to be recovered.
    :param dest_folder: Directory where the recovered folder should be placed.
    """
    if not os.path.isdir(source_folder):
        logging.error(f"Source folder does not exist: {source_folder}")
        return

    # Check if there's at least 100 MB of free space on the destination drive
    if not check_free_space(dest_folder, 100):
        logging.error("Not enough free space on the destination drive. Please ensure there is at least 100 MB of free space.")
        return

    setup_logging(".folder")  # Use a unique log file for folder recovery

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    folder_name = os.path.basename(source_folder)
    dest_folder = os.path.join(dest_folder, folder_name)

    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    
    logging.info(f"Recovery process started for folder {source_folder} to {dest_folder}")

    try:
        # Maintain a stack for directory traversal to avoid recursion
        stack = [(source_folder, dest_folder)]
        while stack:
            current_source_dir, current_dest_dir = stack.pop()
            
            for item in os.listdir(current_source_dir):
                src_path = os.path.join(current_source_dir, item)
                dest_path = os.path.join(current_dest_dir, item)

                if os.path.isdir(src_path):
                    if not os.path.exists(dest_path):
                        os.makedirs(dest_path)
                        logging.info(f"Created directory: {os.path.relpath(dest_path, dest_folder)}")
                    # Add the directory to the stack to process its contents
                    stack.append((src_path, dest_path))
                else:
                    # Handle file recovery
                    dest_file = generate_unique_filename(dest_path)
                    dest_file = shorten_path(dest_file)

                    try:
                        shutil.copy2(src_path, dest_file)
                        logging.info(f"Recovered: {src_path} -> {dest_file}")
                    except Exception as e:
                        logging.error(f"Failed to recover: {src_path}. Error: {e}")

        logging.info(f"Successfully recovered folder: {source_folder} -> {dest_folder}")
        print("Recovery process completed successfully.")  # Print completion message
        
    except Exception as e:
        logging.error(f"Failed to recover folder: {source_folder}. Error: {e}")
        print("Recovery process failed.")  # Print failure message


if __name__ == "__main__":
    source_directory = "Source Directory"
    destination_directory = "Destination Directory"
    
    # Recover specific file types
    # extensions = [".jpg", ".jpeg", ".tif", ".tiff", ".png", ".psd"]  # List of file extensions
    # recover_files(source_directory, destination_directory, extensions)
    
    # Recover an entire folder
    folder_to_recover = "Recover Folder or File Name"  # Replace with the folder you want to recover
    folder_name = os.path.basename(folder_to_recover)
    setup_logging(folder_name + "_folder")  
    recover_folder(folder_to_recover, destination_directory)

    # If you have a single file then use this
    #recover_single_file(folder_to_recover, destination_directory)


