CREATE TABLE IF NOT EXISTS Meals (
    MealId SERIAL PRIMARY KEY
    ,MealName TEXT NOT NULL
    ,MealPrice DECIMAL NOT NULL
);

INSERT INTO Meals(MealName, MealPrice) VALUES ('Mushroom Burger', 10.00);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Crispy Fried Chicken', 11.00);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Fish & Chips', 10.00);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Spaghetti & Meatballs', 12.00);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Hotdog Sandwish', 10.00);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Macaroni Soup', 3.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Tex Mex Chill', 3.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Frensh Fries', 4.50);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Fried Calamari', 9.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Beef Taco', 7.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Water',  2.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Sparking Water', 3.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Soda in A Bottle', 4.50);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Orange Juice', 5.99);
INSERT INTO Meals(MealName, MealPrice) VALUES ('Fresh Lemonade', 7.50);