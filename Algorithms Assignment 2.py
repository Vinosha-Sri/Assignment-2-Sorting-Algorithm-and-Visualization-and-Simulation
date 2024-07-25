# Imports the simpleaudio module to play the sound for each swap: 
import simpleaudio as sa
# Function was created to play the swap sound: 
def play_sound():
    # Load the sound file: 
    wave_object = sa.WaveObject.from_wave_file("beep.wav")
    # Plays the sound from the file: 
    play_object = wave_object.play()
    # Function ends only when the sound ends: 
    play_object.wait_done()
# Function was created for the Merge Sort Algorithm to be executed:
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # In an array, find where the array is in the middle.
        First = arr[:mid] # First half of the array stored in one variable.
        Second = arr[mid:] # Second half of the array stored in one variable.
        merge_sort(First) # Recursively calls merge_sort function for the first half of the array.
        merge_sort(Second) # Recursively call merge_sort function for the second half of the array.
        i = j = k = 0
        # Merge both half of the arrays: 
        while i < len(First) and j < len(Second):
            if First[i] < Second[j]:
                arr[k] = First[i]
                i += 1
            else:
                arr[k] = Second[j]
                j += 1
            play_sound() # After each swap the swap sound will be played. 
            print(arr) # The array is printed after each swap.
            k += 1
        while i < len(First):
            arr[k] = First[i]
            i += 1
            k += 1
            play_sound() # After each insertion the swap sound will be played. 
            print(arr) # The array is printed after each insertion.
        while j < len(Second):
            arr[k] = Second[j]
            j += 1
            k += 1
            play_sound() # After each insertion the swap sound will be played. 
            print(arr) # The array is printed after each insertion.
# Accepts an n array of numbers from the user to use for the Merge Sort Algorithm: 
if __name__ == "__main__":
    # Input taken from the user for an array of numbers: 
    user_input = input("Please enter numbers of your choice and use spaces to separate each of them: ")
    # The input string is changed into to a list of integers: 
    array = list(map(int, user_input.split()))
    # Prints the user input as an array: 
    print("Numbers Entered In Array Format:", array)
    # Performs the Merge Sort Algorithm on the array of numbers: 
    merge_sort(array)
    # Prints the new sorted array: 
    print("Sorted Array:", array)