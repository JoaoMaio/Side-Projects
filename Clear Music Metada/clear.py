import os
from mutagen.mp3 import MP3

def clear_mp3_metadata(file_path):
    """Clear metadata from the specified MP3 file."""
    if not os.path.isfile(file_path):
        print(f"File {file_path} does not exist.")
        return
    
    # Load the MP3 file
    audio = MP3(file_path)

    # Clear all metadata
    audio.delete()
    audio.save()

    print(f"Metadata cleared for {file_path}")

if __name__ == "__main__":    
    for music in os.listdir("music"):
        mp3_file = f"music/{music}"
        clear_mp3_metadata(mp3_file)
