import git
import os
print (f'primera opción: {os.path.dirname(os.path.abspath(__file__))}')
print(f'segunda opción: {os.path.dirname(os.path.abspath(__file__))}/update')

repo = git.Repo(os.getcwd())
print (f'resultado del update: {repo.remotes.origin.pull("")}')