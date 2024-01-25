import jwt

def decode_jwt(token,secret):
    algos=['HS256', 'HS384', 'HS512', 'RS256', 'RS384', 'RS512', 'ES256', 'ES384', 'ES512', 'PS256', 'PS384', 'PS512']
    for algo in algos:
        try:
            print(f"Now Trying {algo}...")
            decoded_data = jwt.decode(token, secret, algorithms=[algo])
            return decoded_data
        except jwt.ExpiredSignatureError:
            print("Token has expired.")
        except jwt.InvalidTokenError:
            print("Invalid token.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage:
token_to_decode = input("Enter token to decode: ")
secret = input("Enter secret:( If you don't know the secret, just press enter)")
if secret == "":
    secret = 'secret'
decoded_data = decode_jwt(token_to_decode,secret)
if decoded_data:
    print("Decoded data:", decoded_data)