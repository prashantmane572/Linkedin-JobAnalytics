create database job_analytics;
use job_analytics;

-----------------------------------------------------------------------------
--Q1
--Comparison of number of jobs
--across different cities for 
--different level 
select 
	  city, Level, count(*) as number_of_jobs 
from 
	jobs a join details b 
on 
	a.Details_id = b.Details_id
group by
	    city , Level
order by
	    number_of_jobs desc;
--------------------------------------------------------------------------

--Q2
--Generate some insight with respect to number of jobs
--distribution across various industry.For instance, what is 
--the total number of jobs in Software Industry as compared to Marketing
select 
	   Industry,count(*) as number_of_jobs
from 
	 company a join jobs b 
on 
	a.Company_id = b.Company_id
group by 
	    Industry
order by
		number_of_jobs desc;
----------------------------------------------------------------------------

 --Q3
 --Generate insights into number of opening with respect to the
 --current employee count - Number of opening in a company with more
 --than 1000 employees in comparison to number of openings in a company with 100 employees

select
	   Name ,city,Employee_count,total_applicants 
from
	company a join jobs b 
on 
	a.Company_id =  b.Company_id
		join details c
on 
	b.Details_id = c.Details_id 
where 
	Employee_count>1000 and Total_applicants>100
order by
		 Name, city;
----------------------------------------------------------------------------

--Q4
--Generate any one interesting insight from the data
select * from
			 (select name,Total_applicants,state 
			  from
				  company a join jobs b 
			  on 
				  a.Company_id =  b.Company_id
				 join details c
			  on 
				  b.Details_id = c.Details_id  ) as aa
pivot

	( min(total_applicants)
	for 
		[state] in ([Chandigarh],[Delhi],[Gujrat],[Haryana],[Karnataka]
		,[Kerala],[Madhya Pradesh],[Maharashtra],[Odisha],[Punjab],
	   [Rajasthan],[Tamil Nadu],[Telangana],[Uttar Pradesh],[West Bengal]))
	   as 
		 dd;
----------------------------------------------------------------------------

--Q5
--Count the number of jobs across different industry across different locations.
--For instance, how many Frontend Engineer jobs are there in Bangalore as compared
--to Data Analytics jobs in Bangalore, or how many Data Analytics jobs are there in
--Bangalore as compared to number of Data Scientists job in Gurgaon - this needs to
--be done in SQL but presented in the above created Excel dashboard

with cte as
(
select 
	city, industry, Designation 
from 
	jobs a join company b 
on 
	a.Company_id = b.Company_id
where 
	city in ('Bengaluru', 'Gurgaon')
)
select 
	city, Industry,
count(case when  
			((
			Designation like '%web%' 
			or 
			(
			Designation like '%java%' and Designation not like '%analyst%'
			)))
			then 0 end
			) as [Frontend Engineer],
count(case when 
			Designation like '%analyst%' 
			then 0 end
			) as [Data Analytics],
count(case when
			Designation like '%Data Scientist%' 
			then 0 end
			) as [Data Scientists]
from 
	cte
group by 
	city, Industry;
