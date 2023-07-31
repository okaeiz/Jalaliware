# Jalaliware

Jalaliware is a collection of useful tools for working with Jalali dates.

## Current Week Calculator

Use [current_week_calculator.py ↗](https://github.com/okaeiz/Jalaliware/blob/main/current_week_calculator.py) to find the beginning and end of the current week in Jalali calendar. The function outputs a list of two dates according to the current date. You can access them using their index.

Example: If the current date is 2023-07-11, the function will output a list containing two elements:

```python
[2023-07-08 00:00:00, 2023-07-14 23:59:59]
```

These two dates can be accessed using their corresponding index:

```python
print(current_week_calculator()[0], ' is the beginning of the current week.')
print(current_week_calculator()[1], ' is the ending of the current week.')
```
Use [current_week_calculator.sql ↗](https://github.com/okaeiz/Jalaliware/blob/main/current_week_calculator.sql) which is a postgresql valid function and then access the outputs of the function using the following syntax:

```sql
SELECT * FROM current_week_calculator();
```
The above statement results in the following table:

```sql
2023-07-08 00:00:00.000000,2023-07-14 23:59:59.000000
```
Where the first result is begin_date and the second one is end_date.

## Previous Week Calculator

Use [previous_week_calculator.py ↗](https://github.com/okaeiz/Jalaliware/blob/main/previous_week_calculator.py) to find the beginning and end of the previous week in Jalali calendar. The function outputs a list of two dates according to the current date. You can access them using their index.

Example: If the current date is 2023-07-11, the function will output a list containing two elements:

```python
[2023-07-01 00:00:00, 2023-07-07 23:59:59]
```

These two dates can be accessed using their corresponding index:

```python
print(previous_week_calculator()[0], ' is the beginning of the previous week.')
print(previous_week_calculator()[1], ' is the ending of the previous week.')
```
Use [previous_week_calculator.sql ↗](https://github.com/okaeiz/Jalaliware/blob/main/previous_week_calculator.sql) which is a postgresql valid function and then access the outputs of the function using the following syntax:

```sql
SELECT * FROM previous_week_calculator();
```
The above statement results in the following table:

```sql
2023-07-01 00:00:00.000000,2023-07-07 23:59:59.000000
```
Where the first result is begin_date and the second one is end_date.

## English to Persian Digit Converter

Use `fdigit_replacer(x)` function in [farsikon.py ↗](https://github.com/okaeiz/Jalaliware/blob/main/farsikon.py) to convert English digits to Persian digits. The function takes an integer as input and outputs the equivalent Persian digits.

Example: If the input number is 2023, the function will return:

```python
'۲۰۲۳'
```

You can use this function as follows:

```python
print(fdigit_replacer(2023), ' is the Persian representation of 2023.')
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
