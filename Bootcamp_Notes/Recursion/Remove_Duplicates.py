def Remove_Duplicates(str):
      if len(str)<2:
          return str
      if str[0]!=str[1]:
          return str[0]+Remove_Duplicates(str[1:])
      return Remove_Duplicates(str[1:])

str=input("Enter a string:")
ans=Remove_Duplicates(str)
print(ans)