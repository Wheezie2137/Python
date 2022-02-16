def wordcount(msg):
    i=0
    space=0
    while i<len(msg):
        if msg[i]==" ":
            space=space+1
        i=i+1
    print ("In the message we found:",space+1)

wordcount("hello my friends")
wordcount("hello")
wordcount("hello my friends how are you")