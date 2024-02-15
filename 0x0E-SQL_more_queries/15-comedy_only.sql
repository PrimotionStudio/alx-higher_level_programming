-- 15-comedy_only.sql
SELECT `tv_shows`.`title` AS `title`
FROM `tv_shows`
JOIN `tv_show_genres`
ON `tv_shows`.`id` = `tv_show_genres`.`show_id`
JOIN `t_genres`
ON `tv_genres`.`id` = `tv_show_genres`.`genre_id`
WHERE `tv_genres`.`name` = 'Comedy'
ORDER BY `tv_show`.`title`;
