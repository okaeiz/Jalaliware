# Jalaliware

Jalaliware is a collection of useful tools for working with Jalali dates.

## Current Week Calculator
Use `current_week_calculator.py` to find the beginning and end of the current week in Jalali calendar. The function outputs a list of two dates according to the current date. You can access them using their index.

Example: If the current date is 2023-07-11, the function will output a list containing two elements:

```python
[2023-07-08 00:00:00, 2023-07-14 23:59:59]
```

These two dates can be accessed using their corresponding index:

```python
print(current_week_calculator()[0], ' is the beginning of the current week.')
print(current_week_calculator()[1], ' is the ending of the current week.')
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
