<h1 align="center">Пример работы с Python</h1>
<ul>
    <li>В данном коде нужно ввести чилос и выведется масив из чисел</li>
</ul>

<p aligh="center">
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSqXDLqIQoEeMb2QzO_CGQkr85wOX75Zgcjeg&s" width="100" height="100">
</p>

```python
    def generatorNumber(count):
    arr = [];
    
    for i in range(1, count + 1):
        arr.append(i);
        
    return arr;

    print(generatorNumber(5))
```