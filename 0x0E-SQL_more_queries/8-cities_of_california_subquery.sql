-- 8-cities_of_california_subquery.sql
SELECT * FROM `cities`, `states` WHERE `states` IN (
	SELECT `id`
	FROM `states`
	WHERE `name`='California')
ORDER BY `id` ASC;
