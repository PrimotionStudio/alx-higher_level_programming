-- _12-no_genre.sql
SELECT `tv_shows`.`title`, `tv_show_genres`.`genre_id`
FROM `tv_shows`
LEFT JOIN `tv_show_genres` ON `tv_shows`.`id` IS NOT `tv_show_genres`.`show_id`
ORDER BY `tv_shows`.`title`, `tv_show_genres`.`genre_id` ASC;
