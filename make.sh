#!/usr/bin/env bash
rm -rf build/*
rm -rf dist/*

# commit and push changes
git commit -a
git push

# Create a new release on GitHub
EXECUTABLE="hyprwindow"
BINARY_PATH="$(pwd)/dist/$EXECUTABLE"
REPO="antrax2024/$EXECUTABLE"
TAG="v$(python3 -c "import hyprwindow; print(hyprwindow.VERSION)")"
RELEASE_NAME="$TAG"

pyinstaller --onefile \
    --clean \
    --workpath=build \
    --specpath=build \
    $EXECUTABLE.py

# copy the executable to the dotfiles bin directory
cp dist/$EXECUTABLE $HOME/dotfiles/bin/

# Create a new release
response=$(
    curl -s -X POST https://api.github.com/repos/$REPO/releases \
        -H "Authorization: token $GITHUB_TOKEN" \
        -d @- <<EOF
{
  "tag_name": "$TAG",
  "target_commitish": "main",
  "name": "$RELEASE_NAME",
  "body": "Automated release from script",
  "draft": false,
  "prerelease": false
}
EOF
)

# Extract the upload URL from the response
upload_url=$(echo $response | jq -r .upload_url | sed -e "s/{?name,label}//")

# Upload the executable to the release
curl -s -X POST "$upload_url?name=$(basename $BINARY)" \
    -H "Authorization: token $GITHUB_TOKEN" \
    -H "Content-Type: application/octet-stream" \
    --data-binary "@$BINARY_PATH"
