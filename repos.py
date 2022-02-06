import requests
from plotly.graph_objs import Bar
from plotly import offline

# Call GitHub API to find most popular Python repos
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
response = r.json()

print(f"Status code: {r.status_code}")
print(f"Total repositories: {response['total_count']}")

# loop over all the returned repos
items = response['items']
for item in items:
    print(f"Name: {item['name']}")
    print(f"Owner: {item['owner']['login']}")
    print(f"Stars: {item['stargazers_count']}")
    print(f"Repository: {item['html_url']}")
    print(f"Description: {item['description']}")