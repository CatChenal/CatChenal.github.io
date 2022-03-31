Python Peeves

This post lists examples of python code or style with explanations as to why they seem peevish to me. Here we go...

#1. (Mis)print
The print function earns the first spot for it is apparently mishandled even by "people paid to code".

## 1.1 Formating percentages: multiplying by 100 not needed!
I've seen this too many times:
```
print(f'formated percentage: {pct*100:.2f}%')
```
The percentage formating parameter `%` can take care of that:  
```
print(f'formated percentage: {pct:.2%}')
```

## 1.2 Concatenation inside `print`:
Apparently, many developers have a hidden typist in them. I've seen this a lot from coders who apparently do not know that the comma-separated items are concatenated with a space, the default separator:  
```
print('some text ' + str(value1) + ' other text ' + str(value2))
```

This simpler statement yields the same output:
```
# removed spaces around strings & after commas to show they're not needed:
print('some text',value1,'other text',value2) 
```
Output:
```
some text 1 other text 2
```
This works because of two parameters and their default values: `sep=' '` and `end='\n'`.
