-- 14-my_genres.sql
SELECT `tv_shows`.`name` AS `name`
FROM `tv_shows`
JOIN `tv_show_genres`, `tv_genres`
ON `tv_genre` = 'Dexter'
WHERE `tv_show_genres`.`genre_id` = `tv_genres`.`id` AND `tv_show_genres`.`show_id` = `tv_shows.id`
ORDER BY `tv_genre`.`name` ASC;
