import requests
response = requests.get("https://api.github.com/users/athiraRaj2019/repos")
my_projects = response.json()

# print the whole objects list
print(my_projects)
print(type(my_projects))

for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n")