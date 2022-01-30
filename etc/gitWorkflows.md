Git Workflows
-------------

## Initializing a repo

- to initialize repo, simply cd workingdirectory
   + git init                                *initializes repo* 
   + git add \*.py                           *stages .py files*              
   + git add LICENSE                         *adds a license* 
   + git commit -m 'Initial project version' *commits changes*

- add new file git add README.md
- git commit -a -m 'Added Readme'            *commits changes with comment*


## Setting up connection with remote 

`git remote add origin *repo url*`  // sets new remote

`git remote -v`                     // verifies


## Pushing to remote 

typical command to push is 
`git push origin master`

## Branching

HEAD points to an arbitrary branch

to see what branch is currently being worked on take a look at 
`git log --oneline --decorate`

To create a new branch 
`git branch testing`

To workon new branch 
`git checkout testing`

After commiting changesto specific branches, you can view the all with the
command
`git log --oneline --decorate --graph --all`

"A branch is a simple file that contains the 40 character SHA-1 checksum of the
commit it points to."

New branch only costs 41 bytes! 

It's easy to create and switch to a new branch at the same time: 
`git checkout -b <newbranchname>


### Typical Branch workflow 

- make a branch to work on a specific issuue 
`git checkout -b issXY`

```
vim index.html
git commit -a -m 'Create new footer [issue XY]
```

This commit does not have to be deployed immediately in fact - imagine that 
another issue comes in that has to be dealt with urgently. You can merge back
to the master branch and then create a hotfix branch. 

to merge this branch: 
```
git checkout master 
git merge hotfix 
```
The phrase "fast-forward" will appear in that merge 

To clarify, the pointers before the merge: 
 master -> C2
 issXY -> C3 -> C2 
 hotfix -> C4

The pointers after the merge: 
 issXY -> C3 -> C2
 master -> hotfix C4 

After deploying this hotfix, then you can switch back to what was going on
before the interrupt

first, you can delete the hotfix branch, as it is no longer needed

```git branch -d hotfix```

```git checkout issXY```
then commit...

After this commit the pointer structure is the following: 

 master -> C4 -> C2
 issXY -> C5 -> C3 -> C2

The work on hotfix is not now contained in the issXY branch, if it needs to be
pulled in then there are two options: merge the master branch into issXY or
wait to integrate those changes until you decide to pull the issXY branch back
into master later. 

Snapshots to merge into 

master -> C4 -> C2 
issXY -> C5 -> C3 -> C2

Pointer structure after merge: 

master -> C6 { -> C5 -> C3 -> C2
             { -> C4    ->    C2

After this merge you can delete the issXY branch. 


### Basic merge conflicts   

+ if a similar issue was worked on in two different branches and the same code
  region was changed, then git won't be able to merge the branches cleanly. 

## Some smart commands for viewing logs

`git log --oneline --graph`
