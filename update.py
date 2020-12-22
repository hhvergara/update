import git
import os
import logging

git_path = f'{os.getcwd()}/update'

logging.basicConfig(level=logging.INFO)
GIT_PYTHON_TRACE = 'full'

repo = git.Repo(git_path)
print (f'resultado del update: {repo.remotes.origin.pull("")}')

# status = repo.remotes.origin.status("")
# print(status)