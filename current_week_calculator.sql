CREATE OR REPLACE FUNCTION current_week_calculator() 
RETURNS TABLE (
    begin_date timestamp,
    end_date timestamp
) AS $$
BEGIN
    RETURN QUERY SELECT
        CASE EXTRACT(ISODOW FROM CURRENT_DATE)
            WHEN 1 THEN 
                CURRENT_DATE - INTERVAL '2 days'
            WHEN 2 THEN 
                CURRENT_DATE - INTERVAL '3 days'
            WHEN 3 THEN 
                CURRENT_DATE - INTERVAL '4 days'
            WHEN 4 THEN 
                CURRENT_DATE - INTERVAL '5 days'
            WHEN 5 THEN 
                CURRENT_DATE - INTERVAL '6 days'
            WHEN 6 THEN 
                CURRENT_DATE - INTERVAL '0 days'
            WHEN 7 THEN 
                CURRENT_DATE - INTERVAL '1 days'
        END AS begin_date,
        CASE EXTRACT(ISODOW FROM CURRENT_DATE)
            WHEN 1 THEN 
                CURRENT_DATE + INTERVAL '4 days'
            WHEN 2 THEN 
                CURRENT_DATE + INTERVAL '3 days'
            WHEN 3 THEN 
                CURRENT_DATE + INTERVAL '2 days'
            WHEN 4 THEN 
                CURRENT_DATE + INTERVAL '1 days'
            WHEN 5 THEN 
                CURRENT_DATE + INTERVAL '0 days'
            WHEN 6 THEN 
                CURRENT_DATE + INTERVAL '6 days'
            WHEN 7 THEN 
                CURRENT_DATE + INTERVAL '5 days'
        END + INTERVAL '23 hours 59 minutes 59 seconds'::interval AS end_date;
END;
$$ LANGUAGE plpgsql;