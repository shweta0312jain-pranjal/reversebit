def reverse_binary(binary_str):
    reversed_str = ""     

    for ch in binary_str:
        reversed_str = ch + reversed_str   

    return reversed_str

binary = input("Enter a binary number: ")


result = reverse_binary(binary)

print("Reversed binary number is:", result)