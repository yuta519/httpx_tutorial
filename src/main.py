import httpx


response = httpx.get('https://www.example.org/')

# Print httpx class
print(response)
print(type(response))

# Print status code
print(response.status_code)

# Print response text
print(response.text)
