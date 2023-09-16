# import requests
# import getpass

# gitlab_token = "{{cookiecutter.token}}"
# gitlab_url = 'https://gitlab.com'

# project_name = "{{cookiecutter.repo_name}}"
# # project_description = 'My GitLab project'

# headers = {
#     'Private-Token': gitlab_token,
# }

# data = {
#     'name': project_name,
# }

# create_project_url = f'{gitlab_url}/api/v4/projects'
# response = requests.post(create_project_url, headers=headers, data=data)

# if response.status_code == 201:
#     print(f'Project {project_name} created successfully.')
# else:
#     print('Failed to create project. Check your GitLab API token and URL.')
import os
import gitlab

gitlab_url = 'https://gitlab.com/'
gitlab_token = "{{cookiecutter.token}}"

project_name = 'Our Project'
project_description = 'A template for projects.'
project_visibility = 'public' 

gl = gitlab.Gitlab(gitlab_url, private_token=gitlab_token)
project = gl.projects.create({
    'name': project_name,
    'description': project_description,
    'visibility': project_visibility,
})

print(f"Project created: {gitlab_url}{project_name}")

if not os.path.exists('.git'):
    os.system('git init')

if not os.path.isfile('README.md'):
    with open('README.md', 'w') as readme_file:
        readme_file.write('# My Project\n\nThis is a template for project.')

if not os.path.exists('src'):
    os.mkdir('src')

os.system('git add .') 

os.system('git commit -m "Initial commit"')

os.system(f'git remote set-url origin {project.http_url_to_repo}')

os.system('git push -u origin master')