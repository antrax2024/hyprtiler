#!/usr/bin/env bash

rm -rfv dist/

uv build
uv publish
