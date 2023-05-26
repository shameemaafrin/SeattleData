select * from trees2;
select FUNDING_SOURCE, count(*) from trees2 group by FUNDING_SOURCE order by count(*) desc;
select TOTAL_COUNT,COMMON_NAME from trees2 group by TOTAL_COUNT order by TOTAL_COUNT DESC;

select TOTAL_COUNT,BOTANICAL_NAME from trees2 group by TOTAL_COUNT order by TOTAL_COUNT DESC;

select avg(DIAM) from trees2;
