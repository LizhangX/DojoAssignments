#1. What query would you run to get the total revenue for March of 2012?

select monthname(billing.charged_datetime) as month, sum(billing.amount) as revenue
from billing
where monthname(billing.charged_datetime) = 'March'
and year(billing.charged_datetime) = '2012';

#2. What query would you run to get total revenue collected from the client with an id of 2?

select sum(billing.amount) as total_revenue, billing.client_id
from billing
where billing.client_id = 2;

#3. What query would you run to get all the sites that client=10 owns?

select sites.client_id, sites.domain_name
from sites
where sites.client_id = 10;

#4. What query would you run to get total # of sites created per month per year for the client 
#with an id of 1? What about for client=20?

select sites.client_id, count(sites.domain_name), monthname(sites.created_datetime), year(sites.created_datetime)
from sites
where sites.client_id = 1
group by monthname(sites.created_datetime), year(sites.created_datetime);

select sites.client_id, count(sites.domain_name), monthname(sites.created_datetime), year(sites.created_datetime)
from sites
where sites.client_id = 20
group by monthname(sites.created_datetime), year(sites.created_datetime);

#5. What query would you run to get the total # of leads generated for each of the sites between 
#January 1, 2011 to February 15, 2011?

select sites.domain_name, count(leads.leads_id) as num_of_leads_generated, date(leads.registered_datetime) as date_generated
from sites
join leads
on sites.site_id = leads.site_id
where leads.registered_datetime > 20110101 and leads.registered_datetime < 20110215
group by leads.site_id;

#6. What query would you run to get a list of client names and the total # of leads we've generated 
#for each of our clients between January 1, 2011 to December 31, 2011?

select clients.first_name, clients.last_name, count(leads.leads_id)
from clients
join sites
on clients.client_id = sites.client_id
join leads
on sites.site_id = leads.site_id 
where leads.registered_datetime > 20110101 and leads.registered_datetime < 20111231
group by clients.first_name;

#7. What query would you run to get a list of client names and the total # of leads we've generated 
#for each client each month between months 1 - 6 of Year 2011?

select clients.first_name, clients.last_name, count(leads.leads_id),monthname(leads.registered_datetime)
from clients
join sites
on clients.client_id = sites.client_id
join leads
on sites.site_id = leads.site_id 
where leads.registered_datetime > 20110101 and leads.registered_datetime < 20110701
group by clients.first_name, monthname(leads.registered_datetime)
order by leads.registered_datetime asc;


#8. What query would you run to get a list of client names and the total # of leads we've generated 
#for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by 
#client id.  Come up with a second query that shows all the clients, the site name(s), and the total 
#number of leads generated from each site for all time.

select concat(clients.first_name, " ", clients.last_name) as client_name,
count(leads.leads_id),
clients.client_id
from clients
join sites
on clients.client_id = sites.client_id
join leads
on sites.site_id = leads.site_id 
where leads.registered_datetime > 20110101 and leads.registered_datetime < 20111231
group by clients.first_name
order by clients.client_id asc;

select concat(clients.first_name, " ", clients.last_name) as client_name,
sites.domain_name as site_name,
count(leads.leads_id),
date_format(leads.registered_datetime, '%M %d, %Y')
from clients
join sites
on clients.client_id = sites.client_id
join leads
on sites.site_id = leads.site_id
where leads.registered_datetime > 20110101 and leads.registered_datetime < 20111231
group by sites.domain_name
order by client_name;

#9. Write a single query that retrieves total revenue collected from each client for each month of 
#the year. Order it by client id.

select clients.client_id,
sum(billing.amount), 
concat(clients.first_name, " ", clients.last_name) as client_name,
monthname(billing.charged_datetime),
year(billing.charged_datetime)
from billing
join clients
on clients.client_id = billing.client_id
group by clients.client_id, monthname(billing.charged_datetime), year(billing.charged_datetime)
order by clients.client_id;

#10. Write a single query that retrieves all the sites that each client owns. Group the results 
#so that each row shows a new client. It will become clearer when you add a new field called 'sites' 
#that has all the sites that the client owns. (HINT: use GROUP_CONCAT)

select concat(clients.first_name, " ", clients.last_name) as client_name,
group_concat('/', sites.domain_name) as sites
from clients
left join sites
on clients.client_id = sites.client_id
group by concat(clients.first_name, " ", clients.last_name);


