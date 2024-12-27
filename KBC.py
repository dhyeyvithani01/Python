Question = [
    [
        "Which of these is a primary color?","Green","Red","Purple","Orange","B"
    ],
    [
        "Who wrote the famous book 'Harry Potter and the Sorcerer's Stone?","J.R.R. Tolkien","J.K. Rowling","George R.R. Martin","C.S. Lewis","B"
    ],
    [
        "In which country would you find the historical site of Machu Picchu?","Brazil","Peru","Mexico","Ecuador","B"
    ],
    [
        "What is the capital city of Canada?","Vancouver","Torrento","Ottawa","Montreal","C"
    ],
    [
        "Who is the author of the book 'The God of Small Things'?","Amitav Ghosh","Vikram Seth","Kiran Desai","Arundhati Roy","D"
    ],
    [
        "In which year did India launch its first mission to Mars, called 'Mangalyaan'?","2013","2009","2014","2019","A"
    ]
    [
        "Who invented the telephone?","Nikola Tesla","Thomas Edison","Alexander Graham Bell","Albert Einstein","C"
    ]
]

Level = [10000,20000,40000,80000,160000,320000,640000,1200000]

for i in range(0,len(Question)):
    print(f"Question for rs.{Level[i]} is {Question[i][0]}")
    print(f"A. {Question[i][1]}  B. {Question[i][2]}")
    print(f"C. {Question[i][3]}  D. {Question[i][4]}")
