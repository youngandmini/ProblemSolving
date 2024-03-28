-- 코드를 입력하세요
select FH.FLAVOR
from FIRST_HALF as FH
join
    (SELECT FLAVOR, sum(TOTAL_ORDER) as SUM_OF_ORDER
    from JULY
    group by FLAVOR) as J
on FH.FLAVOR = J.FLAVOR
order by (FH.TOTAL_ORDER + J.SUM_OF_ORDER) desc
limit 3