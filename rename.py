import os
def get_file_creation_time(file_path):
    return os.path.getctime(file_path)

def rename(src, countNum):
    # Change directory to the specified folder
    os.chdir(src)

    # Get a list of all files in the folder
    files = os.listdir(src)

    # Filter only image files (you can customize this based on your file extensions)
    image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Sort the list of image files alphabetically
    image_files.sort()
    count = countNum
    # Iterate through the sorted image files and rename them
    for index, old_name in enumerate(image_files, start=1):
        # Extract the file extension
        file_extension = os.path.splitext(old_name)[1]

        # Construct the new file name with the specified prefix and index
        new_name = f"{count}{file_extension}"

        # Rename the file
        os.rename(old_name, new_name)
        count += 1
        print(f"Renamed: {old_name} -> {new_name}")


    print('All Files Renamed')
    print('New Names are')
    # verify the result
    res = os.listdir(src)
    print(res)