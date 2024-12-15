playlist = []

def addSong(title, artist, duration):
    """
    Adds a song to the playlist.
    """
    try:
        if not isinstance(title, str) or not isinstance(artist, str):
            raise TypeError("Title and artist must be strings.")
        if not isinstance(duration, (int, float)):
            raise ValueError("Duration must be a number.")
        
        song = {
            "title": title,
            "artist": artist,
            "duration": duration
        }
        playlist.append(song)
        print(f"Song '{title}' by {artist} added to the playlist.")
    
    except TypeError as e:
        print(f"Error: {e}")
    
    except ValueError as e:
        print(f"Error: {e}")

def viewPlaylist():
    """
    Displays the current playlist.
    """
    try:
        if not playlist:
            raise IndexError("The playlist is empty.")
        
        print("\nCurrent Playlist:")
        for song in playlist:
            print(f"Title: {song['title']}, Artist: {song['artist']}, Duration: {song['duration']} minutes")
    
    except IndexError as e:
        print(f"Error: {e}")

def updateSong(old_title, new_title, new_artist, new_duration):
    """
    Updates an existing song in the playlist.
    """
    try:
        song_found = False
        for song in playlist:
            if song['title'] == old_title:
                song['title'] = new_title
                song['artist'] = new_artist
                song['duration'] = new_duration
                song_found = True
                print(f"Song '{old_title}' updated to '{new_title}'.")
                break
        
        if not song_found:
            raise KeyError(f"Song with title '{old_title}' not found in the playlist.")
        
        # Validate new data types
        if not isinstance(new_title, str) or not isinstance(new_artist, str):
            raise TypeError("Title and artist must be strings.")
        if not isinstance(new_duration, (int, float)):
            raise ValueError("Duration must be a number.")
    
    except KeyError as e:
        print(f"Error: {e}")
    
    except TypeError as e:
        print(f"Error: {e}")
    
    except ValueError as e:
        print(f"Error: {e}")

def deleteSong(title):
    """
    Deletes a song from the playlist.
    """
    try:
        song_found = False
        for song in playlist:
            if song['title'] == title:
                playlist.remove(song)
                song_found = True
                print(f"Song '{title}' has been deleted.")
                break
        
        if not song_found:
            raise KeyError(f"Song with title '{title}' not found in the playlist.")
    
    except KeyError as e:
        print(f"Error: {e}")

def main():
    """
    Main function to interact with the user and manage the playlist.
    """
    while True:
        print("\nMenu:")
        print("1. Add Song")
        print("2. View Playlist")
        print("3. Update Song")
        print("4. Delete Song")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter song title: ")
            artist = input("Enter artist name: ")
            try:
                duration = float(input("Enter song duration (in minutes): "))
            except ValueError:
                print("Error: Duration must be a number.")
                continue
            addSong(title, artist, duration)
        
        elif choice == "2":
            viewPlaylist()
        
        elif choice == "3":
            old_title = input("Enter the title of the song to update: ")
            new_title = input("Enter new song title: ")
            new_artist = input("Enter new artist name: ")
            try:
                new_duration = float(input("Enter new song duration (in minutes): "))
            except ValueError:
                print("Error: Duration must be a number.")
                continue
            updateSong(old_title, new_title, new_artist, new_duration)
        
        elif choice == "4":
            title = input("Enter the title of the song to delete: ")
            deleteSong(title)
        
        elif choice == "5":
            print("Thank you for using the playlist manager!")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
