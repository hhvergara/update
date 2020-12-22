import git
import os
import logging

git_path = f'{os.getcwd()}/update'

logging.basicConfig(level=logging.INFO)
repo = git.Repo(git_path)

hcommit = repo.head.commit
print(hcommit.diff())                  # diff tree against index
print(hcommit.diff('HEAD~1'))          # diff tree against previous tree

print(hcommit.diff(None))              # diff tree against working tree

index = repo.index

# diff index against itself yielding empty diff
print(index.diff())

print(index.diff(None))                # diff index against working copy

print(index.diff('HEAD'))              # diff index against current HEAD tree

try:
    repo.remotes.origin.pull("")
except:
    pass
hcommit = repo.head.commit
hcommit.diff(None)              # diff tree against working tree
# Traverse added Diff objects only
for diff_added in hcommit.diff(None):
    print(diff_added)
tags = repo.tags
tag = repo.tags[-1]
print(tag.name)
print(tag.object.message)
print(tag.commit.author.name)
date = tag.commit.committed_datetime
date = f'{date.day}-{date.month}-{date.year}'
print(date)
