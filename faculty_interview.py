import requests

# GITHUB_LIST_REPOS_API =  "https://api.github.com/users/"

def get_top_5(repos: list) -> list:
    pass

def get_top_5_repos(username: str) -> list[str]:
    all_repos = requests.get(url=f"https://api.github.com/users/{username}/repos", params={"per_page": 100}).json()
    list_of_top_5s = []

    list_of_top_5s += get_top_5(all_repos)
    while len(all_repos) == 100:
        all_repos = requests.get(url=f"https://api.github.com/users/{username}/repos", params={"per_page": 100}).json()
        list_of_top_5s += get_top_5(all_repos)
    
    final_top_5(list_of_top_5s)

    all_repos = [{"name": _["name"], "stargazers_count": _["stargazers_count"]} for _ in all_repos]  # list comprehension to keep the info we need
    all_repos.sort(key= lambda x: x["stargazers_count"], reverse=True)  # nlogn
    return all_repos[:5]

    
    # if all_repos.ok:  # if it's 2xx, it's fine
    #     print(all_repos.json())

def optimized_get_top_5_repos(username: str) -> list[str]:
    all_repos = requests.get(url=f"https://api.github.com/users/{username}/repos").json()
    all_repos = [{"name": _["name"], "stargazers_count": _["stargazers_count"]} for _ in all_repos]
    
    top_5_repos = all_repos[:5]
    top_5_repos.sort(key=lambda x: x["stargazers_count"], reverse=True)

    for repo in all_repos[5:]:
        if repo["stargazers_count"] <= top_5_repos[4]["stargazers_count"]:  # if it is less than the least continue
            continue
        for index, _ in enumerate(top_5_repos[::-1]):  
            if repo["stargazers_count"] > _["stargazers_count"]:
                top_5_repos.insert(index, repo)
                top_5_repos.pop()
                break

    return top_5_repos



if __name__ == "__main__":
    print(optimized_get_top_5_repos("samuelcolvin"))