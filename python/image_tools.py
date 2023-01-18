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

#######################################

import requests

artifactory_url = "https://artifactory.example.com"
image_name = "myimage:latest"
repo = "docker-local"
username = "myuser"
password = "mypassword"

# construct the url for pulling the image
pull_url = f"{artifactory_url}/{repo}/{image_name}/latest"

# send request to pull the image
r = requests.get(pull_url, auth=(username, password))

# check if the pull is successful
if r.status_code == 200:
    print("Image pulled successfully")
else:
    print("Error pulling image")

##################################

import boto3

# Create a client object
client = boto3.client('ecr')

# Define the registry, repository and image details
registry_id = 'aws_account_id'
repository_name = 'myimage'
image_tag = 'latest'

# Construct the full image name
image_name = f"{registry_id}.dkr.ecr.us-east-1.amazonaws.com/{repository_name}:{image_tag}"

# Pull the image
response = client.batch_get_image(
    registryId=registry_id,
    repositoryName=repository_name,
    imageIds=[
        {
            'imageTag': image_tag
        },
    ]
)
print(response)


