--LR: https://www.cnblogs.com/yanggb/p/11165276.html
SELECT
	count( * ) AS _count
FROM
	( --LR: 定义了两个CTE
		WITH RECURSIVE XLY_TEMP_TABLE AS (
		  SELECT DISTINCT * FROM ( SELECT * FROM `M_ypzxw_m_userinfo_1_18` ) AS TABLE_VIEW
		),  --LR: 逗号隔开两个CTE：CTE后面跟其他CTE，但只能使用一个WITH，多个CTE用逗号隔开
		COL_CTE ( `id`, `pid`, `xlyShowName`, `xlyLevel` ) AS (
      SELECT
        `id`,
        `pid`,
        `id`,
        1 AS `xlyLevel`
      FROM
        XLY_TEMP_TABLE  --LR: CTE可以引用自身，也可以引用同一个WITH子句中预先定义的CTE，但不允许向前引用（定义钱引用）
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