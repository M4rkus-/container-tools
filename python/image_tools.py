import requests

registry_url = "https://registry.example.com"
image_name = "myimage:latest"
username = "myuser"
password = "mypassword"

# construct the url for pulling the image
pull_url = f"{registry_url}/v2/{image_name}/manifests/latest"

# send request to pull the image
r = requests.get(pull_url, auth=(username, password))

# check if the pull is successful
if r.status_code == 200:
    print("Image pulled successfully")
else:
    print("Error pulling image")
