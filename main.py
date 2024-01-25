import jwt

def decode_jwt(token, secret='secret', algorithm='HS256'):
    try:
        decoded_data = jwt.decode(token, secret, algorithms=[algorithm])
        return decoded_data
    except jwt.ExpiredSignatureError:
        print("Token has expired.")
    except jwt.InvalidTokenError:
        print("Invalid token.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
token_to_decode = input("Enter token to decode: ")
decoded_data = decode_jwt(token_to_decode)

if decoded_data:
    print("Decoded data:", decoded_data)