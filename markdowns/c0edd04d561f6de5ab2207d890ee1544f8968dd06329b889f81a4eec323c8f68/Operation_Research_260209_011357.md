# Linear Programming

1) A Person wants to decide the constituents amount of diet which will fulfill his daily requirements of Protiens,Fats and Carbohydrates at a Minimum cost. The choice is to be made from four different types of foods. The yields per unit of those food are given below. Formulate Linear programming Model

<table><tr><td rowspan="2">Food type</td><td colspan="3">Yield per unit</td><td rowspan="2">Cost per unit (Rs)</td></tr><tr><td>Proteins</td><td>Fats</td><td>Carbohydrates</td></tr><tr><td>1</td><td>3</td><td>2</td><td>6</td><td>45</td></tr><tr><td>2</td><td>4</td><td>2</td><td>4</td><td>40</td></tr><tr><td>3</td><td>8</td><td>7</td><td>7</td><td>85</td></tr><tr><td>4</td><td>6</td><td>5</td><td>4</td><td>65</td></tr><tr><td>Minimum 
Requirement</td><td>800</td><td>200</td><td>700</td><td></td></tr></table>

## Solution:

Let \(\mathsf { X } _ { 1 }\) Amount of Type1 food to be taken, Let \({ \tt X } _ { 2 }\) Amount of Type2 to be taken, Let \({ \sf X } _ { 3 }\) Amount of Type3 to be taken, Let \({ \tt X } _ { 4 }\) Amount of Type4 to be taken,

\[
Z _ {\min } = 4 5 X _ {1} + 4 0 X _ {2} + 8 5 X _ {3} + 6 5 X _ {4} - - - \text {O b j e c t i v e E q u a t i o n}
\]

\[
3 X _ {1} + 4 X _ {2} + 8 X _ {3} + 6 X _ {4} > = 8 0 0 [ \text {P r o t e i n c o n s t r a i n} ]
\]

\[
2 X _ {1} + 2 X _ {2} + 7 X _ {3} + 5 X _ {4} > = 2 0 0 [ \text {F a t s c o n s t r a i n} ]
\]

\[
6 X _ {1} + 4 X _ {2} + 7 X _ {3} + 4 X _ {4} > = 7 0 0 [ \text {C a r b o h y d r a t e s c o n s t r a i n} ]
\]

\[
X _ {1} > = 0, X _ {2} > = 0, X _ {3} > = 0, X _ {4} > = 0 \left\{\text {N o n n e g a t i v e C o n s t r a i n} \right\}
\]

![](images/b8a58414a61006bad4d406cdc9f9906867f9c84126f6bb762db858e2bb543baf.jpg)

# Linear Programming

1) Old Hens can be bought for Rs. 300 each , Young one cost Rs. 500 each, Old Hen lay 3 eggs per week and young ones lay 5 eggs per week, Each egg being worth 6 Rs. A hen costs of Rs. 15 for feed. If a person has only 15000 to spend on the hens, How many of each kind should he buy to get a profit of more than 600 Rs. Per week Assuming that he cannot house more than 30 hens.Formulate Linear programming Model

## Solution:

Let X be the number of Old Hens to be brought,

Let Y be the number of Young Hens to be brought

<table><tr><td></td><td>Old Hen</td><td>Young Hen</td></tr><tr><td>Cost</td><td>300</td><td>500</td></tr><tr><td>Egg</td><td>3 Egg per week</td><td>5 Egg per week</td></tr><tr><td>Feed</td><td>15 Rs.</td><td>15 Rs.</td></tr><tr><td>Each Egg</td><td>6</td><td>6</td></tr></table>

Selling price

\[
Z _ {M a x} = S P - C P =
\]

since objective was not defined, i.e max. profit or minimize cost.we calc profit by this

\[
\begin{array}{l} = (6 ^ {*} 3) X + (6 ^ {*} 5) Y - 1 5 ^ {*} X - 1 5 ^ {*} Y \{1 5 ^ {*} X i n d i c a t e f e e d \} \\ = 1 8 X + 3 0 Y - 1 5 X - 1 5 Y \\ \end{array}
\]

\[
\begin{array}{l} Z _ {M a x} = 3 X + 1 5 Y \quad - - - - O b j e c t i v e E q u a t i o n \\ 3 0 0 X + 5 0 0 Y <   = 1 5 0 0 0 [ \text {C o s t c o n s t r a i n} ] \\ X + Y <   = 3 0 [ \text {S p a c e c o n s t r a i n} ] \\ X > = 0, Y > = 0 [ N o n N e g a t i v e ] \\ 3 X + 1 5 Y > = 6 0 0 [ I n c o m e C o n s t r a i n ] \\ \end{array}
\]

# Linear Programming

1) A farmer has a 100 acre farm, He can sell all the Tomatoes,Onion, Radishes he can raise, The price he can obtain is Rs.5 per kg Tomatoes, Rs.10 per kg Onion,Rs. 8 per kg for Radish,The average yield per acre is \(2 0 0 0 \mathrm { k g }\) of Tomatoes,3000 kg Onion, \(1 0 0 0 ~ \mathrm { k g }\) of Radish, Fertilizer is available at RS.5 per Kg, Amount of fertilizer require for each Tomatoe,Onion- \(1 0 0 \mathrm { K g }\) per acre, \(5 0 ~ \mathrm { K g }\) for Radish,Labour require for cultivating per ace is 5 man day for Tomatoes,6 man day for Onion,5 man day for Radish. A total 400 mans are available at Rs.500 per day. Formulate Linear programming Model.

## Solution:

<table><tr><td></td><td>Tomatoes</td><td>Onion</td><td>Radish</td></tr><tr><td>Selling Price</td><td>Rs.5 per kg</td><td>Rs.10 per kg</td><td>Rs. 8 per kg</td></tr><tr><td>Yield</td><td>2000kg/Acre</td><td>3000kg/Acre</td><td>1000kg/Acre</td></tr><tr><td>Fertilizer</td><td>100kg/Acre</td><td>100kg/Acre</td><td>50kg/Acre</td></tr><tr><td>Cultivating</td><td>5 Man/Acre</td><td>20 Man/Acre</td><td>5 Man/Acre</td></tr></table>

Fertilizer rate: 5 Rs/kg

Each Labour Cost: Rs.500 per Day

<table><tr><td>X1</td><td>X2</td><td>X3</td></tr></table>

Let \(X _ { 1 }\) be the number of acres to be used for growing Tomatoe.

Let \(X _ { 2 }\) be the numbe of acrs to be used for growing Onion.

Let \(X _ { 3 }\) be the numbe of acrs to be used for growing Radishes.

\[
Z _ {\max } = (2 0 0 0 * 5) X _ {1} + (3 0 0 0 * 1 0) X _ {2} + (1 0 0 0 * 8) X _ {3} - (1 0 0 * 5) X _ {1}
\]

\[
- (1 0 0 ^ {*} 5) X _ {2} - (5 0 ^ {*} 5) X _ {3} - (5 0 0 ^ {*} 5) X _ {1} - (2 0 ^ {*} 5 0 0) X _ {2} - (5 0 0 ^ {*} 5) X _ {3}
\]

\[
\begin{array}{l} = 1 0 0 0 0 \mathrm {X} _ {1} + 3 0 0 0 0 \mathrm {X} _ {2} + 8 0 0 0 \mathrm {X} _ {3} - 5 0 0 \mathrm {X} _ {1} - 5 0 0 \mathrm {X} _ {2} - 2 5 0 \mathrm {X} _ {3} - 2 5 0 0 \mathrm {X} _ {1} \\ - 1 0 0 0 0 \mathrm {X} _ {2} - 2 5 0 0 \mathrm {X} _ {3} \\ \end{array}
\]

Zmax= 7000 X1 + 19500 X2 + 5250 X3 { Objective equation }

## Constrains:

\[
\begin{array}{l} 5 \mathrm {X} _ {1} + 2 0 \mathrm {X} _ {2} + 5 \mathrm {X} _ {3} <   = 4 0 0 \{\text {L a b o u r C o n s t r a i n} \} \\ \mathrm {X} _ {1} + \mathrm {X} _ {2} + \mathrm {X} _ {3} <   = 1 0 0 \{\text {L a n d C o n s t r a i n} \} \\ X _ {1} > = 0, X _ {2} > = 0, X _ {3} > = 0 \left\{\text {N o n n e g a t i v e C o n s t r a i n} \right\} \\ \end{array}
\]

<table><tr><td>Period</td><td>Clock time</td><td>Minimal Number of Nurses Required</td></tr><tr><td>1</td><td>6 AM to 10 AM</td><td>2</td></tr><tr><td>2</td><td>10 AM to 2 PM</td><td>7</td></tr><tr><td>3</td><td>2 PM to 6 PM</td><td>15</td></tr><tr><td>4</td><td>6 PM to 10 PM</td><td>8</td></tr><tr><td>5</td><td>10 PM to 2 AM</td><td>20</td></tr><tr><td>6</td><td>2 AM to 6 AM</td><td>6</td></tr></table>

Nurses report to the hospital at the beginning of each period and work for 8 consecutive hours. The hospital wants to determine the minimal number of nurses to be employed so that there is sufficient number of nurses available for each period. Formulate this as Linear programming problem

## Solution:

Let \(\mathrm { X } _ { 1 } , \mathrm { X } _ { 2 } , \mathrm { X } _ { 3 } , \mathrm { X } _ { 4 } , \mathrm { X } _ { 5 } , \mathrm { X } _ { 6 }\) number of nurses to be appointed for period 1,2,3,4,5,6 respectiveley.

Objective equation: \(\mathrm { Z _ { m i n } } = \mathrm { X } _ { 1 } + \mathrm { X } _ { 2 } + \mathrm { X } _ { 3 } + \mathrm { X } _ { 4 } + \mathrm { X } _ { 5 } + \mathrm { X } _ { 6 }\)

### Constrains

\[
\mathrm {X} _ {1} + \mathrm {X} _ {2} > = 7
\]

\[
\mathrm {X} _ {2} + \mathrm {X} _ {3} > = 1 5
\]

\[
\mathrm {X} _ {3} + \mathrm {X} _ {4} > = 8
\]

\[
\mathrm {X} _ {4} + \mathrm {X} _ {5} > = 2 0
\]

\[
\mathrm {X} _ {5} + \mathrm {X} _ {6} > = 6
\]

\[
\mathrm {X} _ {6} + \mathrm {X} _ {1} > = 2
\]

\[
\mathrm {X} _ {1} > = 0, \mathrm {X} _ {2} > = 0, \mathrm {X} _ {3} > = 0, \mathrm {X} _ {4} > = 0, \mathrm {X} _ {5} > = 0, \mathrm {X} _ {6} > = 0,
\]

# Linear Programming

1) Consider the following problem faced by a production planner in a soft drink plant. He has 2 bottling machines A and B. A is assigned for 8-ounce bottle and B is assigned for 16-ounce bottle. The following data are available

Machine A 8ounce bottle 16ounce bottle

A 100/ Minute 40/Minute

B 60/Minute 75/Minute

The machines can be run for 8-hours per day,5 days a week, Profit on 8 ounce bottle is 15 paise and on 16 ounce bottle is 25 paise. Weekly production of the drink cannot exceed 300000 ounces and the market can obserb 25000 eight ounce bottle and 7000 sixteen ouce bottles per week. The planner wishes to maximize his profit,of course,to all the production and marketing constrains. Formulate Linear programming model.

## Solution

Let \(\mathrm { X } _ { 1 }\) be the number of 8 Ounce bottle to be produced on Machine A, \(X _ { 2 }\) be the number of 16 ounce bottle to be produced on Machine A.

Let \(\mathrm { Y } _ { 1 }\) be the number of 8 ounce bottle to be produced on B, \(\mathrm { Y } _ { 2 }\) be the number of 16 ounce bottle to be produced on B.

\[
Z _ {\max } = \left(X _ {1} + Y _ {1}\right) 0. 1 5 + \left(X _ {2} + Y _ {2}\right) 0. 2 5 [ \text {O b j e c t i v e e q u a t i o n} ]
\]

1 Min----100 products then 1 product 1 duration requires 100 Similarley for \(\mathrm { X } _ { 1 }\) products X1 [ 8 Ounce bottles] 100

1 Min----- 40 products 1 product 1 duration requires 40

Similarley for \(X _ { 2 }\) products X2 [16 Ounce bottles] 40

\[
\begin{array}{l} \frac {X _ {1}}{1 0 0} + \frac {X _ {2}}{4 0} <   = 5 ^ {*} 8 ^ {*} 6 0 \\ \frac {Y _ {1}}{6 0} + \frac {Y _ {2}}{7 5} <   = 5 ^ {*} 8 ^ {*} 6 0 \\ \end{array}
\]

\[
\begin{array}{l} \frac {2 X _ {1} + 5 X _ {2}}{2 0 0} <   = 2 4 0 0 \\ 2 \mathrm {X} _ {1} + 5 \mathrm {X} _ {2} <   = 4 8 0 0 0 0 \\ \end{array}
\]

X1 + Y1 > = 25000[Market Constrain 8 ounce bottle]

\(\mathrm { X } _ { 2 } + \mathrm { Y } _ { 2 } > = 7 0 0 0\) [Market Constrain 16 ounce bottle]

\[
8 \left(\mathrm {X} _ {1} + \mathrm {Y} _ {1}\right) + 1 6 \left(\mathrm {X} _ {2} + \mathrm {Y} _ {2}\right) <   = 3 0 0 0 0 0
\]

\[
\mathrm {X} _ {1} > = 0, \mathrm {X} _ {2} > = 0, \mathrm {Y} _ {1} > = 0, \mathrm {Y} _ {2} > = 0
\]

2) A manufacture of a line of patent medicines is preparing a production plan on medicines A and B. There are sufficient ingredient available to make 20,000 bottles of A and 40000 bottles of B but there are only 45000 bottles into which both the medicines can be put. Further more it take 3 hours to prepareenough materials to fill 1000 bottles of A, it take 1 hour to prepare enough materials to fill 1000 bottles of B and there are 66 hours available for this operations. The profit is Rs.8 perbottle for A and Rs.7 perbottle for B. Formulate the linear programming model

Solution: Let x be the number of A type medicine to be produced Let y be the number of B type medicine to be produced

![](images/c9d30567ee37e58cbe44d2bfeadfed703ac7a4f9eb0208728500f9d0ddf1c5da.jpg)

\[
\begin{array}{l} Z _ {\max } = 8 x + 7 y [ o b j e c t i v e ] \\ \mathrm {x} <   = 2 0 0 0 0 [ \text {B o t t l e A c o n s t r a i n} ] \\ \mathrm {y} <   = 4 0 0 0 0 [ \text {B o t t l e B c o n s t r a i n} ] \\ \mathrm {x} + \mathrm {y} <   = 4 5 0 0 0 [ \text {T o g e t h e r} ] \\ \end{array}
\]

![](images/2c5623349b2875869392afc60da0258d9bbb1cd667c010a7e914ca66417434ec.jpg)

\[
\begin{array}{l} \frac {3}{1 0 0 0} * x = \frac {3 x}{1 0 0 0} \\ \frac {1}{1 0 0 0} \quad \star \quad y = \quad \frac {y}{1 0 0 0} \\ \frac {3 x}{1 0 0 0} + \frac {3 y}{1 0 0 0} <   = 6 6 h r s \quad \text {H o u r s c o n s t r a i n} \\ X > = 0, Y > = 0 \\ \end{array}
\]

# Linear Programming

Q1) A firm can produce 3 types of cloth A,B,C. 3 kinds of wool required for it, Red wool,green wool, and blue wool.

One unith length of type A cloth needs 2 yards of red Wool and 3 yards of blue wool.one unit of length of type B cloth need 3 yard of red wool, 2 yards of green wool and 2 yards of blue wool. One unit of type c cloth needs 5 yards of green wool and 4 yards of blue wool. The firm has a stock of only 8 yards of red wool, 10 yads of green wool,and 15 yards of blue wool. It is assumed that the income obtained from one unit length of type A cloth is Rs 3, of type B cloth is Rs.5, of type C cloth is Rs. 4. Formulate the problem as a linear programming problem

## Solution:

Let \(\mathsf { X } _ { 1 }\) be the number of Type A cloth to be produced

Let X2 be the number of Type B cloth to be produced

Let X3 be the number of Type C cloth to be produced

\(Z _ { \operatorname* { m a x } { } } = 3 X _ { 1 } + 5 X _ { 2 } + 4 X _ { 3 }\) ----Objective Equation

<table><tr><td></td><td>Red</td><td>Green</td><td>Blue</td></tr><tr><td>Type A</td><td>2 Yard</td><td>----</td><td>3 Yard</td></tr><tr><td>Type B</td><td>3 Yard</td><td>2 Yard</td><td>2 Yard</td></tr><tr><td>Type C</td><td>----</td><td>5 Yard</td><td>4 Yard</td></tr></table>

Availability

8 Yard

10 Yard

15 Yard

\[
2 X _ {1} + 3 X _ {2} <   = 8 \{\text {R e d W o o l C o n s t r a i n} \}
\]

\[
2 X _ {1} + 5 X _ {3} <   = 1 0 \{G r e e n W o o l C o n s t r i n \}
\]

\[
3 X _ {1} + 2 X _ {2} + 4 X _ {3} <   = 1 5 \{\text {B l u e W o o l C o n s t r a i n} \}
\]

\[
X _ {1} > = 0, X _ {2} > = 0, X _ {3} > = 0 \{\text {N o n n e g a t i v e C o n s t r a i n} \}
\]

Q2) A firm Produce 3 Products,these products are processed in 3 different machine. The time required to manufacture one unit of each product and the daily capacity of machine 3 machine given below

<table><tr><td>Machine</td><td>P1</td><td>P2</td><td>P3</td><td>Machine capacity</td></tr><tr><td>M1</td><td>2</td><td>8</td><td>2</td><td>940 Min/day</td></tr><tr><td>M2</td><td>4</td><td>---</td><td>8</td><td>970 Min/day</td></tr><tr><td>M3</td><td>2</td><td>5</td><td>--</td><td>430 Min/day</td></tr></table>

Profit of product P1,P2,P3 are RS 4, Rs 8, Rs 6 Write a linear programming model to the given problem

## Solution:

Let a be the number of Type P1 Product to be produced

Let b be the number of Type P2Product to be produced

Let c be the number of Type P3 Product to be produced

\(L _ { \mathrm { m a x } } = 4 a + 8 b + 6 c\) ----Objective Equation

\(2 { \mathsf { a } } + 8 { \mathsf { b } } + 2 { \mathsf { c } } < = 9 4 0 ~ .\) { Machine P1 constrain}

\(4 a + 8 c < = 9 7 0\) { Machine P2 constrain}

2a+5b <=430 { Machine P3 constrain}

\(a > = 0 , \mathrm { ~ b > = 0 ~ } , \mathrm { ~ c > = 0 ~ } \{\) { Non negative Constrain}

Q3) A farmer has 1000 acres of land on which he grown corn,wheat, and soyabeans. Each acre of corn cost Rs. 100 for preparation, requires 7 man days of work and yields a profit of Rs 30. An acre of wheat costs Rs 120 to prepare, requires 10 man day of work and yields profit of Rs.40, An acre of soyabean costs Rs 70 to prepare requires 8 man days of work and yields of profit Rs.20, If the farmer has Rs. 100000 for preparation and can count on 8000 man days work, formulate the L.P model to allocate the number of acres to each crop to maximize the total profit

## Solution:

Let \(\mathsf { X } _ { 1 }\) be the land to be used to cultivating Corn

Let X2 be the land to be used to cultivating Wheat

Let X3 be the land to be used to cultivating Soyabean

\(\mathrm { \Delta } Z _ { \mathrm { m a x } } = 3 0 \Upsilon _ { 1 ^ { + } } 4 0 \Upsilon _ { 2 ^ { + } } 2 0 \Upsilon _ { 3 }\) ----Objective Equation

<table><tr><td></td><td>Preparation cost</td><td>Labour</td></tr><tr><td>Corn</td><td>100 RS. per Acre</td><td>7 Man days per Acre</td></tr><tr><td>Wheat</td><td>120 Rs. per Acre</td><td>10 Man days per Acre</td></tr><tr><td>Soyabean</td><td>70 RS. per Acre</td><td>80 Man days per Acre</td></tr></table>

Availability

100000 RS

8000 Mans Available

Acres available: 1000

100X1+ 120X2+70X3 <= 100000 { Preparation cost constrain}

\(7 X _ { 1 } + 1 0 X _ { 2 } + 8 X _ { 3 } < = 8 0 0 0\) {Labour constrain}

\(\mathsf { X } _ { 1 } + \mathsf { X } _ { 2 } + \mathsf { X } _ { 3 } < = 1 0 0 0 \ \{ \mathsf { A c r e s \ c o n s t r a i n } \}\)

\(\scriptstyle \mathsf { X } _ { 1 } > = 0 , \mathsf { X } _ { 2 } > = 0 , \mathsf { X } _ { 3 } > = 0\) { Non negative Constrain}

# Linear Programming

Q1) A firm can produce 3 types of cloth A,B,C. 3 kinds of wool required for it, Red wool,green wool, and blue wool.

One unith length of type A cloth needs 2 yards of red Wool and 3 yards of blue wool.one unit of length of type B cloth need 3 yard of red wool, 2 yards of green wool and 2 yards of blue wool. One unit of type c cloth needs 5 yards of green wool and 4 yards of blue wool. The firm has a stock of only 8 yards of red wool, 10 yads of green wool,and 15 yards of blue wool. It is assumed that the income obtained from one unit length of type A cloth is Rs 3, of type B cloth is Rs.5, of type C cloth is Rs. 4. Formulate the problem as a linear programming problem

## Solution:

Let \(\mathsf { X } _ { 1 }\) be the number of Type A cloth to be produced

Let X2 be the number of Type B cloth to be produced

Let X3 be the number of Type C cloth to be produced

\(Z _ { \operatorname* { m a x } { } } = 3 X _ { 1 } + 5 X _ { 2 } + 4 X _ { 3 }\) ----Objective Equation

<table><tr><td></td><td>Red</td><td>Green</td><td>Blue</td></tr><tr><td>Type A</td><td>2 Yard</td><td>----</td><td>3 Yard</td></tr><tr><td>Type B</td><td>3 Yard</td><td>2 Yard</td><td>2 Yard</td></tr><tr><td>Type C</td><td>----</td><td>5 Yard</td><td>4 Yard</td></tr></table>

Availability

8 Yard

10 Yard

15 Yard

\[
2 X _ {1} + 3 X _ {2} <   = 8 \{\text {R e d W o o l C o n s t r a i n} \}
\]

\[
2 X _ {1} + 5 X _ {3} <   = 1 0 \{G r e e n W o o l C o n s t r i n \}
\]

\[
3 X _ {1} + 2 X _ {2} + 4 X _ {3} <   = 1 5 \{\text {B l u e W o o l C o n s t r a i n} \}
\]

\[
X _ {1} > = 0, X _ {2} > = 0, X _ {3} > = 0 \left\{\text {N o n n e g a t i v e C o n s t r a i n} \right\}
\]

Q2) A firm Produce 3 Products,these products are processed in 3 different machine. The time required to manufacture one unit of each product and the daily capacity of machine 3 machine given below

<table><tr><td>Machine</td><td>P1</td><td>P2</td><td>P3</td><td>Machine capacity</td></tr><tr><td>M1</td><td>2</td><td>8</td><td>2</td><td>940 Min/day</td></tr><tr><td>M2</td><td>4</td><td>---</td><td>8</td><td>970 Min/day</td></tr><tr><td>M3</td><td>2</td><td>5</td><td>--</td><td>430 Min/day</td></tr></table>

Profit of product P1,P2,P3 are RS 4, Rs 8, Rs 6 Write a linear programming model to the given problem

## Solution:

Let a be the number of Type P1 Product to be produced

Let b be the number of Type P2Product to be produced

Let c be the number of Type P3 Product to be produced

\(L _ { \mathrm { m a x } } = 4 a + 8 b + 6 c\) ----Objective Equation

\(2 { \mathsf { a } } + 8 { \mathsf { b } } + 2 { \mathsf { c } } < = 9 4 0 ~ .\) { Machine P1 constrain}

\(4 a + 8 c < = 9 7 0\) { Machine P2 constrain}

2a+5b <=430 { Machine P3 constrain}

\(a > = 0 , \mathrm { ~ b > = 0 ~ } , \mathrm { ~ c > = 0 ~ } \{\) { Non negative Constrain}

Q3) A farmer has 1000 acres of land on which he grown corn,wheat, and soyabeans. Each acre of corn cost Rs. 100 for preparation, requires 7 man days of work and yields a profit of Rs 30. An acre of wheat costs Rs 120 to prepare, requires 10 man day of work and yields profit of Rs.40, An acre of soyabean costs Rs 70 to prepare requires 8 man days of work and yields of profit Rs.20, If the farmer has Rs. 100000 for preparation and can count on 8000 man days work, formulate the L.P model to allocate the number of acres to each crop to maximize the total profit

## Solution:

Let \(\mathsf { X } _ { 1 }\) be the land to be used to cultivating Corn

Let X2 be the land to be used to cultivating Wheat

Let X3 be the land to be used to cultivating Soyabean

\(\mathrm { \Delta } Z _ { \mathrm { m a x } } = 3 0 \Upsilon _ { 1 ^ { + } } 4 0 \Upsilon _ { 2 ^ { + } } 2 0 \Upsilon _ { 3 }\) ----Objective Equation

<table><tr><td></td><td>Preparation cost</td><td>Labour</td></tr><tr><td>Corn</td><td>100 RS. per Acre</td><td>7 Man days per Acre</td></tr><tr><td>Wheat</td><td>120 Rs. per Acre</td><td>10 Man days per Acre</td></tr><tr><td>Soyabean</td><td>70 RS. per Acre</td><td>80 Man days per Acre</td></tr></table>

Availability

100000 RS

8000 Mans Available

Acres available: 1000

100X1+ 120X2+70X3 <= 100000 { Preparation cost constrain}

\(7 X _ { 1 } + 1 0 X _ { 2 } + 8 X _ { 3 } < = 8 0 0 0\) {Labour constrain}

\(\mathsf { X } _ { 1 } + \mathsf { X } _ { 2 } + \mathsf { X } _ { 3 } < = 1 0 0 0 \ \{ \mathsf { A c r e s \ c o n s t r a i n } \}\)

\(\scriptstyle \mathsf { X } _ { 1 } > = 0 , \mathsf { X } _ { 2 } > = 0 , \mathsf { X } _ { 3 } > = 0\) { Non negative Constrain}

# LinearProgramming

1) A computer manufacturing company purchases components parts and make 2models of moniters A and B. The components are assembled by the company to produce model A and B. Model A requires 28 hours of labour to assemble from component part, while model B requires 42 hours. After assembly each monitor is tested in inspection department. Model A requires 12 hours of inspection time while B requires 6 hours. The company employs 400 peoples in the assembly department, each working 7 hours a day, 6 days a week. 100 peoples are presently employed in the inspection department, each working 8 hours a day, 6 days a week. Currently wages rate are Rs. 50 per hour in assembly and Rs.75 per hour in inspection. Model A cost 1850 and Model B cost Rs.3250 to produce. Currently two models sell for Rs. 6400 and Rs. 8300. The supplier of these chip can provide no more than 660 in any one working week

<table><tr><td>Solution:</td><td>Monitor A</td><td>Monitor B</td></tr><tr><td>Component Cost</td><td>1850</td><td>3250</td></tr><tr><td>Assemble Cost</td><td>1400</td><td>2100</td></tr><tr><td>Inspection Cost</td><td>900</td><td>450</td></tr><tr><td>Cost Price</td><td>4150</td><td>5800</td></tr><tr><td>Selling price</td><td>6400</td><td>8300</td></tr><tr><td>Profit</td><td>6400-4150= 2250</td><td>8300-5800=2500</td></tr></table>

Let X be the number of type A to be produced,

Let Y be the number of type B to be produced

\({ \cal Z } _ { \mathrm { m a x } } = 2 2 5 0 \times \mathrm { ~ + ~ } 2 5 0 0 \forall\) [Objective equation]

Assemble for per monitor A type requires 28 hour labour, 1 hour labour cost for assemble \(= 5 0\) for 28 hours \(= 2 8 ^ { \star } ~ 5 0 = 1 4 0 0\)

Type B requires 42 hour labour for assemble

For 42 hours \(= 4 2 ^ { \star } 5 0 = 2 1 0 0\)

Inspection cost per hou \(= 7 5\)

Type A— \(1 2 = 1 2 ^ { \star } 7 5 = 9 0 0\)

Type B---- \(6 { = } 6 ^ { \star } 7 5 \mathrm { = }\) 450

<table><tr><td></td><td>Monitor A</td><td>Monitor B</td><td>Employees</td><td>working</td><td>total day</td><td>Total hour</td></tr><tr><td>Assemble</td><td>28 hours</td><td>42hours</td><td>400</td><td>7 hour/day</td><td>6</td><td>400*7*6= 16800</td></tr><tr><td>Inspection</td><td>12 hours</td><td>6 hours</td><td>100</td><td>8 hour/day</td><td>8</td><td>100*8*6= 4800</td></tr></table>

One Monitor Type A require 28 hour for assemble, So X monitor requires \(x ^ { \star } 2 8 = 2 8 x\)

One Monitor Type B require 42 hour for assemble, So Y monitor requires \(\forall ^ { \star } 4 2 = 4 2 \) Y

Available hour in assemble department \(= 1 6 8 0 0\) 28 X +42Y <=16800 [ Assemble constrain]

Similarly

One Monitor Type A require 12 hour for inspection, So X monitor requires \(\bigstar \bigstar 1 2 = 1 2 \bigstar\)

One Monitor Type B require 6 hour for assemble, So Y monitor requires \(\Upsilon ^ { \star } 6 { = } 6\) Y

Available hour in assemble department \(= 4 8 0 0\) \(1 2 x + 6 y < = 4 8 0 0 1\) [ Inspection dept. hour constrain]

## Chip available 660

Assume that 1 monitor require 1 chip of any type X number of Type A require X number of chip, Y number of type B requires Y number of chip

\(x + y < = 6 6 0\) [Chip Constarin] \(\scriptstyle x > = 0 , Y > = 0\) [Non negative Constrain]

2) A confectionery company mixes 3 types of toffees ingredients to form one kg of toffee packs. The pack is sold at Rs. 170, The 3 types of toffees ingredients cost Rs.200, Rs.100 and Rs.50 per kg. The mixture must contain at least 0.3kg of the first type of toffees and the weight of first first two types of toffees almost be equal to the weight of third type. Determine the optimal mix for maximum profit

Solution : Let X, Y,Z be the number of KG ingredients of 3 types is mixed to prepare 1 KG toffees

\[
Z _ {\max } = 1 7 0 - 2 0 0 ^ {*} X - 1 0 0 ^ {*} Y - 5 0 ^ {*} Z [ \text {O b j e c t i v e} ]
\]

\(\mathtt { X } \mathtt { > } = 0 . 3 0\) [ First type ingredients constrain]

\(x + y < = 2\) [type1 and 2 almost equal to third type]

\(x + y + z = 7\) [ To add all that to form only 1 kg, not exceed or less than 1]

\[
X > = 0, Y > = 0, Z > = 0
\]

# Simplex Method

Q1) \(\mathrm { Z } _ { \mathrm { M a x } } { = } 3 \mathrm { X } _ { 1 } { + } 4 \mathrm { X } _ { 2 }\)

\[
\mathrm {X} _ {1} + \mathrm {X} _ {2} <   = 4
\]

\[
\mathrm {X} _ {1} - \mathrm {X} _ {2} <   = 2
\]

Solution: Zmax-3X1-4X2=0

\[
\mathrm {X} _ {1} + \mathrm {X} _ {2} + \mathrm {S} _ {1} = 4
\]

\[
\mathrm {X} _ {1} - \mathrm {X} _ {2} + \mathrm {S} _ {2} = 2
\]

Basic Variable: Unique, Unit, Positive Co-efficient : S1, S2, ZMax

<table><tr><td>Basic variable</td><td>X1</td><td>X2</td><td>S1</td><td>S2</td><td>ZMax</td><td>RHS</td><td>Ratio= RHS/PC</td></tr><tr><td>S1</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>4</td><td>4/1=4</td></tr><tr><td>S2</td><td>1</td><td>-1</td><td>0</td><td>1</td><td>0</td><td>2</td><td>2/−1=−2</td></tr><tr><td>ZMax</td><td>-3</td><td>-4</td><td>0</td><td>0</td><td>1</td><td>0</td><td></td></tr></table>

Pivoting Column [ P C] = Entering variable [ E V] = Maximum Negative in \(\mathrm { { Z } _ { M a x } \ \mathrm { X } } _ { 2 } = - 4\)

Pivoting Row \([ \mathrm { P } \mathrm { R } ] =\) Leaving Variable \([ \mathrm { L V } ] =\) Minimum Positive Ratio \(= 4\)

Pivoting Element \(=\) Intersecting of Row and Column= 1

New Pivoting \(\begin{array} { r } { \mathrm { R o w } { } = \mathrm { X } _ { 2 } = \frac { 1 } { \mathrm { P E } } * \mathrm { O } { } | \mathrm { d } \mathrm { R o w } { } } \end{array}\)

\[
\mathrm {X} _ {2} = \frac {1}{1} * [ 1, 1, 1, 0, 0, 4 ]
\]

\[
\mathrm {X} _ {2} = [ 1, 1, 1, 0, 0, 4 ]
\]

Key Element for \({ \bf S } _ { 2 } = - 1\)

\[
\begin{array}{l} = - (- 1) [ 1, 1, 1, 0, 0, 4 ] + [ 1, - 1, 0, 1, 0, 2 ] \\ = 1 \quad [ 1, 1, 1, 0, 0, 4 ] + [ 1, - 1, 0, 1, 0, 2 ] \\ = \left[ 1, 1, 1, 0, 0, 4 \right] + \left[ 1, - 1, 0, 1, 0, 2 \right] \\ = \left[ 1 + 1, 1 - 1, 1 + 0, 0 + 1, 0 + 0, 4 + 2 \right] \\ = \left[ \begin{array}{c c c c c c c} 2 & 0 & 1 & 1 & 0 & 6 \end{array} \right] \\ \end{array}
\]

# Simplex Method

Key Element for \(\mathrm { Z _ { M a x } } = - 4\)

\[
\begin{array}{l} Z _ {\text {M a x}} = \quad - \text {K e y} * \text {N P R} + \text {O l d r o w} \\ = - (- 4) \left[ 1, 1, 1, 0, 0, 4 \right] + \left[ - 3, - 4, 0, 0, 1, 0 \right] \\ = 4 \quad [ 1, 1, 1, 0, 0, 4 ] + [ - 3, - 4, 0, 0, 1, 0 ] \\ = \left[ 4, 4, 4, 0, 0, 1 6 \right] + \left[ - 3, - 4, 0, 0, 1, 0 \right] \\ = \left[ 4 - 3, 4 - 4, 4 + 0, 0 + 0, 0 + 1, 1 6 + 0 \right] \\ = \left[ \begin{array}{c c c c c c} 1 & 0 & 4 & 0 & 1 & 1 6 \end{array} \right] \\ \end{array}
\]

<table><tr><td>Basic variable</td><td>X1</td><td>X2</td><td>S1</td><td>S2</td><td>ZMax</td><td>RHS</td><td>Ratio= RHS/PC</td></tr><tr><td>X2</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>4</td><td></td></tr><tr><td>S2</td><td>2</td><td>0</td><td>1</td><td>1</td><td>0</td><td>6</td><td></td></tr><tr><td>ZMax</td><td>1</td><td>0</td><td>4</td><td>0</td><td>1</td><td>16</td><td></td></tr></table>

Stop the Process because there is no negative in \({ \cal Z } _ { \mathrm { m a x } }\) row.

\[
1 \mathrm {X} _ {2} = 4 \quad 1 \mathrm {Z} _ {\text {M a x}} = 1 6
\]

\[
\mathrm {X} _ {2} = 4 \quad | \quad \mathrm {Z} _ {\text {M a x}} = 1 6
\]

There is no \(\mathrm { X } _ { 1 }\) is present in Basic Variable Column So \(\mathrm { X } _ { 1 } { = } 0\)

## Verification:

\[
\mathrm {X} _ {1} + \mathrm {X} _ {2} <   = 4
\]

\[
\mathrm {X} _ {1} - \mathrm {X} _ {2} <   = 2
\]

\[
Z _ {\text {M a x}} = 3 X _ {1} + 4 X _ {2}
\]

\[
0 + 4 <   = 4
\]

\[
0 - 4 <   = 2
\]

\[
= 3 (0) + 4 (4)
\]

\[
4 <   = 4
\]

\[
- 4 <   = 2
\]

\[
= 0 + 1 6
\]

\[
Z _ {\text {M a x}} = 1 6
\]

# Simplex Method

\[
\begin{array}{l} 3 \mathrm {X} _ {1} - \mathrm {X} _ {2} + 3 \mathrm {X} _ {3} <   = 7 \\ 4 \mathrm {X} _ {1} + 3 \mathrm {X} _ {2} + 8 \mathrm {X} _ {3} <   = 1 0 \\ - 2 \mathrm {X} _ {1} + 4 \mathrm {X} _ {2} <   = 1 2 \\ \end{array}
\]

Solution : 3X1- X2 +3X3 +S1 = 7

\[
\begin{array}{l} 4 \mathrm {X} _ {1} + 3 \mathrm {X} _ {2} + 8 \mathrm {X} _ {3} + \mathrm {S} _ {2} = 1 0 \\ - 2 \mathrm {X} _ {1} + 4 \mathrm {X} _ {2} + \mathrm {S} _ {3} = 1 2 \\ \end{array}
\]

Convert \(Z _ { \mathrm { m i n } }\) to \(Z _ { \mathrm { m a x } }\)

I.e. \(Z _ { \operatorname* { m a x } } = - ~ \mathrm { Z _ { \operatorname* { m i n } } }\)

\[
Z _ {\max} = - \left[ X _ {1} - 3 X _ {2} + 2 X _ {3} \right]
\]

\[
Z _ {\max } = - X _ {1} + 3 x _ {2} - 2 X _ {3}
\]

\[
Z _ {\max } + X _ {1} - 3 X _ {2} + 2 X _ {3} = 0
\]

I. B.F.S.

Let \(\mathbf { X } _ { 1 } = 0 , \mathbf { X } _ { 2 } = 0 , \mathbf { X } _ { 3 } = 0\) \(\mathrm { { X } } _ { 1 } = 0\) \({ \bf X } _ { 2 } = 0\) \({ \bf X } _ { 3 } = 0\) , then \(\mathbf { S } _ { 1 } = 7\) , S2 = 10, S3 = 12

Basic variable :Unique, Unit, \(+ ^ { \mathrm { v e } }\) Co-effcient

<table><tr><td>B.V</td><td>X1</td><td>X2</td><td>X3</td><td>S1</td><td>S2</td><td>S3</td><td></td><td>Zmax</td><td>RHS</td><td>Ratio=RHS/P.C</td></tr><tr><td>S1</td><td>3</td><td>-1</td><td>3</td><td>1</td><td>0</td><td>0</td><td></td><td>0</td><td>7</td><td>7/-1=-7</td></tr><tr><td>S2</td><td>4</td><td>3</td><td>8</td><td>0</td><td>1</td><td>0</td><td></td><td>0</td><td>10</td><td>10/3</td></tr><tr><td>S3</td><td>-2</td><td>4</td><td>0</td><td>0</td><td>0</td><td>1</td><td></td><td>0</td><td>12</td><td>3</td></tr><tr><td>Zmax</td><td>1</td><td>-3</td><td>2</td><td>0</td><td>0</td><td>0</td><td></td><td>1</td><td>0</td><td></td></tr></table>

# Simplex Method

Pivoting Element [P.E] \(=\) Intersting of row and column = 4

\[
\begin{array}{l} = \frac {1}{4} \left[ - 2, 4, 0, 0, 0, 1, 0, 1 2 \right] \\ = \left[ - \frac {1}{2}, 1, 0, 0, 0, \frac {1}{4}, 0, 3 \right] \\ \end{array}
\]

Key element for \(\mathbf { S } _ { 1 } = \mathbf { - } 1\)

\[
\begin{array}{l} = - (- 1) \left(\frac {- 1}{2}, 1, 0, 0, 0, \frac {1}{4}, 0, 3\right) + \left(3, - 1, 3, 1, 0, 0, 0, 7\right) \\ = \quad 1 \left[ \frac {- 1}{2}, 1, 0, 0, 0, \frac {1}{4}, 0, 3 \right] + \left[ 3, - 1, 3, 1, 0, 0, 0, 7 \right] \\ = \left[ - \frac {1}{2}, 1, 0, 0, 0, \frac {1}{4}, 0, 3 \right] + \left(3, - 1, 3, 1, 0, 0, 0, 7 \right] \\ = \left[ - \frac {1}{2} + 3, 1 - 1, 0 + 3, 0 + 1, 0 + 0, \frac {1}{4} + 0, 0 + 0, 3 + 7 \right] \\ = \left[ \begin{array}{l l l l l l l l} \frac {5}{2}, & 0 & 3 & 1 & 0 & \frac {1}{4} & 0 & 1 0 \end{array} \right] \\ \end{array}
\]

Key element for \(\mathbf { S } _ { 2 } = 3\)

\[
\begin{array}{l} = - 3 \left[ - \frac {1}{2}, 1, 0, 0, 0, \frac {1}{4} 0, 3 \right] + \left[ 4, 3, 8, 0, 1, 0, 0, 1 0 \right] \\ = \left[ \frac {3}{2}, - 3, 0, 0, 0, - \frac {3}{4}, 0, - 9, \right] + \left(4, 3, 8, 0, 1, 0, 0, 1 0 \right\rbrack \\ \end{array}
\]