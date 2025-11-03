SELECT * FROM users WHERE age > 30 and balance >= 1000;

SELECT * FROM users WHERE balance <= 1000 and age <= 20;

SELECT 
    * 
FROM 
    users 
WHERE 
    first_name LIKE '현%' and country = '제주특별자치도' 
ORDER BY 
    age DESC LIMIT 1;

SELECT 
    * 
FROM 
    users 
WHERE 
    last_name = '박' and age >= 25 
ORDER BY 
    age LIMIT 1;

SELECT 
    * 
FROM 
    users 
WHERE 
    first_name in ('재은', '영일')
ORDER BY 
    balance DESC LIMIT 1;

SELECT 
    *, max(balance)
FROM 
    users
GROUP BY
    country 
ORDER BY 
    balance DESC;

SELECT
    *
FROM
    users
WHERE
    age >= 30 AND
    balance > (SELECT avg(balance) FROM users WHERE age >= 30);
