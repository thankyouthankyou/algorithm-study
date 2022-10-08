n = int(input())
parent_node_list = list(map(int,input().split()))
removed_node = int(input())

def remove_dfs(removed_node):
    parent_node_list[removed_node] = -2
    for i in range(len(parent_node_list)):
        if parent_node_list[i] == removed_node:
            remove_dfs(i)
            
remove_dfs(removed_node)

cnt=0
for i in range(len(parent_node_list)):
    if parent_node_list[i]!=-2 and i not in parent_node_list:
        cnt+=1
print(cnt)
# print(parent_node_list)