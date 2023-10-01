def remove_vowels_from_end(s):
    vowels = "aeiouAEIOU"
    result = ""

    for char in s[::-1]:
        if char not in vowels:
            result = char + result
        elif result == "":
            continue
        else:
            break

    return result

# Example usage:
input_string = "openAI"
result = remove_vowels_from_end(input_string)
print(result)  # Output: "I"
