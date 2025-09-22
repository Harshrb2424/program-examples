```bash
/d/obsidian/3.2/College/4th Year/exp4
> python program.py 
Original Data:
  Product Region  Year Quarter  Sales
0  Laptop   East  2023      Q1   1000
1  Laptop   West  2023      Q1    800
2  Laptop   East  2024      Q2   1200
3  Tablet   West  2023      Q3    600
4  Tablet   East  2024      Q4    900
5   Phone   East  2023      Q1    400
6   Phone   West  2023      Q2    700
7   Phone   West  2024      Q3    500

Data Cube (Pivot Table):
Year            2023            2024
Quarter           Q1   Q2   Q3    Q2   Q3   Q4
Product Region
Laptop  East    1000    0    0  1200    0    0
        West     800    0    0     0    0    0
Phone   East     400    0    0     0    0    0
        West       0  700    0     0  500    0
Tablet  East       0    0    0     0    0  900
        West       0    0  600     0    0    0

Roll-up (Total Sales by Year):
Year
2023    3500
2024    2600
Name: Sales, dtype: int64

Drill-down (Sales by Year & Quarter):
Year  Quarter
2023  Q1         2200
      Q2          700
      Q3          600
2024  Q2         1200
      Q3          500
      Q4          900
Name: Sales, dtype: int64

Slice (Sales in East Region):
  Product Region  Year Quarter  Sales
0  Laptop   East  2023      Q1   1000
2  Laptop   East  2024      Q2   1200
4  Tablet   East  2024      Q4    900
5   Phone   East  2023      Q1    400

Dice (Laptop Sales in 2023):
  Product Region  Year Quarter  Sales
0  Laptop   East  2023      Q1   1000
1  Laptop   West  2023      Q1    800

Pivot (Products vs Region):
Region   East  West
Product
Laptop   2200   800
Phone     400  1200
Tablet    900   600
```