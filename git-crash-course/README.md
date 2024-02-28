## Branch Dev
Testing ```git branch dev``` and ```git checkout dev```
## Git Hidden Folder
There's a hidden folder called `.git` indicating that the project is a git repo.

If we wanted to create a git repo in a new project, we'd create the folder and then initialize that repo using `git init`

```
cd /workspaces/tmp/aoc2023/new-project
git init
touch README.md
open README.md
# make changes to readme
git commit -a -m "add readmefile"
```
## Cloning
 We can clone three ways:  HTTPS, SSH Github CLI

Since we are using GitHub CodeSpaces, we'll create a temp directory in our workspace
```sh
mkdir /workspace/tmp
cd /workspace/tmp
```

 ### HTTPS
 ```sh
 git clone https://github.com/cocacolaGfussNet/aoc2023.git
 cd aoc2023
 ```

## Commits

## Branches

## Remotes

## Stashing

## Merging

## Add

```
# to stage a single file
git add README.md

# add ALL unstaged files
git add .
```

## Reset

Reset allows you to move staged files back to be unstaged.  This is useful when you want to revert all staged files.

```
git add .
git reset
```

