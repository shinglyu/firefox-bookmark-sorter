SELECT place_id, title, url, count(place_id), visit_date FROM moz_historyvisits as H, moz_places as P WHERE H.place_id == P.id GROUP BY place_id ORDER BY count(place_id) DESC limit 100;


