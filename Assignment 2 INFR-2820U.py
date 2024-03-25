import pygame

# Initialize Pygame mixer
pygame.mixer.init()

# Load the sound
swap_sound = pygame.mixer.Sound('sound.mp3')  

def merge(left, right):
    merged_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1
            swap_sound.play()  # Play sound on merge operation
            pygame.time.wait(int(swap_sound.get_length() * 1000))
    # Append any remaining items from the lists
    merged_array.extend(left[i:])
    merged_array.extend(right[j:])
    return merged_array

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    L = merge_sort(arr[:mid])
    R = merge_sort(arr[mid:])

    merged = merge(L, R)
    print(f"Merge: {L} and {R} to get {merged}")
    return merged

# Testing the merge sort
arr = [11, 1, 30, 2, 51, 6, 29, 7, 67, 15, 118, 4, 89, 23]
print("Product IDs:", arr)
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)









