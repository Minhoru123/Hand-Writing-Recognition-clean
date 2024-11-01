import zipfile
import os
import shutil

def unzip_and_organize(zip_file, extract_to='data/'):
    # Unzip the file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    
    print('Data extracted successfully')

    # Define paths
    base_folder = extract_to
    train_folder = os.path.join(base_folder, 'train_v2/train/')
    test_folder = os.path.join(base_folder, 'test_v2/test/')
    validation_folder = os.path.join(base_folder, 'validation_v2/validation/')

    # Create directories if they don't exist
    os.makedirs('data/train_v2/', exist_ok=True)
    os.makedirs('data/test_v2/', exist_ok=True)
    os.makedirs('data/validation_v2/', exist_ok=True)

    # Move files to the appropriate directories
    for subdir, new_subdir in [(train_folder, 'data/train_v2/'), 
                               (test_folder, 'data/test_v2/'), 
                               (validation_folder, 'data/validation_v2/')]:
        if os.path.exists(subdir):
            for filename in os.listdir(subdir):
                shutil.move(os.path.join(subdir, filename), new_subdir)

    print('Data organized into train, test, and validation folders.')

# Run the function
unzip_and_organize('data/Handwriting.zip')
