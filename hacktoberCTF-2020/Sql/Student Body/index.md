# Student Body
![image](assets/sql/student-body_1.png)
[Zip File](assets/sql/shallowgraveu.zip) 
First we need to find who is `SOCI424` professor of `Lucia`.
To find `user_id`of Lucia
```sql
	SELECT * FROM users WHERE first like 'lucia'
```
![image](assets/sql/student-body_2.png)
Her `user_id` is `49`.

To find `enrollments` that `Lucia` made
```sql
	SELECT * FROM `enrollments` WHERE `user_id`=49
```
![image](assets/sql/student-body_3.png)

To find `courses` with name `SOCI424 `
```sql
	SELECT * FROM courses WHERE title="SOCI424"
```
![image](assets/sql/student-body_4.png)
so `SOCI424`'s `cours_id` is 6775

To find `term_course_id` for the use in  `enrollments`
```sql
	SELECT * FROM `term_courses` WHERE `course_id`=6775
```
![image](assets/sql/student-body_5.png)

From last query we can obtain that Lucia takes course with the `term_course_id` 640
whose instructror id is 480
To see who the prof is
```sql
	SELECT * FROM `a`.`users` WHERE `user_id` = 480
```
![image](assets/sql/student-body_6.png)

We find the last part of flag which is `: flag{???_CLAUDEDARRACOTT}`

Let's find term courses whose instructos is `CLAUDE DARRACOTT`
```sql
	SELECT * FROM `term_courses` WHERE `instructor`=480

```
![image](assets/sql/student-body_7.png)


Then find enrollments' count that have `term_course_id` from previous query
```sql
	SELECT COUNT(*) FROM `enrollments` WHERE `term_crs_id` in (SELECT term_crs_id FROM `term_courses` WHERE `instructor`=480)
```
![image](assets/sql/student-body_8.png)


Flag: `flag{122_CLAUDEDARRACOTT}` 
