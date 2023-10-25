#! /bin/bash
git status
git fetch
git add *.ipynb
git commit -m "aktualizacja kalibracji"
git push -f
