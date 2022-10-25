#! /bin/bash
git status
git fetch
git add *.ipynb
git commit -m "update"
git push -f
