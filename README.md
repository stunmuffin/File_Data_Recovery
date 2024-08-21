# File Data Recovery
File Data Recovery is a Python-based tool designed to recover files and folders from a source directory to a destination directory. This utility supports the following features:

Directory and File Recovery: Recovers entire folders or specific files while preserving the original directory structure.
File Type Filtering: Optionally filters files by their extensions for selective recovery.
Unique Filename Handling: Avoids overwriting by generating unique filenames if necessary.
Path Shortening: Ensures that file paths do not exceed the maximum length limits.
Free Space Check: Verifies that there is sufficient free space on the destination drive before starting the recovery process.
Logging: Provides detailed logging of the recovery process, including successful and failed operations.
Use this tool to efficiently recover lost or accidentally deleted files while maintaining their original structure and organization.

No external packages are required for this script.



# Single File Recovery

Step 1: Go and open "folder_map_finder.py" and Please specify a folder to search and use double '\\\' like D:\\\G\\\Myfolder 

![Screenshot_4](https://github.com/user-attachments/assets/a14aac16-6623-4278-9fa2-62980c64bf42)

Step 2: Run the code on Visual Studio or IDE or command

![Screenshot_5](https://github.com/user-attachments/assets/9059af4d-bb0f-4dbb-b8d1-6feac3be0aa9)

Step 3: Control your  "folder_map_finder.py" folder it creates logs until you stop the code.

![Screenshot_2](https://github.com/user-attachments/assets/fe871f0f-d30c-40a9-b387-aad159a678ba)

Step 4: Stop until you specify to recover folder or file in log or if you remember the name you can check from "folder_map_finder.py" directory_to_scan = "D:\\G\\Your_folder" or   "D:\\G\\Your_file.jpg", ...vs.

![Screenshot_6](https://github.com/user-attachments/assets/f4c9054a-ca8e-4a2b-84b6-7663b05d744d)

Step 5: If you want to recover a folder Use the  "folder_map_finder.py" and create a log that you can see the main file system recover folder.

Step 6: If you want to recover just 1 File (.Jpg, jpeg, .exe , .psd  ,....vs. all file format) go to "File_Data_Recovery.py" 

![Screenshot_7](https://github.com/user-attachments/assets/f4d2ab34-5b6c-4e3a-a9ad-bf67aca8ab4b)

![Screenshot_8](https://github.com/user-attachments/assets/963cf1cf-8473-494f-8182-8a4cff06e150)


# Folder Recovery Process

![Screenshot_9](https://github.com/user-attachments/assets/ab909dcb-5b17-4111-919a-b9b0d1c4fa2f)

Folder name must be like this : >> D:\\FOLDER_NAME not the >> D:\\FOLDER_NAME\\

![Screenshot_10](https://github.com/user-attachments/assets/de4a52bc-ad55-4f1f-89c9-938dea85931d)

Hope this helps!


#Folder or File Name

     directory_to_scan = "D:\\G"  # Replace with your target directory

# Recover an entire folder
    folder_to_recover = "Your Destination Place"  # Replace with the folder you want to recover

# If you have a single file then use this
    recover_single_file(folder_to_recover, destination_directory)
