# git

## 0. Common commands

git status : check if current is clean

git reset --hard : if changes not committed, undo all changes (including deleted) 
git clean : if not committed, remove untracked files 
  options: -n,  -i,  -f

git stash : Stash the changes in a dirty working directory away
git stash list / show / drop / pop / clear

git commit: create a new node point HEAD to it 

git merge <branch_name> : merge branch_name into HEAD 

git rebase <branch_name> : rebase HEAD to branch0 
git rebase <branch0> <branch1> : rebase branch1 to branch0 
git rebase -i <node_hash> : pop UI to rearrage and pick

git checkout <branch_name> or <node_hash> : point HEAD to a node 
git checkout -b <branch_name> : create and checkout 

git branch : list branches 
git branch -f <branch_name> : force branch_name point to HEAD 
git branch -f <branch_name> <node_hash> : force branch_name point to a node

git cherry_pick <node_hash1> <node_hash2> <node_hash3>  : pick any nodes (changes) from other branch and merge to HEAD

git tag versionX : add a tag to HEAD 
git tag versionX <node_hash> : add a tag to a node 
git describe <node_hash> : show how far from latest tag


Use Cases:

## 1. Clone
- git clone url: clone repo to local

## 2. Temporarily go to a previous commit and then switch back
- git log    to see the history and node hash
- git checkout <node_hash>
- git checkout <node_hash> or <branch_name>

## 3. Reset all uncommit change 
git reset : use locally, move HEAD(cannot be detached) and attached branch pointer to any node
  - git reset --hard HEAD    this will remove all current local uncommit changes
  - git reset --hard HEAD~1    this will reset to HEAD~1
  
## 4. Undo the reset 
  - git reflog              see all the git actions
  - git reset 'HEAD@{1}'     this will undo 'reset HEAD' if it was just ran

## 4. Reset a single file
- git checkout file_name    to reset it to HEAD
- git checkout HEAD file_name    same

## 5. Push out
- git add .
- git commit -am "message"
- git push

## 6. Revert commit and create new one
simply creates a new commit that is the opposite of an existing commit
The --no-commit flag lets git revert all the commits at once- otherwise you'll be prompted for a message for each commit in the range, littering your history with unnecessary new commits
This is a safe and easy way to rollback to a previous state
- git revert HEAD    this will revert what changed in HEAD
- git revert HEAD HEAD~1 HEAD~2     revert multiple recent commits
- git revert <node1> <node2> <node3>    better to use this at work

## 7. Push/Fetech local <-> remote branch
git push origin localbranch:remotebranch    ->  push localbranch to remotebranch 
git push origin :remotebranch    ->  delete remote branch 
git fetch origin remotebranch:localbranch    -> fetch remotebranch to localbranch 
git fetch origin :localbranch    ->  delete local branch 


git commit --amend : slight modification, creates parallel node 


## 3. Pull in
git pull

git fetch : download all new nodes (ALL branches) and update origin/branches pointers 
git fetch origin \<branch_name> : download new nodes from a branch, point local origin/branch

git diff master origin/master : show difference between master and remote master 

git merge : merge the fetch
