# lorem  (actually this is for the index page)
Ipsom
```
I want to get the following output:
```
# lorem
Ipsom
```
I tried the following:
```
sed -n '/^# lorem/,/^$/p' src/introduction.md
```
But it doesn't work. I get the following output:
```
# lorem
