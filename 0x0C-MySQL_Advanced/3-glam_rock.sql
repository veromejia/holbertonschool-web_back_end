-- Select the bands table from the holberton database
-- lists all bands with Glam rock as their main style, ranked by their longevity
SELECT
    band_name,
    ABS(formed - IFNULL(split, 2020)) lifespan
FROM
    metal_bands
WHERE
    FIND_IN_SET('Glam rock', style)
ORDER BY
    lifespan DESC
