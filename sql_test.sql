WITH dependency_levels AS (

    -- initial node
    SELECT 
        d.UNIT_NBR,
        d.STEP_SEQ_ID,
        1 AS exec_level
    FROM DEPENDENCY_RULES d
    WHERE d.STEP_DEP_ID = 0

    UNION ALL

    -- Dependency checks
    SELECT 
        d.UNIT_NBR,
        d.STEP_SEQ_ID,
        MAX(dl.exec_level) + 1 AS exec_level
    FROM DEPENDENCY_RULES d
    JOIN dependency_levels dl
        ON d.STEP_DEP_ID = dl.STEP_SEQ_ID
        AND d.UNIT_NBR = dl.UNIT_NBR
    GROUP BY d.UNIT_NBR, d.STEP_SEQ_ID
),

-- Take max level 
final_levels AS (
    SELECT 
        UNIT_NBR,
        STEP_SEQ_ID,
        MAX(exec_level) AS exec_level
    FROM dependency_levels
    GROUP BY UNIT_NBR, STEP_SEQ_ID
)

-- Final
SELECT 
    f.UNIT_NBR,
    f.exec_level,
    p.STEP_SEQ_ID,
    p.STEP_PROG_NAME
FROM final_levels f
JOIN PROG_NAME p
    ON f.UNIT_NBR = p.UNIT_NBR
    AND f.STEP_SEQ_ID = p.STEP_SEQ_ID
ORDER BY f.UNIT_NBR, f.exec_level, p.STEP_SEQ_ID;
