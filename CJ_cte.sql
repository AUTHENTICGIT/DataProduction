SELECT
	count( * ) AS _count
FROM
	(
		WITH RECURSIVE XLY_TEMP_TABLE AS (
		  SELECT DISTINCT * FROM ( SELECT * FROM `M_ypzxw_m_userinfo_1_18` ) AS TABLE_VIEW
		),
		COL_CTE ( `id`, `pid`, `xlyShowName`, `xlyLevel` ) AS (
      SELECT
        `id`,
        `pid`,
        `id`,
        1 AS `xlyLevel`
      FROM
        XLY_TEMP_TABLE
      WHERE
        CONCAT( `pid` ) = '0' AND CONCAT( `id` ) != CONCAT( `pid` )

      UNION ALL

      SELECT
        TEMP_CTE_TABLE.`id`,
        TEMP_CTE_TABLE.`pid`,
        TEMP_CTE_TABLE.`id`,
        TEMP_CTE_TABLE2.`xlyLevel` + 1 AS `xlyLevel`
      FROM
        XLY_TEMP_TABLE AS TEMP_CTE_TABLE
        INNER JOIN COL_CTE AS TEMP_CTE_TABLE2 ON CONCAT( TEMP_CTE_TABLE.`pid` ) = CONCAT( TEMP_CTE_TABLE2.`id` )
        AND CONCAT( TEMP_CTE_TABLE.`pid` ) != CONCAT( TEMP_CTE_TABLE2.`pid` ) -- 防止子节点再指向父节点的情况

        AND CONCAT( TEMP_CTE_TABLE2.`id` ) IS NOT NULL
        AND LENGTH( trim( TEMP_CTE_TABLE2.`id` ) ) > 0 -- 防止子节点为空的情况

		)
		SELECT DISTINCT *
	  FROM COL_CTE
	) AS A