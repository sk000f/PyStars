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
stars,labels, links = [], [], []
for item in items:
    # record number of stars
    stars.append(item['stargazers_count'])

    # build label from owner and description
    owner = item['owner']['login']
    description = item['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

    # add clickable link to bar
    name = item['name']
    url = item['html_url']
    link = f"<a href='{url}'>{name}</a>"
    links.append(link)


data = [{
  'type': 'bar',
  'x': links,
  'y': stars,
  'hovertext': labels,
  'marker': {
    'color': 'rgb(60,100,150)',
    'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
  },
  'opacity': 0.6
}]

graph_layout = {
  'title': 'Popular Python Projects',
  'xaxis': {
    'title': 'Repo',
    'titlefont': {'size':24},
    'tickfont': {'size': 14}
  },
  'yaxis': {
    'title': 'Stars',
    'titlefont': {'size':24},
    'tickfont': {'size': 14}
  }
}

fig = {'data': data, 'layout': graph_layout}
offline.plot(fig, filename='repos.html')