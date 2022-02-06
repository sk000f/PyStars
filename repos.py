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

items = response['items']
repo_names, stars = [], []
for item in items:
    repo_names.append(item['name'])
    stars.append(item['stargazers_count'])

data = [{
  'type': 'bar',
  'x': repo_names,
  'y': stars
}]

graph_layout = {
  'title': 'Popular Python Projects',
  'xaxis': {'title': 'Repo'},
  'yaxis': {'title': 'Stars'}
}

fig = {'data': data, 'layout': graph_layout}
offline.plot(fig, filename='repos.html')