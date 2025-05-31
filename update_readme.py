import random
from datetime import datetime, timedelta

# Dummy repositories
dummy_repos = [
    {"name": "ai-image-generator", "url": "https://github.com/niteshwin6/ai-image-generator"},
    {"name": "portfolio-website", "url": "https://github.com/niteshwin6/portfolio-website"},
    {"name": "chatbot-engine", "url": "https://github.com/niteshwin6/chatbot-engine"},
    {"name": "dev-tools-cli", "url": "https://github.com/niteshwin6/dev-tools-cli"},
    {"name": "data-visualizer", "url": "https://github.com/niteshwin6/data-visualizer"},
    {"name": "github-insights", "url": "https://github.com/niteshwin6/github-insights"},
    {"name": "game-ai-bot", "url": "https://github.com/niteshwin6/game-ai-bot"},
    {"name": "personal-blog", "url": "https://github.com/niteshwin6/personal-blog"},
    {"name": "task-manager-api", "url": "https://github.com/niteshwin6/task-manager-api"},
]

activities = [
    "Code cleanup, PR merge",
    "Added dark mode support",
    "Refactored backend logic",
    "Improved CI/CD pipeline",
    "Updated documentation",
    "Implemented caching",
    "Response optimization",
    "Database schema changes",
    "Fixed deployment bug",
]

lines = []
for repo in dummy_repos:
    stars = random.randint(50, 150)
    days_ago = random.randint(0, 10)
    pushed_at = (datetime.now() - timedelta(days=days_ago)).strftime("%Y-%m-%d")
    activity = random.choice(activities)
    lines.append(
        f"- [{repo['name']}]({repo['url']}) - ⭐ {stars} | ⬆ Last pushed: {pushed_at} | 🛠️ {activity}"
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

print("✅ README.md updated with recent activity.")
