

# Linear Programming

1) A Person wants to decide the constituents amount of diet which will fulfill his daily requirements of Proteins, Fats and Carbohydrates at a Minimum cost. The choice is to be made from four different types of foods. The yields per unit of those food are given below. Formulate Linear programming Model

| Food type                  | Yield per unit |            |               | Cost per unit (Rs) |
|----------------------------|----------------|------------|---------------|--------------------|
|                            | Proteins       | Fats       | Carbohydrates |                    |
| 1                          | 3              | 2          | 6             | 45                 |
| 2                          | 4              | 2          | 4             | 40                 |
| 3                          | 8              | 7          | 7             | 85                 |
| 4                          | 6              | 5          | 4             | 65                 |
| <b>Minimum Requirement</b> | <b>800</b>     | <b>200</b> | <b>700</b>    |                    |

## Solution:

Let  $X_1$  Amount of Type1 food to be taken, Let  $X_2$  Amount of Type2 to be taken, Let  $X_3$  Amount of Type3 to be taken, Let  $X_4$  Amount of Type4 to be taken,

$$Z_{\min} = 45X_1 + 40X_2 + 85X_3 + 65X_4 \text{ ----Objective Equation}$$

$$3X_1 + 4X_2 + 8X_3 + 6X_4 \ge 800 \text{ [Protein constrain]}$$

$$2X_1 + 2X_2 + 7X_3 + 5X_4 \ge 200 \text{ [Fats constrain]}$$

$$6X_1 + 4X_2 + 7X_3 + 4X_4 \ge 700 \text{ [Carbohydrates constrain]}$$

$$X_1 \ge 0, X_2 \ge 0, X_3 \ge 0, X_4 \ge 0 \text{ { Non negative Constrain}}$$

![A blue hand-drawn asterisk or star shape.](2173c0102e23a5ff29d90d4353fc0339_img.jpg)

A blue hand-drawn asterisk or star shape.

## Linear Programming

1) Old Hens can be bought for Rs. 300 each , Young one cost Rs. 500 each, Old Hen lay 3 eggs per week and young ones lay 5 eggs per week, Each egg being worth 6 Rs. A hen costs of Rs. 15 for feed. If a person has only 15000 to spend on the hens, How many of each kind should he buy to get a profit of more than 600 Rs. Per week Assuming that he cannot house more than 30 hens. Formulate Linear programming Model

## Solution:

Let X be the number of Old Hens to be brought,

Let Y be the number of Young Hens to be brought

|               | Old Hen        | Young Hen      |
|---------------|----------------|----------------|
| Cost          | 300            | 500            |
| Egg           | 3 Egg per week | 5 Egg per week |
| Feed          | 15 Rs.         | 15 Rs.         |
| Each Egg      | 6              | 6              |
| Selling price |                |                |

$Z_{Max} = SP - CP =$  since objective was not defined, i.e max. profit or minimize cost..we calc. profit by this

$$= (6 \times 3)X + (6 \times 5)Y - 15X - 15Y \{15 \times X \text{ indicate feed}\}$$

$$= 18X + 30Y - 15X - 15Y$$

$$Z_{Max} = 3X + 15Y \quad \text{----Objective Equation}$$

$$300X + 500Y \le 15000 \quad [\text{Cost constrain}]$$

$$X + Y \le 30 \quad [\text{Space constrain}]$$

$$X \ge 0, Y \ge 0 \quad [\text{Non Negative}]$$

$$3X + 15Y \ge 600 \quad [\text{Income Constrain}]$$

## Linear Programming

1) A farmer has a 100 acre farm, He can sell all the Tomatoes, Onion, Radishes he can raise, The price he can obtain is Rs.5 per kg Tomatoes, Rs.10 per kg Onion, Rs. 8 per kg for Radish, The average yield per acre is 2000 kg of Tomatoes, 3000 kg Onion, 1000 kg of Radish, Fertilizer is available at RS.5 per Kg, Amount of fertilizer require for each Tomatoe, Onion-100 Kg per acre, 50 Kg for Radish, Labour require for cultivating per acre is 5 man day for Tomatoes, 6 man day for Onion, 5 man day for Radish. A total 400 mans are available at Rs.500 per day. Formulate Linear programming Model.

## **Solution:**

|               | Tomatoes    | Onion        | Radish       |
|---------------|-------------|--------------|--------------|
| Selling Price | Rs.5 per kg | Rs.10 per kg | Rs. 8 per kg |
| Yield         | 2000kg/Acre | 3000kg/Acre  | 1000kg/Acre  |
| Fertilizer    | 100kg/Acre  | 100kg/Acre   | 50kg/Acre    |
| Cultivating   | 5 Man/Acre  | 20 Man/Acre  | 5 Man/Acre   |

Fertilizer rate: 5 Rs/kg

Each Labour Cost: Rs.500 per Day

|       |       |       |
|-------|-------|-------|
| $X_1$ | $X_2$ | $X_3$ |
|-------|-------|-------|

Let  $X_1$  be the number of acres to be used for growing Tomatoe.

Let  $X_2$  be the number of acres to be used for growing Onion.

Let  $X_3$  be the number of acres to be used for growing Radishes.

$$Z_{\max} = (2000 \times 5) X_1 + (3000 \times 10) X_2 + (1000 \times 8) X_3 - (100 \times 5) X_1 - (100 \times 5) X_2 - (50 \times 5) X_3 - (500 \times 5) X_1 - (20 \times 500) X_2 - (500 \times 5) X_3$$

profit= SP-CP

$$=10000X_1 + 30000 X_2 + 8000 X_3 - 500 X_1 - 500 X_2 - 250 X_3 - 2500 X_1 \\ - 10000 X_2 - 2500 X_3$$

$$Z_{\max} = 7000 X_1 + 19500 X_2 + 5250 X_3 \quad \{ \text{Objective equation} \}$$

**Constrains:**

$$5 X_1 + 20 X_2 + 5 X_3 \le 400 \quad \{ \text{Labour Constrain} \}$$

$$X_1 + X_2 + X_3 \le 100 \quad \{ \text{Land Constrain} \}$$

$$X_1 \ge 0, X_2 \ge 0, X_3 \ge 0 \quad \{ \text{Non negative Constrain} \}$$

![Hand-drawn blue triangle symbol with a circle inside, containing the number 2.](bb08c83fc8939517c6803d65c69dd06b_img.jpg)

Hand-drawn blue triangle symbol with a circle inside, containing the number 2.

2) A hospital has the following minimal daily requirement of nurses

| Period | Clock time    | Minimal Number of Nurses Required |
|--------|---------------|-----------------------------------|
| 1      | 6 AM to 10 AM | 2                                 |
| 2      | 10 AM to 2 PM | 7                                 |
| 3      | 2 PM to 6 PM  | 15                                |
| 4      | 6 PM to 10 PM | 8                                 |
| 5      | 10 PM to 2 AM | 20                                |
| 6      | 2 AM to 6 AM  | 6                                 |

Nurses report to the hospital at the beginning of each period and work for 8 consecutive hours. The hospital wants to determine the minimal number of nurses to be employed so that there is sufficient number of nurses available for each period. Formulate this as Linear programming problem

## **Solution:**

Let  $X_1, X_2, X_3, X_4, X_5, X_6$  number of nurses to be appointed for period 1,2,3,4,5,6 respectively.

**Objective equation:**  $Z_{\min} = X_1 + X_2 + X_3 + X_4 + X_5 + X_6$

## **Constrains**

$$X_1 + X_2 \ge 7$$

$$X_2 + X_3 \ge 15$$

$$X_3 + X_4 \ge 8$$

$$X_4 + X_5 \ge 20$$

$$X_5 + X_6 \ge 6$$

$$X_6 + X_1 \ge 2$$

$$X_1 \ge 0, X_2 \ge 0, X_3 \ge 0, X_4 \ge 0, X_5 \ge 0, X_6 \ge 0,$$

## Linear Programming

1) Consider the following problem faced by a production planner in a soft drink plant. He has 2 bottling machines A and B. A is assigned for 8-ounce bottle and B is assigned for 16-ounce bottle. The following data are available

| Machine A | 8ounce bottle | 16ounce bottle |
|-----------|---------------|----------------|
| A         | 100/ Minute   | 40/Minute      |
| B         | 60/Minute     | 75/Minute      |

The machines can be run for 8-hours per day, 5 days a week, Profit on 8 ounce bottle is 15 paise and on 16 ounce bottle is 25 paise. Weekly production of the drink cannot exceed 300000 ounces and the market can observe 25000 eight ounce bottle and 7000 sixteen ounce bottles per week. The planner wishes to maximize his profit, of course, to all the production and marketing constraints. Formulate Linear programming model.

## Solution

Let  $X_1$  be the number of 8 Ounce bottle to be produced on Machine A,  $X_2$  be the number of 16 ounce bottle to be produced on Machine A.

Let  $Y_1$  be the number of 8 ounce bottle to be produced on B,  $Y_2$  be the number of 16 ounce bottle to be produced on B.

$$Z_{\max} = (X_1 + Y_1) 0.15 + (X_2 + Y_2) 0.25 \quad [\text{Objective equation}]$$

|                                       |                   |                    |
|---------------------------------------|-------------------|--------------------|
| 1 Min-----100 products then 1 product | $\frac{1}{100}$   | duration requires  |
| Similarley for $X_1$ products         | $\frac{X_1}{100}$ | [ 8 Ounce bottles] |

1 Min----- 40 products    1 product  $\frac{1}{40}$  duration requires

Similarley for  $X_2$  products     $\frac{X_2}{40}$  [16 Ounce bottles]

$$\frac{X_1}{100} + \frac{X_2}{40} \le 5 \times 8 \times 60$$

$$\frac{Y_1}{60} + \frac{Y_2}{75} \le 5 \times 8 \times 60$$

$$\frac{2X_1 + 5X_2}{200} \le 2400$$

$$2X_1 + 5X_2 \le 480000$$

$$X_1 + Y_1 \ge 25000 \text{ [Market Constrain 8 ounce bottle]}$$

$$X_2 + Y_2 \ge 7000 \text{ [Market Constrain 16 ounce bottle]}$$

$$8(X_1 + Y_1) + 16(X_2 + Y_2) \le 300000$$

$$X_1 \ge 0, X_2 \ge 0, Y_1 \ge 0, Y_2 \ge 0$$

![Handwritten blue triangle symbol](dce81645e0100714e86d66fe4d06ecba_img.jpg) 2) A manufacture of a line of patent medicines is preparing a production plan on medicines A and B. There are sufficient ingredient available to make 20,000 bottles of A and 40000 bottles of B but there are only 45000 bottles into which both the medicines can be put. Further more it take 3 hours to prepare enough materials to fill 1000 bottles of A, it take 1 hour to prepare enough materials to fill 1000 bottles of B and there are 66 hours available for this operations. The profit is Rs.8 per bottle for A and Rs.7 per bottle for B. Formulate the linear programming model

**Solution:** Let  $x$  be the number of A type medicine to be produced  
Let  $y$  be the number of B type medicine to be produced

$$Z_{\max} = 8x + 7y \text{ [ objective]}$$

$$x \le 20000 \text{ [Bottle A constrain]}$$

$$y \le 40000 \text{ [Bottle B constrain]}$$

$$x + y \le 45000 \text{ [Together]}$$

![A blue hand-drawn star or asterisk symbol.](e0ebcd8fdcfd34b12de3601b59505fdd_img.jpg)

A blue hand-drawn star or asterisk symbol.

$$\frac{3}{1000} * x = \frac{3x}{1000}$$

$$\frac{1}{1000} * y = \frac{y}{1000}$$

$$\frac{3x}{1000} + \frac{3y}{1000} \le 66 \text{ hrs} \quad \text{Hours constrain}$$

$$X \ge 0, Y \ge 0$$

## Linear Programming

**Q1)** A firm can produce 3 types of cloth A,B,C. 3 kinds of wool required for it, Red wool,green wool, and blue wool.

One unit length of type A cloth needs 2 yards of red Wool and 3 yards of blue wool.one unit of length of type B cloth need 3 yard of red wool, 2 yards of green wool and 2 yards of blue wool. One unit of type c cloth needs 5 yards of green wool and 4 yards of blue wool. The firm has a stock of only 8 yards of red wool, 10 yads of green wool,and 15 yards of blue wool. It is assumed that the income obtained from one unit length of type A cloth is Rs 3, of type B cloth is Rs.5, of type C cloth is Rs. 4. Formulate the problem as a linear programming problem

## Solution:

Let  $X_1$  be the number of Type A cloth to be produced

Let  $X_2$  be the number of Type B cloth to be produced

Let  $X_3$  be the number of Type C cloth to be produced

**$Z_{\max} = 3X_1 + 5X_2 + 4X_3$  ----Objective Equation**

|        | Red    | Green  | Blue   |
|--------|--------|--------|--------|
| Type A | 2 Yard | -----  | 3 Yard |
| Type B | 3 Yard | 2 Yard | 2 Yard |
| Type C | -----  | 5 Yard | 4 Yard |

**Availability    8 Yard    10 Yard    15 Yard**

$2X_1 + 3X_2 \le 8$  {Red Wool Constrain}

$2X_1 + 5X_3 \le 10$  {Green Wool Constrain}

$3X_1 + 2X_2 + 4X_3 \le 15$  { Blue Wool Constrain}

$X_1 \ge 0, X_2 \ge 0, X_3 \ge 0$  { Non negative Constrain}

**Q2)** A firm Produce 3 Products, these products are processed in 3 different machine. The time required to manufacture one unit of each product and the daily capacity of machine 3 machine given below

| Machine | P1 | P2  | P3 | Machine capacity |
|---------|----|-----|----|------------------|
| M1      | 2  | 8   | 2  | 940 Min/day      |
| M2      | 4  | --- | 8  | 970 Min/day      |
| M3      | 2  | 5   | -- | 430 Min/day      |

Profit of product P1, P2, P3 are RS 4, Rs 8, Rs 6 Write a linear programming model to the given problem

**Solution:**

Let **a** be the number of Type P1 Product to be produced

Let **b** be the number of Type P2 Product to be produced

Let **c** be the number of Type P3 Product to be produced

**Z<sub>max</sub> = 4a + 8b + 6c** ----Objective Equation

**2a + 8b + 2c ≤ 940** { Machine P1 constrain}

**4a + 8c ≤ 970** { Machine P2 constrain}

**2a + 5b ≤ 430** { Machine P3 constrain}

**a ≥ 0, b ≥ 0, c ≥ 0** { Non negative Constrain}