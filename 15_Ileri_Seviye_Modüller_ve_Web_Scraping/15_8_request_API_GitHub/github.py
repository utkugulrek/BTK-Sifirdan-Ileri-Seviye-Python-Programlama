from unittest import case

import requests


class GitHub:
    def __init__(self):
        self.BASE_URL = "https://api.github.com"
        self.TOKEN = (
            "YOUR_GITHUB_PERSONAL_ACCESS_TOKEN"  # Replace with your actual token
        )
        self.HEADERS = {"Authorization": f"token {self.TOKEN}"}

    def getUser(self, username):
        response = requests.get(f"{self.BASE_URL}/users/{username}")
        return response.json()

    def get_repositories(self, username):
        response = requests.get(f"{self.BASE_URL}/users/{username}/repos")
        return response.json()

    def create_repository(self, repo_name):
        payload = {
            "name": repo_name,
            "description": "This is your first repository",
            "homepage": "https://github.com",
            "private": True,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True,
        }
        response = requests.post(
            f"{self.BASE_URL}/user/repos", headers=self.HEADERS, json=payload
        )
        return response.json()


github = GitHub()

while True:
    choice = input(
        "1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\nEnter your choice:"
    )
    print("*" * 50)
    match choice:
        case "1":
            username = input("Enter the username:")
            result = github.getUser(username)
            print(
                f"Name: {result.get('name')} Public Repos: {result.get('public_repos')} Followers: {result.get('followers')}"
            )
        case "2":
            username = input("Enter the username:")
            result = github.get_repositories(username)
            for repo in result:
                print(
                    f"Repository Name: {repo.get('name')} URL: {repo.get('html_url')}"
                )
        case "3":
            name = input("repository name: ")
            result = github.create_repository(name)
            print(result)
        case "4":
            print("Exiting...")
            break
        case _:
            print("Invalid choice. Please try again.")
            print("*" * 50)
