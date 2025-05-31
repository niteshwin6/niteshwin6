import os
from github import Github

# Authenticate using GitHub token
g = Github(os.environ["GITHUB_TOKEN"])

username = "niteshwin6"
user = g.get_user()

# Get your 9 most recently pushed public repos
repos = sorted(
    [repo for repo in user.get_repos() if not repo.private],
    key=lambda r: r.pushed_at,
    reverse=True
)[:9]

# Format content for README
lines = []
for repo in repos:
    lines.append(
        f"- [{repo.name}]({repo.html_url}) - ⭐ {repo.stargazers_count} | ⬆ Last pushed: {repo.pushed_at.date()} | 🛠️ Simulated Activity: Code Review, Pull Request"
    )

# Inject the content into README.md
readme_path = "README.md"
with open(readme_path, "r") as f:
    content = f.read()

start = content.index("<!--START_SECTION:repo_activity-->") + len("<!--START_SECTION:repo_activity-->")
end = content.index("<!--END_SECTION:repo_activity-->")

new_content = content[:start] + "\n" + "\n".join(lines) + "\n" + content[end:]

with open(readme_path, "w") as f:
    f.write(new_content)
