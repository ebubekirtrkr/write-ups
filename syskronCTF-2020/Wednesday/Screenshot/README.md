# Screenshot
![](../../assets/Wednesday/screenshot_1.png)

Chall has a [image attachment](../../assets/Wednesday/Screenshot_2020-05-19_at_11.38.08_AM.png)  

From `even if it's not that significant` statement,  we can understand it is probably LSB related question.

If you open image with [stegsolve.jar](https://github.com/eugenekolo/sec-tools/tree/master/stego/stegsolve/stegsolve) and look around the planes, at red plane 1 you will see message below

![](../../assets/Wednesday/screenshot_2.png)

and at green plane 0 you will see

![](../../assets/Wednesday/screenshot_3.png) 

and  at its upper center

![](../../assets/Wednesday/screenshot_4.png)

Go to data exract section and exract data with green plane 0 , lsb and column settings checked.

![](../../assets/Wednesday/screenshot_5.png)

search `s` character in the [output file](../assets/Wednesday/Screenshot_output.txt)  to see flag.

![](../../assets/Wednesday/screenshot_6.png)

Flag : `syskronCTF{s3cr3T_m3sS4g3}`
