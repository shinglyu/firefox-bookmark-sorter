SELECT * FROM moz_places WHERE last_visit_date > strftime('%s000000', 'now', '-3 month') ORDER BY frecency DESC limit 200;

