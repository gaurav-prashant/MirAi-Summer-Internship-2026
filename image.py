import requests

user_prompt ="Virat Kholi winning the world cup ,along with the indian team "

url = f"https://image.pollinations.ai/prompt/{user_prompt}"  

print(f"Generating for: {user_prompt}")

response = requests.get(url)

print(response)

if response.status_code == 200:
    with open("output.png", "wb") as file:
        file.write(response.content)
    print("Success")
else:
    print("Error")