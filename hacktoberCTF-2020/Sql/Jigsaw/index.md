# Jigsaw
![image](assets/sql/jigsaw_1.png)
[Zip File](assets/sql/shallowgraveu.zip) 


I use rwgexp for that.
[Geekforgeeks](https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/)
my sql query was
```sql
	SELECT * FROM `users` WHERE `last` REGEXP '^[KRI][KRI]....[E-N]$'
```
`^`: for begining of string
`[KRI]`: for one char from 'K','R' or 'I'
`[KRI]`: for one char from 'K','R' or 'I'
`....` : for any character except newline, then three letters 
`[E-N]`: for one char between 'E' to 'N'
`$`: for begining of string
![image](assets/sql/jigsaw_2.png)
Flag: `flag{image.wa1k3624}` 
