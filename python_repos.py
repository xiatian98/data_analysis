import requests

# 调用API
url = "https://api.github.com/search/repositories?q={python}{&sort=stars}"
# 使用第3版的API
headers = {'Accept': 'application/vnd.github.v3+json'}
# 存储响应
r = requests.get(url, headers=headers)
print(f"状态码: {r.status_code}")
# 将相应赋给一个变量
response_dict = r.json()
# print(response_dict.keys())
# # 上面的代码打印的信息：状态码: 200 dict_keys(['total_count', 'incomplete_results', 'items'])
# # items是一个包含很多字典的列表，每个字典都包含有关一个Python仓库的信息
print(f"仓库总数：{response_dict['total_count']}")
repo_dicts = response_dict['items']
# 打印长度获悉得到多少个仓库信息
print(f"返回的仓库数：{len(repo_dicts)}")
# 获取第一个仓库的信息
# repo_dict = repo_dicts[0]
# 打印字典包含的键数
# print(f"\nKeys:{len(repo_dict)}")
# 打印这个字典中的所有键
# for key in sorted(repo_dict.keys()):
#     print(key)

print("\nSelected information about first repository:")
for repo_dict in repo_dicts:
    print(f"Name:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f"Stars:{repo_dict['stargazers_count']}")
    print(f"Repository:{repo_dict['html_url']}")
    print(f"Description:{repo_dict['description']}")


# print(f"Created:{repo_dict['created_at']}")
# print(f"Updated:{repo_dict['updated_at']}")

