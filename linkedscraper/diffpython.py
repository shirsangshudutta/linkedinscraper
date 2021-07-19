
# # Import pandas library
# import pandas as pd
 
# # initialize list of lists
# data1 = [['tom', 10], ['nick', 15], ['juli', 14]]
# data2 = [['tom', 10], ['nick', 14], ['john', 21]]

# # Create the pandas DataFrame
# df1 = pd.DataFrame(data1, columns = ['Name', 'Age'])
# df2 = pd.DataFrame(data2, columns = ['Name', 'Age'])

# print(df1)
# print(df2)
# print(df2!=df1)
# # print dataframe.

link2="https://www.linkedin.com/in/ayan7926?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAABDmvnIBixb7E6GUMTyWbSFU6JTd6DFcBSM"
link3=link2.partition("?")[0]
print(link3)
