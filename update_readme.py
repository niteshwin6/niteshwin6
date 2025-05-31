import os
from github import Github

# Prefer personal token if available
token = os.getenv("MY_GITHUB_TOKEN") or os.getenv("GITHUB_TOKEN")

if not token:
    raise ValueError("No GitHub token found in environment.")

g = Github(token)

# Safer user context
try:
    user = g.get_user()
    repos = sorted(
        [repo for repo in user.get_repos(visibility='public')],
        key=lambda r: r.pushed_at,
        reverse=True
    )[:9]
except Exception as e:
    raise RuntimeError(f"Failed to retrieve repositories: {e}")

# Format repo info
lines = []
for repo in repos:
    lines.append(
        f"- [{repo.name}]({repo.html_url}) - ⭐ {repo.stargazers_count} | ⬆ Last pushed: {repo.pushed_at.date()} | 🛠️ Simulated Activity: Code Review, Pull Request"
    )

# Inject into README
readme_path = "README.md"
with open(readme_path, "r") as f:
    content = f.read()

start_tag = "<!--START_SECTION:repo_activity-->"
end_tag = "<!--END_SECTION:repo_activity-->"

if start_tag not in content or end_tag not in content:
    raise ValueError("Markers not found in README.md")

start = content.index(start_tag) + len(start_tag)
end = content.index(end_tag)

new_content = content[:start] + "\n" + "\n".join(lines) + "\n" + content[end:]

with open(readme_path, "w") as f:
    f.write(new_content)

print("✅ README.md updated with latest repo activity.")
