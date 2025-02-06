import base64

def convert_to_base64(input1, input2):
    # Combine the inputs in the format "input1:input2"
    combined_input = f"{input1}:{input2}"
    
    # Encode the combined string to base64
    encoded_result = base64.b64encode(combined_input.encode()).decode()
    
    return encoded_result

# Example usage
input1 = "48c6a972-6cb0-44b4-92f7-6ede901f5dba"
input2 = "sl2ZPNZNliNS6lfbB-DV3A"
result = convert_to_base64(input1, input2)
print("Base64 encoded result:", result)