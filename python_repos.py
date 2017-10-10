import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

#make an API call and store the response
url= 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:" ,r.status_code)

#store api response in a variable
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

#explore information about repositories
repo_dicts = response_dict['items']
print("Repositories return:", len(repo_dicts))

#examine the first repository
repo_dict = repo_dicts[0]

names, stars = [], []
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	stars.append(repo_dict['stargazers_count'])

#make visualization
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')