#!/bin/bash
TAG="v$(python3 -c "import hyprwindow; print(hyprwindow.VERSION)")"
echo "Tag ===> $TAG"
