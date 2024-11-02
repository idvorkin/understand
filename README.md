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

### WOW - Just dump it into Google AI Studio

Then start talkikng to it:

- [All.Md](https://drive.google.com/file/d/1-2EwHZGnEHoe3ybRAMiZCeH_py2VJKOy/view?usp=sharing)

- [Converation](https://aistudio.google.com/app/prompts?state=%7B%22ids%22:%5B%221tViSUJDwE5eAReh_q3ZESnwcFlF5H6d1%22%5D,%22action%22:%22open%22,%22userId%22:%22116207807353387122003%22,%22resourceKeys%22:%7B%7D%7D&usp=sharing)
