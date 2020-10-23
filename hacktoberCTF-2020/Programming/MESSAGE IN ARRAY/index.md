# MESSAGE IN ARRAY
![](assets/programming/message-in-array_1.png)
```java
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GhostTown
{
    class Program
    {
        static void Main(string[] args)
        {
           string[] str = new string[4] {"DEADFACE","Nothing", "Stop", "Will"};

           Console.WriteLine("{1} {3} {2} {0}", str);
         }
    }
}
```
`{1}` : `Nothing` 
`{3}` : `Will` 
`{2}` : `Stop` 
`{0}` : `DEADFACE` 

Flag: `flag{Nothing Will Stop DEADFACE}` 
