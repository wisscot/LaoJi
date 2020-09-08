# git

## 0. Local Ops
git reset --hard : if changes not committed, undo all changes (including deleted) \
git clean : if not committed, remove untracked files \
  options: -n,  -i,  -f

git stash : Stash the changes in a dirty working directory away
git stash list / show / drop / pop / clear

git commit: create a new node point HEAD to it 

git merge \<branch_name> : merge branch_name into HEAD \
git rebase \<branch0> \<branch1> : rebase HEAD/branch1 to branch0 \
git rebase -i \<node_hash> : pop UI to rearrage and pick

git checkout \<branch_name> : checkout \
git checkout -b \<branch_name> : create and checkout \
git checkout \<node_hash> / \<branch_name>\~2 / HEAD\~2 : checkout a specific node

git branch : list branches \
git branch -f \<branch_name> : force branch_name point to HEAD \
git branch -f \<branch_name> \<node_hash> : force branch_name point to a node

git cherry_pick \<node_hash1> \<node_hash2> \<node_hash3>  : pick any nodes and merge to HEAD

git tag versionX : add a tag to HEAD \
git tag versionX \<node_hash> : add a tag to a node \
git describe \<node_hash> : show how far from latest tag


## 1. Clone
- git clone url: clone repo to local

## 2. Push out
- git add -> git commit -> git push
- git commit -a -> git push

git commit --amend : slight modification, creates parallel node \
git reset : use locally, go back to last node \
git revert : use for remote, create a new node

git push origin localbranch : remotebranch    : push localbranch to remotebranch \
git push origin : remotebranch    : delete remote branch \
git fetch origin remotebranch : localbranch    : fetch remotebranch to localbranch \
git fetch origin : localbranch    : delete local branch 


## 3. Pull in
git pull

git fetch : download all new nodes (ALL branches) and update origin/branches pointers \
git fetch origin \<branch_name> : download new nodes from a branch, point local origin/branch

git diff master origin/master : show difference between master and remote master 

git merge : merge the fetch
