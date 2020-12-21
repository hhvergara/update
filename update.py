import git
import os
print (f'primera opción: {os.path.dirname(os.path.abspath(__file__))}')
print(f'segunda opción: {os.getcwd()}')

repo = git.Repo('/home/hedade/Documents/SmartDryer/modulos/update_module/update')
print (f'resultado del update: {repo.remotes.origin.pull("")}')