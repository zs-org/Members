import requests

ORG = "zs-org"
README_PATH = "README.md"

def get_members():
    url = f"https://api.github.com/orgs/{ORG}/members"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_user_details(username):
    url = f"https://api.github.com/users/{username}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    return response.json()

def generate_table(members):
    table = "| Avatar | Name | Bio |\n|--------|------|-----|\n"
    for member in members:
        user = get_user_details(member['login'])
        avatar = f"![]({user['avatar_url']}&s=40)"
        name = f"[{user['login']}]({user['html_url']})"
        bio = user['bio'] if user['bio'] else ""
        table += f"| {avatar} | {name} | {bio} |\n"
    return table

def update_readme(table):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    start = content.find("## 👥 Members")
    end = content.find("---", start)
    before = content[:start]
    after = content[end:]
    new_section = f"## 👥 Members\n\nWelcome to our awesome members! 🚀\n\n{table}"
    new_content = before + new_section + after

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    members = get_members()
    table = generate_table(members)
    update_readme(table)
