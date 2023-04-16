SELECT * FROM public.Exercises
Where 'triceps' = ANY(primary_muscles)
AND equipment = 'body only'

OR 'triceps' = ANY(secondary_muscles)
AND equipment = 'body only'

AND category = 'strength'

ORDER BY primary_muscles ASC