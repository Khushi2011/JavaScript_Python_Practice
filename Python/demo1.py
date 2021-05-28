dict_1 = {}
n = int(raw_input())
for _ in range(n):
    name = raw_input()
    score = float(raw_input())
    dict_1.update({name: score})

dict_3 = sorted(dict_1.values())
def ans():
    for i in range(0,n-1):
        if abs(dict_3[i]-dict_3[i+1])>1e-9:
            ans=dict_3[i+1]
            return ans
ans=ans()
key_list=list(dict_1.keys())
value_list=list(dict_1.values())
i=0
pos=0
flag=0
# while i<=n:
#     if value_list[i]==ans:
#         if flag==1 and pos!=0:
#             pos+=1
#         else:
#             pos=value_list.index(ans)
#             flag=1
#             print(key_list[pos])
#     i+=1




