```bash
/d/obsidian/3.2/College/4th Year/exp3
> python program.py 
Original Dataset:
     Customer ID        Name                  Email   Age       Location
0          C0065     Name_65     22Q91A6665@mrce.in  23.0         Guntur
1          C0066     Name_66     22Q91A6666@mrce.in  17.0     Karimnagar
2          C0067     Name_67     22Q91A6667@mrce.in   NaN        Medchal
3          C0068     Name_68     22Q91A6668@mrce.in  23.0   Secunderabad
4          C0069     Name_69                    NaN  17.0      Hyderabad
...          ...         ...                    ...   ...            ...
9931       C9996   Name_9996   22Q91A669996@mrce.in  25.0  Visakhapatnam
9932       C9997   Name_9997   22Q91A669997@mrce.in  24.0       Warangal
9933       C9998   Name_9998   22Q91A669998@mrce.in  24.0  Visakhapatnam
9934       C9999   Name_9999   22Q91A669999@mrce.in  23.0     Vijayawada
9935      C10000  Name_10000  22Q91A6610000@mrce.in  26.0   Secunderabad

[9936 rows x 5 columns]

============================================================

Horizontal Partition 1 (First Half):
     Customer ID       Name                 Email  Age       Location
0          C0065    Name_65    22Q91A6665@mrce.in   23         Guntur
1          C0066    Name_66    22Q91A6666@mrce.in   17     Karimnagar
2          C0067    Name_67    22Q91A6667@mrce.in   21        Medchal
3          C0068    Name_68    22Q91A6668@mrce.in   23   Secunderabad
4          C0069    Name_69               Unknown   17      Hyderabad
...          ...        ...                   ...  ...            ...
4963       C5028  Name_5028               Unknown   21         Kerala
4964       C5029  Name_5029  22Q91A665029@mrce.in   21         Guntur
4965       C5030  Name_5030  22Q91A665030@mrce.in   24  Visakhapatnam
4966       C5031  Name_5031  22Q91A665031@mrce.in   19     Karimnagar
4967       C5032  Name_5032  22Q91A665032@mrce.in   18         Guntur

[4968 rows x 5 columns]

Horizontal Partition 2 (Second Half):
     Customer ID        Name                  Email  Age       Location
4968       C5033   Name_5033   22Q91A665033@mrce.in   20   Secunderabad
4969       C5034   Name_5034   22Q91A665034@mrce.in   20        Medchal
4970       C5035   Name_5035   22Q91A665035@mrce.in   19      Nizamabad
4971       C5036   Name_5036   22Q91A665036@mrce.in   22  Visakhapatnam
4972       C5037   Name_5037   22Q91A665037@mrce.in   23         Guntur
...          ...         ...                    ...  ...            ...
9931       C9996   Name_9996   22Q91A669996@mrce.in   25  Visakhapatnam
9932       C9997   Name_9997   22Q91A669997@mrce.in   24       Warangal
9933       C9998   Name_9998   22Q91A669998@mrce.in   24  Visakhapatnam
9934       C9999   Name_9999   22Q91A669999@mrce.in   23     Vijayawada
9935      C10000  Name_10000  22Q91A6610000@mrce.in   26   Secunderabad

[4968 rows x 5 columns]

--------------------------------------------------

Vertical Partition 1 (Customer Info - ID, Name, Email):
     Customer ID        Name                  Email
0          C0065     Name_65     22Q91A6665@mrce.in
1          C0066     Name_66     22Q91A6666@mrce.in
2          C0067     Name_67     22Q91A6667@mrce.in
3          C0068     Name_68     22Q91A6668@mrce.in
4          C0069     Name_69                Unknown
...          ...         ...                    ...
9931       C9996   Name_9996   22Q91A669996@mrce.in
9932       C9997   Name_9997   22Q91A669997@mrce.in
9933       C9998   Name_9998   22Q91A669998@mrce.in
9934       C9999   Name_9999   22Q91A669999@mrce.in
9935      C10000  Name_10000  22Q91A6610000@mrce.in

[9936 rows x 3 columns]

Vertical Partition 2 (Demographics - Age, Location):
      Age       Location
0      23         Guntur
1      17     Karimnagar
2      21        Medchal
3      23   Secunderabad
4      17      Hyderabad
...   ...            ...
9931   25  Visakhapatnam
9932   24       Warangal
9933   24  Visakhapatnam
9934   23     Vijayawada
9935   26   Secunderabad

[9936 rows x 2 columns]

--------------------------------------------------

Round Robin Partition 1 (Even-indexed Rows):
     Customer ID       Name                 Email  Age      Location
0          C0065    Name_65    22Q91A6665@mrce.in   23        Guntur
2          C0067    Name_67    22Q91A6667@mrce.in   21       Medchal
4          C0069    Name_69               Unknown   17     Hyderabad
6          C0071    Name_71    22Q91A6671@mrce.in   18        Kerala
8          C0073    Name_73               Unknown   24     Nizamabad
...          ...        ...                   ...  ...           ...
9926       C9991  Name_9991  22Q91A669991@mrce.in   24  Secunderabad
9928       C9993  Name_9993  22Q91A669993@mrce.in   21  Secunderabad
9930       C9995  Name_9995  22Q91A669995@mrce.in   17        Kerala
9932       C9997  Name_9997  22Q91A669997@mrce.in   24      Warangal
9934       C9999  Name_9999  22Q91A669999@mrce.in   23    Vijayawada

[4968 rows x 5 columns]

Round Robin Partition 2 (Odd-indexed Rows):
     Customer ID        Name                  Email  Age       Location
1          C0066     Name_66     22Q91A6666@mrce.in   17     Karimnagar
3          C0068     Name_68     22Q91A6668@mrce.in   23   Secunderabad
5          C0070     Name_70     22Q91A6670@mrce.in   23     Vijayawada
7          C0072     Name_72     22Q91A6672@mrce.in   22        Medchal
9          C0074     Name_74     22Q91A6674@mrce.in   19     Vijayawada
...          ...         ...                    ...  ...            ...
9927       C9992   Name_9992   22Q91A669992@mrce.in   16  Visakhapatnam
9929       C9994   Name_9994   22Q91A669994@mrce.in   25      Hyderabad
9931       C9996   Name_9996   22Q91A669996@mrce.in   25  Visakhapatnam
9933       C9998   Name_9998   22Q91A669998@mrce.in   24  Visakhapatnam
9935      C10000  Name_10000  22Q91A6610000@mrce.in   26   Secunderabad

[4968 rows x 5 columns]

--------------------------------------------------

Hash Partition 1 (Customer ID % 2 == 0):
     Customer ID        Name                  Email  Age       Location
1          C0066     Name_66     22Q91A6666@mrce.in   17     Karimnagar
3          C0068     Name_68     22Q91A6668@mrce.in   23   Secunderabad
5          C0070     Name_70     22Q91A6670@mrce.in   23     Vijayawada
7          C0072     Name_72     22Q91A6672@mrce.in   22        Medchal
9          C0074     Name_74     22Q91A6674@mrce.in   19     Vijayawada
...          ...         ...                    ...  ...            ...
9927       C9992   Name_9992   22Q91A669992@mrce.in   16  Visakhapatnam
9929       C9994   Name_9994   22Q91A669994@mrce.in   25      Hyderabad
9931       C9996   Name_9996   22Q91A669996@mrce.in   25  Visakhapatnam
9933       C9998   Name_9998   22Q91A669998@mrce.in   24  Visakhapatnam
9935      C10000  Name_10000  22Q91A6610000@mrce.in   26   Secunderabad

[4968 rows x 5 columns]

Hash Partition 2 (Customer ID % 2 == 1):
     Customer ID       Name                 Email  Age      Location
0          C0065    Name_65    22Q91A6665@mrce.in   23        Guntur
2          C0067    Name_67    22Q91A6667@mrce.in   21       Medchal
4          C0069    Name_69               Unknown   17     Hyderabad
6          C0071    Name_71    22Q91A6671@mrce.in   18        Kerala
8          C0073    Name_73               Unknown   24     Nizamabad
...          ...        ...                   ...  ...           ...
9926       C9991  Name_9991  22Q91A669991@mrce.in   24  Secunderabad
9928       C9993  Name_9993  22Q91A669993@mrce.in   21  Secunderabad
9930       C9995  Name_9995  22Q91A669995@mrce.in   17        Kerala
9932       C9997  Name_9997  22Q91A669997@mrce.in   24      Warangal
9934       C9999  Name_9999  22Q91A669999@mrce.in   23    Vijayawada

[4968 rows x 5 columns]
```