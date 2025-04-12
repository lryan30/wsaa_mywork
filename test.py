from github import Github
import config2 as cfg  # Assuming your API key is stored here

# API key for authentication
apiKey = cfg.githubkey
g = Github(apiKey)

# Connect to the repository
repo = g.get_repo("lryan30/wsaa_mywork")
file_path = "assignment4.txt"

# Get the file content from the repository (base64 encoded)
file_content = repo.get_contents(file_path)

# Decode the content (base64 -> string)
decoded_content = file_content.content.decode('utf-8')

# Replace "Andrew" with "Louise"
updated_content = decoded_content.replace("Andrew", "Louise")

# Commit the changes and push to the repository
commit_message = "Updated test.txt with edited name"

# Update the file on GitHub using PyGithub
updated_file = repo.update_file(file_path, commit_message, updated_content)


if updated_file:  
    print("File updated successfully.")
else:
    print("Failed to update file.")
