SELECT a.id, a.title, a.text
FROM article AS a
LEFT JOIN comment AS c
ON a.id = c.article_id
WHERE c.article_id is null