import requests

ORG = "zs-org"
MEMBERS_MD = "members.md"

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

def write_members_md(table):
    content = f"""## 👥 Members

Welcome to our awesome members! 🚀

{table}
"""
    with open(MEMBERS_MD, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    members = get_members()
    table = generate_table(members)
    write_members_md(table)
