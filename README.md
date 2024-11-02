### 1. Download the feed file

```
wget https://interconnected.org/home/all-posts.json
```

### 2. Copy it all down

```bash
# Define base URL

BASE_URL="https://interconnected.org/"

# Extract permalinks from posts.json and download 8 at a time

jq -r '.posts[].permalink' all-posts.json | while read -r permalink; do echo "${BASE_URL}${permalink}"; done | \
    xargs -n 1 -P 32 -I {} sh -c 'http "{}" -o "$(basename {}).html"'
```

### Convert to Markdown

```bash
mkdir -p content && fd -e html . content-html -x sh -c 'python extract-content.py --file "{}" > "content/$(basename "{}" .html).md"'
```
