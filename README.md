# Python File Organizer

A Python script that automatically organizes files in a directory by sorting them into folders based on their file extensions.

## Description

This script helps you keep your directories clean and organized by automatically sorting files into appropriate folders based on their file types. It creates folders for different categories of files (documents, images, videos, etc.) and moves files into them accordingly.

## Features

- Automatically creates folders based on file types
- Sorts files into appropriate folders based on their extensions
- Handles various file types including:
  - Documents (Word, Excel, PDF, etc.)
  - Images (JPG, PNG, GIF, etc.)
  - Audio files (MP3, WAV, etc.)
  - Video files (MP4, AVI, etc.)
  - Compressed files (ZIP, RAR, etc.)
  - Design files (DWG, EPS, etc.)
  - Development files (Python, Java, etc.)
- Creates an 'others' folder for unrecognized file types
- Provides detailed operation summary
- Handles duplicate files safely

## Requirements

- Python 3.6 or higher
- pathlib module (included in Python standard library)

## Installation

1. Clone this repository or download the script:
```bash
git clone https://github.com/yourusername/file-organizer.git
```

2. Copy the script in the desired folder.

## Usage

1. Basic usage (organizes current directory):
```bash
python sort-files.py
```

2. To create a desktop shortcut for easy access:
```powershell
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$env:USERPROFILE\Desktop\Sort Files.lnk")
$Shortcut.TargetPath = "python"
$Shortcut.Arguments = "sort-files.py"
$Shortcut.Save()
```

## Output Example

```
Created folder: documents
Moved document.pdf to documents
Created folder: images
Moved photo.jpg to images
Warning! file.txt already exists in documents
...
Operation summary:
Files successfully moved: 15
Files not moved: 2
```

## Supported File Types

### Documents
- Microsoft Office files (.doc, .docx, .xls, .xlsx, .ppt, .pptx)
- PDF files (.pdf)
- Text files (.txt)
- OpenDocument formats (.odt, .ods, .odp)

### Images
- Common formats (.jpg, .jpeg, .png, .gif)
- Raw formats (.raw, .cr2, .nef)
- Design formats (.ai, .psd)

### Audio
- Common formats (.mp3, .wav, .wma, .aac)
- Lossless formats (.flac)

### Video
- Common formats (.mp4, .avi, .mkv, .mov)
- Web formats (.webm)

### Development
- Source code files (.py, .java, .cpp, .html, .css, .js)

## Contributing

Feel free to fork this repository and submit pull requests to improve the script. You can also open issues if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
