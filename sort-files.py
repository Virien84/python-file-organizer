from pathlib import Path

# Define the path using Path
current_directory = Path.cwd()

# List the contents of the current directory
contents = list(current_directory.iterdir())

# Dictionary of extensions and their corresponding folders
extension_folders = {
    # Microsoft Office documents
    '.doc': 'documents',
    '.docx': 'documents',
    '.xls': 'documents',
    '.xlsx': 'documents',
    '.ppt': 'documents',
    '.pptx': 'documents',
    '.accdb': 'documents',
    '.pub': 'documents',
    '.one': 'documents',
    '.rtf': 'documents',
    '.odt': 'documents',
    '.ods': 'documents',
    '.odp': 'documents',
    '.pdf': 'documents',
    '.txt': 'documents',
    
    # Image files
    '.jpg': 'images',
    '.jpeg': 'images',
    '.png': 'images',
    '.gif': 'images',
    '.bmp': 'images',
    '.tiff': 'images',
    '.webp': 'images',
    '.svg': 'images',
    '.ico': 'images',
    '.raw': 'images',
    '.cr2': 'images',
    '.nef': 'images',
    '.ai': 'images',
    '.psd': 'images',
    '.xcf': 'images',
    
    # Audio files
    '.mp3': 'audio',
    '.wav': 'audio',
    '.wma': 'audio',
    '.aac': 'audio',
    '.ogg': 'audio',
    '.flac': 'audio',
    '.m4a': 'audio',
    '.mid': 'audio',
    '.midi': 'audio',
    
    # Video files
    '.mp4': 'videos',
    '.avi': 'videos',
    '.mkv': 'videos',
    '.mov': 'videos',
    '.wmv': 'videos',
    '.flv': 'videos',
    '.webm': 'videos',
    '.m4v': 'videos',
    '.mpeg': 'videos',
    '.mpg': 'videos',
    '.3gp': 'videos',
    
    # Compressed files
    '.zip': 'compressed',
    '.rar': 'compressed',
    '.7z': 'compressed',
    '.gz': 'compressed',
    '.tar': 'compressed',
    '.bz2': 'compressed',
    
    # Design and CAD files
    '.dwg': 'design',
    '.dxf': 'design',
    '.eps': 'design',
    '.cdr': 'design',
    '.skp': 'design',

    # Development files
    '.py': 'code',
    '.java': 'code',
    '.cpp': 'code',
    '.c': 'code',
    '.html': 'code',
    '.css': 'code',
    '.js': 'code',
    '.php': 'code',
    '.sql': 'code'
}

# Declare empty lists and counters before the loop
folders = []
files = []
files_not_moved = 0
files_moved = 0

for item in contents:
    if item.is_file():
        files.append(item)
    elif item.is_dir():
        folders.append(item)

# Create necessary directories based on found extensions
for file in files:
    extension = file.suffix.lower()  # get extension in lowercase
    
    # Determine target folder
    if extension in extension_folders:
        folder_name = extension_folders[extension]
    else:
        folder_name = 'others'
        if extension:
            print(f"Unrecognized extension: {extension}")
        else:
            print(f"File without extension: {file.name}")
    
    # Create folder if it doesn't exist
    target_folder = current_directory / folder_name
    if not target_folder.exists():
        target_folder.mkdir()
        print(f"Created folder: {folder_name}")
    
    # Move file to corresponding folder
    try:
        target_file = target_folder / file.name
        if target_file.exists():
            print(f"Warning! {file.name} already exists in {folder_name}")
            files_not_moved += 1
        else:
            file.rename(target_file)
            print(f"Moved {file.name} to {folder_name}")
            files_moved += 1
    except Exception as e:
        print(f"Error moving {file.name}: {str(e)}")
        files_not_moved += 1

# Show final summary
print("\nOperation summary:")
print(f"Files successfully moved: {files_moved}")
print(f"Files not moved: {files_not_moved}")


