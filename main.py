from github import Github
import datetime
from datetime import timedelta

user_name = "leapcode"
repo_name = "bitmask_android"

now = datetime.datetime.now()
#late = now - timedelta(days=3)
late = now - timedelta(minutes=3)

g = Github("user_name", "password")

OpenIssues = g.get_repo(full_name_or_id="user_name"/"repo_name")

for i in OpenIssues.get_issues():
    if i.updated_at =< late
    print i.title+" is late for an important date "+i.html_url



