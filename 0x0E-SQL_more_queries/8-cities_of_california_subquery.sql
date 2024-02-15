-- 8-cities_of_california_subquery.sql
SELECT * FROM `cities` WHERE `state_id` IN (
	SELECT `id`
	FROM `states`
	WHERE `name`='California')
ORDER BY `id` ASC;
