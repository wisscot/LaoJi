# git

## Common commands

  ```git status```  check if current is clean
  
  ```git reset --hard``` if changes not committed, undo all changes (including deleted) \
  git clean : if not committed, remove untracked files 
    options: -n,  -i,  -f
  
  git stash : Stash the changes in a dirty working directory away \
  git stash list / show / drop / pop / clear
  
  git commit: create a new node point HEAD to it 
  
  git rebase <branch_name> : rebase current to another branch \
  git rebase <branch0> <branch1> : rebase branch1 to branch0 \
  git rebase -i <node_hash> : pop UI to rearrage and pick
  
  git merge <branch_name> : merge branch_name into HEAD 
  
  ```git switch <branch name>``` : point HEAD to a node \
  ```git switch -c <branch name>``` : create and checkout 
  
  
  git branch : list branches \
  git branch -f <branch_name> : force branch_name point to HEAD \
  git branch -f <branch_name> <node_hash> : force branch_name point to a node
  
  ```git cherry_pick <node_hash1> <node_hash2> <node_hash3>```  : pick any nodes (changes) from other branch and merge to HEAD \
  ```git cherry_pick <hash1>..<hash2>```  : pick a range of nodes, first node not included
  
  git tag versionX : add a tag to HEAD \
  git tag versionX <node_hash> : add a tag to a node \
  git describe <node_hash> : show how far from latest tag


## Use Cases

1. Clone
- ```git clone url```: clone repo to local

 2. Temporarily go to a previous commit and then switch back
- ```git log```    to see the history and node hash
- ```git switch <node_hash> or <branch_name>```

 3. Reset all uncommit change 
  - ```git reset``` : use locally, move HEAD(cannot be detached) and attached branch pointer to any node
  - ```git reset --hard HEAD```    this will remove all current local uncommit changes
  - ```git reset --hard HEAD~1```    this will reset to HEAD~1
  
 4. Undo the reset 
  - git reflog              see all the git actions
  - git reset 'HEAD@{1}'     this will undo 'reset HEAD' if it was just ran

 4. Reset a single file to a version
- ```git checkout file_name```    to reset it to HEAD (disgard changes)
- ```git checkout <node> file_name```    reset file to a version

 4. Develop locally on a different branch
 - git checkout -b <local>      to create a new branch
 - git commit      add commit to local branch
 - git pull --rebase     do this on mainline
 - git rebase <mainline>  do this on localbranch, all commit in local branch will be rebased after mainline
 - git rebase <local>     do this on mainline to fast-forward

 5. Pull the latest changes from code base (origin/mainline)
 Assume we are at local mainline
 - git commit/stash       commit or stash all changes first to make it clean
 - git pull --rebase        pull the changes and rebase local changes to go after origin/mainline
   its possible that the pull has a conflict.  If that happens, use IntelliJ's VCS - continue rebase to merge the conflict interactively. 

 5. Push out
- git add .    or    git clean
- git commit -am "message"
- git push

 6. Revert commit and create new one
simply creates a new commit that is the opposite of an existing commit
The --no-commit flag lets git revert all the commits at once- otherwise you'll be prompted for a message for each commit in the range, littering your history with unnecessary new commits
This is a safe and easy way to rollback to a previous state
- ```git revert HEAD```    this will revert what changed in HEAD
- ```git revert HEAD HEAD~1 HEAD~2```     revert multiple recent commits
- ```git revert <node1> <node2> <node3>```    better to use this at work

 7. Push/Fetech local <-> remote branch
- git push origin localbranch:remotebranch    ->  push localbranch to remotebranch 
- git push origin :remotebranch    ->  delete remote branch 
- git fetch origin remotebranch:localbranch    -> fetch remotebranch to localbranch 
- git fetch origin :localbranch    ->  delete local branch 

 - git pull origin remotebranch

 - git commit --amend : slight modification, creates parallel node 


 8. Pull in
 - git pull --rebase        run at mainline
 or
 - git fetch : download all new nodes (ALL branches) and update origin/branches pointers 
 - git fetch origin <branch_name> : download new nodes from a branch, point local origin/branch
 - git diff <master> <origin/master> : show difference between master and remote master 
 - git merge : merge the fetch
  
  
## Alias
- g=git
- ga='git add'
- gaa='git add --all'
- gam='git am'
- gama='git am --abort'
- gamc='git am --continue'
- gams='git am --skip'
- gamscp='git am --show-current-patch'
- gap='git apply'
- gapa='git add --patch'
- gapt='git apply --3way'
- gau='git add --update'
- gav='git add --verbose'
- gb='git branch'
- gbD='git branch -D'
- gba='git branch -a'
- gbd='git branch -d'
- gbda='git branch --no-color --merged | command grep -vE "^(\+|\*|\s*($(git_main_branch)|development|develop|devel|dev)\s*$)" | command xargs -n 1 git branch -d'
- gbl='git blame -b -w'
- gbnm='git branch --no-merged'
- gbr='git branch --remote'
- gbs='git bisect'
- gbsb='git bisect bad'
- gbsg='git bisect good'
- gbsr='git bisect reset'
- gbss='git bisect start'
- gc='git commit -v'
- 'gc!'='git commit -v --amend'
- gca='git commit -v -a'
- 'gca!'='git commit -v -a --amend'
- gcam='git commit -a -m'
- 'gcan!'='git commit -v -a --no-edit --amend'
- 'gcans!'='git commit -v -a -s --no-edit --amend'
- gcas='git commit -a -s'
- gcasm='git commit -a -s -m'
- gcb='git checkout -b'
- gcd='git checkout develop'
- gcf='git config --list'
- gcl='git clone --recurse-submodules'
- gclean='git clean -id'
- gcm='git checkout $(git_main_branch)'
- gcmsg='git commit -m'
- 'gcn!'='git commit -v --no-edit --amend'
- gco='git checkout'
- gcor='git checkout --recurse-submodules'
- gcount='git shortlog -sn'
- gcp='git cherry-pick'
- gcpa='git cherry-pick --abort'
- gcpc='git cherry-pick --continue'
- gcs='git commit -S'
- gcsm='git commit -s -m'
- gcss='git commit -S -s'
- gcssm='git commit -S -s -m'
- gd='git diff'
- gdca='git diff --cached'
- gdct='git describe --tags $(git rev-list --tags --max-count=1)'
- gdcw='git diff --cached --word-diff'
- gds='git diff --staged'
- gdt='git diff-tree --no-commit-id --name-only -r'
- gdw='git diff --word-diff'
- gf='git fetch'
- gfa='git fetch --all --prune --jobs=10'
- gfg='git ls-files | grep'
- gfo='git fetch origin'
- gg='git gui citool'
- gga='git gui citool --amend'
- ggpull='git pull origin "$(git_current_branch)"'
- ggpur=ggu
- ggpush='git push origin "$(git_current_branch)"'
- ggsup='git branch --set-upstream-to=origin/$(git_current_branch)'
- ghh='git help'
- gignore='git update-index --assume-unchanged'
- gignored='git ls-files -v | grep "^[[:lower:]]"'
- git-svn-dcommit-push='git svn dcommit && git push github $(git_main_branch):svntrunk'
- gk='\gitk --all --branches'
- gke='\gitk --all $(git log -g --pretty=%h)'
- gl='git pull'
- glg='git log --stat'
- glgg='git log --graph'
- glgga='git log --graph --decorate --all'
- glgm='git log --graph --max-count=10'
- glgp='git log --stat -p'
- glo='git log --oneline --decorate'
- globurl='noglob urlglobber '
- glod='git log --graph --pretty='\''%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ad) %C(bold blue)<%an>%Creset'\'
- glods='git log --graph --pretty='\''%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%ad) %C(bold blue)<%an>%Creset'\'' --date=short'
- glog='git log --oneline --decorate --graph'
- gloga='git log --oneline --decorate --graph --all'
- glol='git log --graph --pretty='\''%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'
- glola='git log --graph --pretty='\''%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'' --all'
- glols='git log --graph --pretty='\''%Cred%h%Creset -%C(auto)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'\'' --stat'
- glp=_git_log_prettily
- glum='git pull upstream $(git_main_branch)'
- gm='git merge'
- gma='git merge --abort'
- gmom='git merge origin/$(git_main_branch)'
- gmt='git mergetool --no-prompt'
- gmtvim='git mergetool --no-prompt --tool=vimdiff'
- gmum='git merge upstream/$(git_main_branch)'
- gp='git push'
- gpd='git push --dry-run'
- gpf='git push --force-with-lease'
- 'gpf!'='git push --force'
- gpoat='git push origin --all && git push origin --tags'
- gpr='git pull --rebase'
- gpristine='git reset --hard && git clean -dffx'
- gpsup='git push --set-upstream origin $(git_current_branch)'
- gpu='git push upstream'
- gpv='git push -v'
- gr='git remote'
- gra='git remote add'
- grb='git rebase'
- grba='git rebase --abort'
- grbc='git rebase --continue'
- grbd='git rebase develop'
- grbi='git rebase -i'
- grbm='git rebase $(git_main_branch)'
- grbo='git rebase --onto'
- grbs='git rebase --skip'
- grep='grep --color=auto --exclude-dir={.bzr,CVS,.git,.hg,.svn,.idea,.tox}'
- grev='git revert'
- grh='git reset'
- grhh='git reset --hard'
- grm='git rm'
- grmc='git rm --cached'
- grmv='git remote rename'
- groh='git reset origin/$(git_current_branch) --hard'
- grrm='git remote remove'
- grs='git restore'
- grset='git remote set-url'
- grss='git restore --source'
- grst='git restore --staged'
- grt='cd "$(git rev-parse --show-toplevel || echo .)"'
- gru='git reset --'
- grup='git remote update'
- grv='git remote -v'
- gsb='git status -sb'
- gsd='git svn dcommit'
- gsh='git show'
- gsi='git submodule init'
- gsps='git show --pretty=short --show-signature'
- gsr='git svn rebase'
- gss='git status -s'
- gst='git status'
- gsta='git stash push'
- gstaa='git stash apply'
- gstall='git stash --all'
- gstc='git stash clear'
- gstd='git stash drop'
- gstl='git stash list'
- gstp='git stash pop'
- gsts='git stash show --text'
- gstu='gsta --include-untracked'
- gsu='git submodule update'
- gsw='git switch'
- gswc='git switch -c'
- gtl='gtl(){ git tag --sort=-v:refname -n -l "${1}*" }; noglob gtl'
- gts='git tag -s'
- gtv='git tag | sort -V'
- gunignore='git update-index --no-assume-unchanged'
- gunwip='git log -n 1 | grep -q -c "\-\-wip\-\-" && git reset HEAD~1'
- gup='git pull --rebase'
- gupa='git pull --rebase --autostash'
- gupav='git pull --rebase --autostash -v'
- gupv='git pull --rebase -v'
- gwch='git whatchanged -p --abbrev-commit --pretty=medium'
- gwip='git add -A; git rm $(git ls-files --deleted) 2> /dev/null; git commit --no-verify --no-gpg-sign -m "--wip-- [skip ci]"'
  
