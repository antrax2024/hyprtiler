#!/usr/bin/env bash

pyinstaller --onefile \
    --clean \
    --distpath="$HOME/dotfiles/bin" \
    --workpath=build \
    --specpath=build \
    hyprwindow.py

rm -rf build/*
