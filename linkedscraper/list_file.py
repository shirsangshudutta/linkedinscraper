# # places_new = ['Berlin', 'Cape Town', 'Sydney', 'Moscow','Delhi']
# # def Diff(li1, li2):
# #     li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
# #     return li_dif
 

# # with open('listfile_new.txt', 'w') as filehandle:
# #     filehandle.writelines("%s\n" % place for place in places_new)

# # # open file and read the content in a list
# # places_old = []
# # with open('listfile.txt', 'r') as filehandle:
# #     places_old = [current_place.rstrip() for current_place in filehandle.readlines()]

# # frontier=[]
# # frontier=Diff(places_new, places_old) 
# # print(len(frontier)) 
# # print(len(places_old))  

# evens = ['Berlin', 'Cape Town', 'Sydney']
# odds = ['Moscow','Delhi']

# evens = odds + evens
# print(evens)  # [1, 3, 5, 2, 4, 6]   
with open('C:\\Users\\pc\\Desktop\\linkedin_sept\\linkedscraper\\visitedProfiles.txt', 'r') as filehandle:
    visitedProfiles = [current_link.rstrip() for current_link in filehandle.readlines()]           