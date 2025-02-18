#!/usr/bin/env bash
rm -rf build/*
rm -rf dist/*

git commit -a
git push

EXECUTABLE="hyprwindow"

pyinstaller --onefile \
    --clean \
    --workpath=build \
    --specpath=build \
    $EXECUTABLE.py

cp dist/$EXECUTABLE $HOME/dotfiles/bin/
# Create a new release on GitHub
REPO="antrax2024/$EXECUTABLE"
TAG="v$(python3 -c "import hyprwindow; print(hyprwindow.VERSION)")"
RELEASE_NAME="Release $TAG"
GITHUB_TOKEN=$GITHUB_TOKEN
BINARY="$(pwd)/dist/$EXECUTABLE"

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
    --data-binary "@$BINARY"
