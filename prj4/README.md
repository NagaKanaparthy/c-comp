# C- Quadruples Generator  
### Nagavarun Kanaparthy
## Goals
This program will generate simple quadruples as shown in the examples
below.
### Supported Quadruples Features
* scope (blocking)
* function
    * params
* variable allocation
    * arrays
* function calls
* control flow
    * while
    * if
        * else
* simple arithmetic
* assignment
## Examples
```c
Example 1

void main(void)
{
  int x;
  int y;
  int z;
  int m;
   while(x + 3 * y > 5)
   {
     x = y + m / z;
     m = x - y + z * m / z;
   }
}

----------------------------------------------------

1         func           main           void           0
2         alloc          4                             x
3         alloc          4                             y
4         alloc          4                             z
5         alloc          4                             m
6         mult           3              y              _t0 
7         add            x              _t0            _t1
8         comp           _t1            5              _t2
9         BRLEQ          _t2                           21
10        block
11        div            m              z              _t3
12        add            y              _t3            _t4
13        assign         _t4                           x
14        sub            x              y              _t5
15        times          z              m              _t6
16        div            _t6            z              _t7
17        add            _t5            _t7            _t8
18        assign         _t8                           m
19        end            block
20        BR                                           6
21        end            func           main
----------------------------------------------------
Example 2

int sub(int x, float y)
{
   return(x+x);
}
void main(void)
{
  int x;
  int y;
  y = sub(x);
}


----------------------------------------------------

1         func           sub            int            2
2         param
3         alloc          4                             x
4         param
5         alloc    		 4                             y
6         add            x              x              _t0
7         return                                       _t0
8         end            func           sub
9         func           main           void           0
10        alloc          4                             x
11        alloc          4                             y
12        arg                                          x
13        call           sub            1              _t1
14        assign         _t1                           y
15        end            func           main

Example 3

void main(void)
{
   int x[10];
   int y;
   y = (x[5] + 2) * y;
}

----------------------------------------------------

1   func    main		void        0
2   alloc   			40          x
3   alloc    			4           y
4   disp    x			20          _t0
5   add     _t0	        2           _t1
6   mult    _t1         y           _t2
7   assign  _t2			            y
8   end     func		main
```

