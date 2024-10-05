from .inference import infer_openvino

def ask_algo_whiz(user_input):
    """
    Gets a response from the inference model using OpenVINO.
    """
    response = infer_openvino(user_input)
    return response

# Predefined DSA solutions
def bubble_sort_code():
    return """
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    """

def selection_sort_code():
    return """
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
    """

def insertion_sort_code():
    return """
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    """

def merge_sort_code():
    return """
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr
    """

def binary_search_code():
    return """
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return -1  # Target not found
    """

def linear_search_code():
    return """
def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1  # Target not found
    """

# Predefined DSA solutions mapping
dsa_solutions = {
    "bubble sort": bubble_sort_code,
    "selection sort": selection_sort_code,
    "insertion sort": insertion_sort_code,
    "merge sort": merge_sort_code,
    "binary search": binary_search_code,
    "linear search": linear_search_code,
}

def dsa_help(question):
    """
    Responds to specific DSA queries or delegates to the inference function for general questions.
    """
    question_lower = question.lower()  # Normalize the question to lower case
    
    # Check if the question is in the predefined DSA solutions
    for key, func in dsa_solutions.items():
        if key in question_lower:
            return func()  # Call the function associated with the found key
    
    # For general queries, invoke the OpenVINO inference function
    return ask_algo_whiz(question)
