# File_Data_Recovery
File_Data_Recovery is a Python-based tool designed to recover files and folders from a source directory to a destination directory. This utility supports the following features:

Directory and File Recovery: Recovers entire folders or specific files while preserving the original directory structure.
File Type Filtering: Optionally filters files by their extensions for selective recovery.
Unique Filename Handling: Avoids overwriting by generating unique filenames if necessary.
Path Shortening: Ensures that file paths do not exceed the maximum length limits.
Free Space Check: Verifies that there is sufficient free space on the destination drive before starting the recovery process.
Logging: Provides detailed logging of the recovery process, including successful and failed operations.
Use this tool to efficiently recover lost or accidentally deleted files while maintaining their original structure and organization.

"# No external packages are required for this script"



#Main File

File_Data_Recovery.py


#Folder or File Name Mapper

folder_map_finder.py


#Folder or File Name
      
     directory_to_scan = "D:\\G"  # Replace with your target directory

# Recover an entire folder
    folder_to_recover = "Your Destination Place"  # Replace with the folder you want to recover

# If you have a single file then use this
    recover_single_file(folder_to_recover, destination_directory)
