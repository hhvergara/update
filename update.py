import git
import os
import logging
import subprocess

git_path = f'{os.getcwd()}/update'


def bash_command(cmd='', path='.'):
    pipe = subprocess.Popen(cmd, shell=True, cwd=path,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, error) = pipe.communicate()
    pipe.wait()
    return {'out': out.decode("utf-8"), 'error': error.decode("utf-8")}


def update_system():
    update_available_msg = 'On branch main\nYour branch is behind \'origin/main\' by'
    up_to_date = 'On branch main\nYour branch is up to date'
    error_msg = 'Error: update could not be performed, please try again later'

    try:
        bash_command('git fetch', git_path)
        process = bash_command('git status', git_path)
        if process.get('error') != '':
            return process
        elif process.get('out').find(update_available_msg) != -1:
            process = bash_command('git pull', git_path)
            process = bash_command('git status', git_path)
            if process.get('out').find(up_to_date) != -1:
                tag = bash_command('git tag', git_path)
                if tag.get('error') !='':
                     p_tag = tag.get('out')   
                #bash_command('nohup  bash -c "sleep 10; shutdown -r -t now"', git_path)
                return {'out': f'The system has been updated to {p_tag}, restarting ...', 'error': ''}
            else:
                return {'out': '', 'error': error_msg}
        elif process.get('out').find(up_to_date) != -1:
            return {'out': 'System is up to date', 'error': ''}
        else:
            return process
    except Exception as e:
        return {'out': '', 'error': f'{error_msg} Traceback:\n {e}'}

print(update_system())


logging.basicConfig(level=logging.INFO)
repo = git.Repo(git_path)
status = repo.is_dirty()
repo_update = repo.remotes.origin.update()
print(repo_update.fetch)
fetch_info = git.remote.FetchInfo
print(fetch_info.note)
status = repo.is_dirty()

cmd = 'git status '
pipe = subprocess.Popen(cmd, shell=True, cwd=git_path,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
(out, error) = pipe.communicate()
pipe.wait()
print(out)


repo_fetch = repo.remotes.origin.fetch(verbose=True)
print(repo_fetch)
print(repo_fetch[0].ref.log)
status = repo.is_dirty()

repo_remote = git.remote.Remote(repo, name='origin')
repo_remote.fetch(verbose=True)
list_repo = repo_remote.list_items(repo)
[print(x) for x in list_repo]
status = repo.is_dirty()

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

# diff index against current HEAD tree
diff_i_head = index.diff('HEAD')

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
status = repo.is_dirty()
print(date)
repo__remote = git.remote.RemoteProgress()
print(repo__remote)
