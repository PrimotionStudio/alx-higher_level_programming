-- 14-my_genres.sql
SELECT `tv_genres`.`name` AS `name`
FROM `tv_genres`
JOIN `tv_show_genres`, `tv_shows`
ON `tv_shows`.`title` = 'Dexter'
WHERE `tv_show_genres`.`genre_id` = `tv_genres`.`id` AND `tv_show_genres`.`show_id` = `tv_shows.id`
ORDER BY `tv_genre`.`name` ASC;
