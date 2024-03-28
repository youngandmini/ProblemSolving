-- 코드를 작성해주세요

select distinct d.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
from SKILLCODES s
join DEVELOPERS d
on (s.CODE & d.SKILL_CODE)
where s.CATEGORY = 'Front End'
order by d.ID