import git
import os
import logging
logging.basicConfig(level=logging.INFO)
GIT_PYTHON_TRACE = 'full'

print (f'primera opción: {os.path.dirname(os.path.abspath(__file__))}')
print(f'segunda opción: {os.getcwd()}')
print (os.path.dirname(__file__))
repo = git.Repo(f'{os.getcwd()}/update')
print (f'resultado del update: {repo.remotes.origin.pull("")}')

# status = repo.remotes.origin.status("")
# print(status)