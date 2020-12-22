import git
import os
import logging

git_path = f'{os.getcwd()}/update'

logging.basicConfig(level=logging.INFO)
GIT_PYTHON_TRACE = 'full'

repo = git.Repo(git_path)
repo.remotes.origin.pull("")

hcommit = repo.head.commit
hcommit.diff(None)              # diff tree against working tree
# Traverse added Diff objects only
for diff_added in hcommit.diff(None):
    print(diff_added)

print(repo.tags)

# status = repo.remotes.origin.status("")
# print(status)