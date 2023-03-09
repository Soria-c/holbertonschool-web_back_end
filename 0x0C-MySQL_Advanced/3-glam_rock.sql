-- script that lists all bands with Glam rock as their main style, ranked by their longevity

-- query definition
SELECT band_name, (IFNULL(split, YEAR(CURDATE()))-formed) as lifespan
FROM metal_bands
WHERE LOCATE('Glam rock', style)
ORDER BY lifespan DESC
