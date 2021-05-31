#enmuerate use for if we want something remove from list without initalize any variable so we can that list as enumerate
l1=["Java","Python","JavaScript","Php"]
# i=0
# for item in l1:
#     if i%2==0:
#         print(f"Learn language {item}")
#     i+=1
#  same using enumerate
for i,item in enumerate(l1):
    if i%2==0:
        print(f"Learn language {item}")