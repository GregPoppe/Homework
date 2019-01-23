use sakila;

#1a. Display the first and last names of all actors from the table actor.

select first_name
	,last_name

from actor;


#1b. Display the first and last name of each actor in a single column in upper case letters. Name the column Actor Name.

select concat(upper(first_name), " ",upper(last_name)) as Name_Concat

from actor;



#2a. You need to find the ID number, first name, and last name of an actor, of whom you know only the first name, "Joe." What is one query would you use to obtain this information?

select first_name
	,last_name
    ,actor_id

from actor

where upper(first_name) = "JOE";



#2b. Find all actors whose last name contain the letters GEN:


select first_name
	,last_name
    ,actor_id

from actor

where upper(last_name) like "%GEN%";


#2c. Find all actors whose last names contain the letters LI. This time, order the rows by last name and first name, in that order:

select first_name
	,last_name
    ,actor_id

from actor

where upper(last_name) like "%LI%"
order by 1,2

;


#2d. Using IN, display the country_id and country columns of the following countries: Afghanistan, Bangladesh, and China:


select country_id
	,country

from country

where country in ("Afghanistan", "Bangladesh", "China")
;

#3a. You want to keep a description of each actor. You don't think you will be performing queries on a description, 
#so create a column in the table actor named description and use the data type BLOB (Make sure to research the type BLOB, as the difference between it and VARCHAR are significant).


create table actors_description  (

actor_id int not null primary key,
first_name varchar(30) not null,
last_name varchar(30) not null,
actor_desc blob

)

;

select * from actors_description;


#3b. Very quickly you realize that entering descriptions for each actor is too much effort. Delete the description column.


alter table actors_description
drop column actor_desc
;

select * from actors_description;

#4a. List the last names of actors, as well as how many actors have that last name.


select last_name
	,count(*) as LastNameCount

from actor

group by last_name

;


#4b. List last names of actors and the number of actors who have that last name, but only for names that are shared by at least two actors

select last_name
	,count(*) as LastNameCount

from actor

group by last_name
having LastNameCount >= 2
;




#4c. The actor HARPO WILLIAMS was accidentally entered in the actor table as GROUCHO WILLIAMS. Write a query to fix the record.

#create copy of actors

CREATE TABLE actor_corrected LIKE actor; 
INSERT actor_corrected SELECT * FROM actor;

#Check table
select * from actor_corrected;

#find groucho

select * from actor_corrected where first_name = 'GROUCHO';

update actor_corrected
set first_name = 'HARPO' where first_name = 'GROUCHO' and last_name = 'WILLIAMS';

#find groucho again

select * from actor_corrected where first_name = 'GROUCHO';



#4d. Perhaps we were too hasty in changing GROUCHO to HARPO. It turns out that GROUCHO was the correct name after all! 
#In a single query, if the first name of the actor is currently HARPO, change it to GROUCHO.

update actor_corrected
set first_name = 'GROUCHO' where first_name = 'HARPO' and last_name = 'WILLIAMS';



#5a. You cannot locate the schema of the address table. Which query would you use to re-create it?

#Hint: https://dev.mysql.com/doc/refman/5.7/en/show-create-table.html

show create table address;


#6a. Use JOIN to display the first and last names, as well as the address, of each staff member. Use the tables staff and address:


select a.first_name
	,a.last_name
    ,b.address
    
from staff a
	left join address b
		on a.address_id = b.address_id
;



#6b. Use JOIN to display the total amount rung up by each staff member in August of 2005. Use tables staff and payment.

select a.first_name
	,a.last_name
    ,sum(b.amount) as TotalPayments
    
from staff a
	left join payment b
		on a.staff_id = b.staff_id
        
where month(payment_date) = 8
and year(payment_date) = 2005

group by 1,2
;




#6c. List each film and the number of actors who are listed for that film. Use tables film_actor and film. Use inner join.

select title
	,count(distinct(actor_id)) as Nbr_Actors

from film a
	inner join film_actor b
		on a.film_id = b.film_id
        
group by 1

;

#6d. How many copies of the film Hunchback Impossible exist in the inventory system?

select title
	,count(*) as NbrInv


from film a
	left join inventory b
		on a.film_id = b.film_id

where title = "Hunchback Impossible"

group by 1

;


#6e. Using the tables payment and customer and the JOIN command, list the total paid by each customer. List the customers alphabetically by last name:

select last_name
	,first_name
	,sum(b.amount) as TotalRentalPayments

from customer a 
	inner join payment b
		on a.customer_id = b.customer_id

group by 1,2

order by 1 
;


#7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
#As an unintended consequence, films starting with the letters K and Q have also soared in popularity. 
#Use subqueries to display the titles of movies starting with the letters K and Q whose language is English.

select title

from film

where title in (select title from film where title like 'K%' or title like 'O%')
and language_id = (select language_id from language where lower(name) = 'english')

;


#7b. Use subqueries to display all actors who appear in the film Alone Trip.


select *

from actor

where actor_id in (
	select actor_id from film_actor where film_id =
		(select film_id from film where title = 'Alone Trip')

)
;


#7c. You want to run an email marketing campaign in Canada, for which you will need the names and email addresses of all Canadian customers. Use joins to retrieve this information.

select first_name
	,last_name
    ,email
    ,d.country

from customer a
	inner join address b
		on a.address_id = b.address_id
	inner join city c
		on b.city_id = c.city_id
	inner join country d
		on c.country_id = d.country_id and d.country = 'Canada'

;


#7d. Sales have been lagging among young families, and you wish to target all family movies for a promotion. Identify all movies categorized as family films.

select title
	,c.name

from film a
	left join film_category b
		on a.film_id = b.film_id
	left join category c
		on b.category_id = c.category_id
where c.name = 'Family'

;


#7e. Display the most frequently rented movies in descending order.

select title
	,count(c.rental_id) as NbrTimesRented

from film a
	left join inventory b
		on a.film_id = b.film_id
	left join rental c
		on b.inventory_id = c.inventory_id

group by 1

order by 2 desc

;

#7f. Write a query to display how much business, in dollars, each store brought in.


select a.store_id
	,sum(c.amount) as Totals

from store a
	left join customer b
		on a.store_id = b.store_id
	left join payment c
		on b.customer_id = c.customer_id

group by 1

        
;        


#7g. Write a query to display for each store its store ID, city, and country.

select store_id
	,c.city
    ,d.country


from store a
	left join address b
		on a.address_id = b.address_id
	left join city c
		on b.city_id = c.city_id
	left join country d
		on c.country_id = d.country_id

;



#7h. List the top five genres in gross revenue in descending order. (Hint: you may need to use the following tables: category, film_category, inventory, payment, and rental.)


select a.name
	,sum(e.amount) as Revenue
    

from category a
	left join film_category b
		on a.category_id = b.category_id
	left join inventory c
		on b.film_id = c.film_id
	left join rental d
		on c.inventory_id = d.inventory_id
	left join payment e
		on d.rental_id = e.rental_id
  
group by 1

order by 2 desc

limit 5


;


#8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
#Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

create view top_five_genres as

select a.name
	,sum(e.amount) as Revenue
    

from category a
	left join film_category b
		on a.category_id = b.category_id
	left join inventory c
		on b.film_id = c.film_id
	left join rental d
		on c.inventory_id = d.inventory_id
	left join payment e
		on d.rental_id = e.rental_id
  
group by 1

order by 2 desc

limit 5


;


#8b. How would you display the view that you created in 8a?

select * from top_five_genres;


#8c. You find that you no longer need the view top_five_genres. Write a query to delete it.


drop view if exists top_five_genres;





