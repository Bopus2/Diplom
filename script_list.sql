-- TASK 1 --
SELECT courierList.login,
     Count(*) AS orderListCountInDelivery
FROM "Couriers" AS courierList
  JOIN "Orders" AS orderList
      ON courierList.id = orderList."courierId"
WHERE orderList."inDelivery" = true
GROUP BY courierList.login;



-- TASK 2 --
SELECT orderList.track,
       (CASE
            WHEN orderList.finished = true THEN
                2
            WHEN orderList.cancelled = true THEN
                -1
            WHEN orderList."inDelivery" = true THEN
                1
            ELSE
                0
        END
       ) AS status
FROM "Orders" AS orderList;
