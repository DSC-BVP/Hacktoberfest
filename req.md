 fname=input("Enter  name of file") 
  fopen=open(fname) 
  count=0 
  for letter in fopen: 
      if letter.startswith("From") : 
          count=count+1 
          split=letter.split() 
          print(split[1]) 
          print(count) 
