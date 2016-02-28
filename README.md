# pingprobe
A small asynchronous ping probing tool written in Python (for an online course)

## Sample usage

```
$ python3.5 pingProbe.py -n 10.0.1.0/24
```
Returns all hosts that reply
```
10.0.1.11                              
10.0.1.9                               
10.0.1.3                               
10.0.1.18                              
10.0.1.1                               
10.0.1.2                               
10.0.1.7                               
10.0.1.43                              
```
To get a nice sorted list you can pipe the output through *sort* and *uniq*
````
$ python3.5 pingProbe.py -n 10.0.1.0/24 | sort -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | uniq > sorted.txt
```

