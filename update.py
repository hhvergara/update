import git
import os
import logging

git_path = f'{os.getcwd()}/update'

logging.basicConfig(level=logging.INFO)
repo = git.Repo(git_path)
status=repo.is_dirty()
repo_update = repo.remotes.origin.update()
print(repo_update.fetch)
status=repo.is_dirty()

repo_fetch = repo.remotes.origin.fetch(verbose=True)
print(repo_fetch)
print(repo_fetch[0].ref.log)
status=repo.is_dirty()

repo_remote =  git.remote.Remote(repo,name='origin')
repo_remote.fetch(verbose=True)
status=repo.is_dirty()

hcommit = repo.head.commit
diff = hcommit.diff()                  # diff tree against index
diff_head = hcommit.diff('HEAD~1')          # diff tree against previous tree
[print(x)for x in diff_head]
diff_head[0]

diff_none = hcommit.diff(None)              # diff tree against working tree
[print(x)for x in diff_none]
index = repo.index

# diff index against itself yielding empty diff
diff_index = index.diff()

diff_i_none = index.diff(None)                # diff index against working copy

diff_i_head = index.diff('HEAD')              # diff index against current HEAD tree

# Traverse added Diff objects only
for diff_added in hcommit.diff('HEAD~1').iter_change_type('A'):
    print(diff_added)

diff_index_none = repo.index.diff(None)
# print(diff_index_none[0].a_blob)



# try:
#     repo.remotes.origin.pull("")
# except:
#     pass
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
