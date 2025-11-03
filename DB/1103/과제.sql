SELECT * FROM tracks WHERE "Name" LIKE '%love%'

SELECT * 
FROM tracks 
WHERE "GenreId"=1 and "Milliseconds">=300000
ORDER BY "UnitPrice" DESC;

SELECT "GenreId", count(*) as 'TotalTracks'
FROM tracks 
GROUP BY "GenreId";

SELECT "GenreId", SUM(UnitPrice) as 'TotalPrice'
FROM tracks 
GROUP BY "GenreId"
HAVING SUM(UnitPrice)>=100;
