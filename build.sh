#!/usr/bin/env bash

rm -rfv dist/*
rm -rfv build/*

pyinstaller --onefile --clean --distpath="$HOME/dotfiles/bin" --workpath=build --specpath=build -
