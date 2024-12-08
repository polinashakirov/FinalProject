SELECT c.login, COUNT(*)
FROM "Couriers" c
         JOIN "Orders" o ON o."courierId" = c."id"
WHERE o."inDelivery" = TRUE
GROUP BY c."id";