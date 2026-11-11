
import os
from pathlib import Path

# Define file categories and their extensions
subcategory = {
    "DOCUMENTS": [
        ".pdf", ".txt", ".doc", ".docx",
        ".rtf", ".pptx", ".odt", ".xlsx"
    ],

    "AUDIO": [
        ".mp3", ".m4b", ".m4a", ".wav",
        ".ogg", ".oga", ".srt"
    ],

    "VIDEOS": [
        ".mov", ".avi", ".mp4", ".3gp",
        ".ogv", ".wmv", ".webm", ".flv",
        ".mkv", ".vob"
    ],

    "IMAGES": [
        ".jpg", ".jpeg", ".raw", ".png",
        ".tiff", ".gif", ".bmp", ".svg"
    ],

    "PROGRAMMING FILES": [
        ".htm", ".html", ".cpp", ".c",
        ".py", ".css", ".java", ".js",
        ".json"
    ]
}


# Identify the category based on file extension
def findTheCategory(value):
    for category, extensions in subcategory.items():
        if value in extensions:
            return category

    return "MISC"


# Organize files in the current directory
def organizeDir():

    current_dir = Path.cwd()

    for item in os.scandir(current_dir):

        if item.is_dir():
            continue

        filePath = Path(item.path)
        fileType = filePath.suffix.lower()

        directory = findTheCategory(fileType)

        directoryPath = current_dir / directory

        # Create category folder if it does not exist
        directoryPath.mkdir(exist_ok=True)

        destination = directoryPath / filePath.name

        # Avoid overwriting existing files
        if destination.exists():
            print(f"Skipped: {filePath.name}")
            continue

        # Move file into the category folder
        filePath.rename(destination)

        print(f"Moved: {filePath.name} -> {directory}")


if __name__ == "__main__":
    organizeDir()
