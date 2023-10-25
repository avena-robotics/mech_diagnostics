#! /bin/bash
git status
git fetch
git add *.ipynb
git commit -m "aktualizacja kalibracji 23.10.25"
git push -f
