-- 01. Querying data
SELECT LastName From employees;
SELECT 
    LastName, FirstName
From 
    employees;
SELECT * From employees;
SELECT FirstName AS '이름' From employees;

SELECT Name, Milliseconds/60000 AS '재생시간(분)' FROM tracks;

-- 02. Sorting data
SELECT FirstName FROM employees ORDER BY FirstName;
SELECT FirstName FROM employees ORDER BY FirstName DESC;
SELECT Country, City FROM customers ORDER BY Country DESC, City;
SELECT 
    Name, Milliseconds/60000 AS '재생시간(분)' 
FROM 
    tracks 
ORDER BY 
    Milliseconds DESC;


-- NULL 정렬 예시

-- 03. Filtering data
# DISTINCT
SELECT DISTINCT Country FROM customers ORDER BY Country;

# WHERE
SELECT "LastName", "FirstName", "City" FROM customers WHERE "City"='Prague';
    -- ""로 컬럼명 표현 가능
SELECT "LastName", "FirstName", "City" FROM customers WHERE "City"!='Prague';
SELECT 
    "LastName", "FirstName", "Company", "Country" 
FROM 
    customers 
WHERE 
    "Company" ISNULL
    AND "Country"='USA';    -- OR도 사용함

SELECT Name, Bytes FROM tracks WHERE "Bytes" BETWEEN 100000 and 500000;
SELECT 
    Name, Bytes 
FROM 
    tracks 
WHERE 
    "Bytes" BETWEEN 100000 and 500000
ORDER BY
    bytes;

SELECT 
    "LastName", "FirstName", "Country" 
FROM 
    customers 
WHERE 
    "Country" IN ('Canada', 'Germany', 'France');   -- NOT IN 이면 포함안함

SELECT 
    "LastName", "FirstName" 
FROM 
    customers 
WHERE 
    "LastName" LIKE '%son';

SELECT 
    "LastName", "FirstName"
FROM 
    customers 
WHERE 
    "FirstName" LIKE '___a';

# LIMIT
    # Bytes 기준 4번째부터 7번째 데이터만 조회
SELECT
    TrackId, Name, Bytes
FROM
    tracks
ORDER BY
    "Bytes" DESC
LIMIT
    3, 4;

-- 04. Grouping data
# GROUP BY
SELECT
    Country, 
    COUNT(*)
FROM
    customers
GROUP BY
    "Country";
