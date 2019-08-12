# CMND SHIFT N to open a new workspace
"""
git help <verb>
git verb --help  both bring up help manuals

git init --> initializes git in terminal system, git then tracks code
rm -rf .git --> deletes current git directory
ls -la --> creates a git directory (ls means "show files" adding
-something adds modifications to the "show files" command)

git status --> shows untracked files in red.
touch .gitignore --> creates a text git ignore file to put files into that are not affected by personal preferences
 -then copy and paste all projects you want in git ignors
 git status again will show what that file has moved to git ignore

git add -A >> adds all untracted files in staging area

gir reset filename >> takes files off the staging area
git reset >> moves all files back to working directory

git status shows all files in green
git commit -m "message"

git status >> will show that the workign directory is clean.
git log >> gives hash number for commit and datetime

TRACKING A REMOTE PROJECT WITH GIT
git clone <url> <where to clone>
git clone <url> <where to clone> . >> dot means clone the whole repository
git remote -v >> lists information to repository
git branch -a >> lists all branches to repository locally and remotely

git diff >> shows changes made to code, removed in red, added in green
git add -A >> adds all changes
git commit -m "explanation of changes" >> commiting to staging area
git pull origin master >> pulls changes since last time we pulled
git push origin master >> pushes changes to master branch of mremote repository

CREATING A BRANCH TO WORK OFF OF
git branch <branchname> >> creates branch to work on, this one is named "calc-divide"
git branch >> lists branches, the working branch is in green
git checkout <branchname>
git branch >> will show you are working on checkout branch
make changes
git status >> shows uncommited files
git commit -m "message" 

git push -u origin <created branch name>
git branch -a >> shows all branches
 'changes will be verified by others working on the project'

git pull origin master >> checkout if there are updates on master branch

MERGE A BRANCH
git checkout master >> look at changes
git pull origin master >> pull changes
git branch --merged >> shows what has been merged so for
git merge <branch name> >> if not merged already, this merges the branch
git push origin master >>  pushes changes to master

DELETING A BRANCH
git branch --merged >> double check what branches have been merged
git branch -d <branch name> >> deletes branch locally
git branch -a >> lists all branches
git push origin --delete <branch name> >> pushes changes to remote repository

#2 FIXING COMMON MISTAKES-if before pushing changes
ls -la
git status >> notifies of changes
git diff >> can see changes if these changes are not what you want:
git checkout <filename>
git status >> Working directory will be clean
git diff >> no changes will be listed

# changing commit message:
git commit --amend -m "changed message"
git log >> will return changed message

# Accidentilly leaving out a file that was meant to be committed
tough.gitignore >> creating a gitignore
git status
git add <gitignore or filename>
git commit --amend >>> will amend a file now, brings up interactive editor
git log --stat >>> will show that new file has been added to commit

# Changing which branch our changes are committed to and restoring master (
    original branch to previous state
)
git log >> (to get/copy original commit id/hash)
git checkout <intended branch>
git log >> see what has been committed to branch
git cherry_pick <paste hash> >> cherry-pick only copies does not cut
git log >> will see intended commit in log

git checkout <unintended branch> >> change to unintended branch
notes: git reset --soft, git reset --mixed, git reset --hard >>differences
git rest --soft <paste hash of initial commit> >> 
git log >> initial commit will be removed from unintended branch
git status >> will show that changes are still in staging directory (green)

git reset (--mixed is default no need to type)
git log >> only one commit
git status >> changes in working directory, not staging directory (red)

git reset --hard <paste in hash> >> make all files return to state they were in at the hash we specify
git log >> shows one commit
git status >> pasted hash file will not be in working directory. reset --hard
            will remove tracked files and leave untracked files alone

git clean -df >> gets rid of untracked d~directories f~files
git status >> working directory will be clean

# Undoing git reset --hard
gir reflog >> shows previous activity
copy hash of step before reset --hard
git checkout <paste hash>
git log >> changes are returned, but they are not on branches, you have to make a new branch
git branch <name of new branch>
git branch >> checkout if branch is created, note that hash of file says "HEAD detached at <hash>"
# I guess changes are saved to new branch between these two steps even though we did
    not actively put changes in new branch
git checkout <master>
git checkout <new branch> >> will show new commit hashes

git reflog >> is important!!!!


# UNdoing changes when others have already pulled them
git revert >> creates new commits that reverse changes

git log >> see commits
copy hash
git revert <paste hash>
save and exit out of vim page
git log >> can see previous commits in addition to commit that reverts them
git diff <paste hashes> >> shows changes

# USING THE STASH COMMAND
-changes not ready to commit but need to switch branches or revert to a 
  previous state but you don't know where to put current changes

git branch <branche name>
git checkout <branch name>
work on branch
git diff >> shows changes
git stash save "type message of what changes were made"
git diff >> no changed showed
git states >> workign directory clean
git stash list >> stash message returned beginning stash{stashIndex}
git stash apply <stashIndex> >> changes moved back to working directory
git stash list >> will show that stash is still there
git checkout --. >> goes back
git stash list >> shows stashes
git stash pop >> will grab first in list of stashes, apply changes
                to working directory, and remove stash from stash list
git diff >> will show changes
make more changes
git diff >> will show changes
git stash save "another stash message"
git stash list >> shows stash list
make more changes
git diff >> shows changes
git stash save "new message"
git stash list>> old stash moved index to 1 not 0
git stash pop >> pops most recent change
git stash drop <paste stash{stashIndex} >> drops stashed changes according to index
git stash list >> shows changes without dropped stash 
git stash clear >> deletes all stashed chages
git stash list >> shows that there are no stashed changes

-if you realize you are working on the wrong branch:
git stash save "message:
git checkout <branch you want to work on>
git stash pop >> moves most recent stash onto current branch
git diff >> shows changes
git add . >> adds all changes
git commit -m "commit message"  

# GIT DIFF AND MERGE TOOLS
-make changes in file
git diff > shows changes in green
-download diffmerge
ls usr/bin >> shows ... programs? includind installation of diffmerge
git config <stuff> >> gets diffmerge working
git difftool >> opens up window showing split screen of file you changes
                this is for when there are many changes to files and 
                git diff is too hard to look at

 # DIFFERENCES BETWEEN git add -A, git add -u, and git add *

 git add -A >> add all untracked files in working directory to stage 
 git reset >> goes back to before add
 git add -A <specific directory name> >> only adds files in specified directory
 git add  <specific directory name> >> same as above
 git add --no-all >> wont stage deleted files

 git add -u >> adds all modified and deleted files but not untracked files
 git reset
 git add -u <directory name>

 git add . >> only adds files in local directory, not all in working directory

 git add * >> unpredictable as to what gets added










  
























"""


 