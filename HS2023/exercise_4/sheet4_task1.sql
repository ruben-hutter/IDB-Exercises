-- 1)
select distinct result from games;

-- 2)
select result, count(*) as count from games group by result;

-- 3)
select e.eco_code, count(*) as opening_count
from openings o
join ecos e on o.eco_id = e.eco_id 
group by e.eco_code 
order by opening_count desc;

-- 4)
select e.eco_code, count(*) as games_played
from games g 
join openings o on g.opening_id = o.opening_id 
join ecos e on o.eco_id = e.eco_id 
group by e.eco_code 
order by games_played desc;

-- 5)
select
	p1.player_name as white_player,
	p2.player_name as black_player,
	t.tournament_url,
	coalesce(t1.title_short, 'No Title') as white_title,
	coalesce(t2.title_short, 'No Title') as black_title
from games g
join players p1 on g.white = p1.player_id
join players p2 on g.black = p2.player_id
join tournaments t on g.tournament_id = t.tournament_id
left join titles t1 on g.white_title = t1.title_id
left join titles t2 on g.black_title = t2.title_id
where g.result = '1-0';

-- 6)
select count(*)
from openings o 
where opening_text like '%Queen%';

-- 7)
select opening_text
from openings o 
where opening_text like '%Queen%'
order by length(opening_text) desc 
limit 1;

-- 8) without join
select count(*) from games 
where opening_id = (
select opening_id from openings 
where opening_text ilike '%Queen%' 
order by length(opening_text) desc 
limit 1);


-- 8) with join
select count(*) 
from games 
join(
    select opening_id 
    from openings 
    where opening_text ilike '%Queen%' 
    order by length(opening_text) desc 
    limit 1
) as selected_opening on games.opening_id = selected_opening.opening_id;
	
-- 9)
select max(length(substring(player_name from '%ruben%' for ''))) as longest_sequence
from players p 
where player_name ilike '%ruben%';

-- 10)
alter table titles add column title_long text;
update titles set title_long = 'International Master' where title_short = 'IM';
update titles set title_long = 'Candidate Master' where title_short = 'CM';
update titles set title_long = 'FIDE Master' where title_short = 'FM';
update titles set title_long = 'Lichess Master' where title_short = 'LM';
update titles set title_long = 'National Master' where title_short = 'NM';

-- 11)
insert into titles (title_id, title_short, title_long)
values (default, 'GM', 'Grand Master');

-- 12)
create table plays_in (
	game_id int references games(game_id),
	player_id int references players(player_id),
	is_white bit(1) not null,
	primary key (game_id, player_id),
	constraint CHK_Player_Color check (is_white in (b'0', b'1'))
);

-- 13)
-- Note: apparently, some players can be black and white at the same time...
select * from games g
where g.black = g.white;

-- Players that played against themselves will be listed as white...
insert into plays_in (game_id, player_id, is_white)
select g.game_id, g.white, b'1'
from games g
union all
select g.game_id, g.black, b'0'
from games g
where g.white <> g.black;

-- 14)
select player_id, count(distinct game_id) as games_played
from plays_in pi2 
group by player_id 
order by games_played desc 
limit 1;

-- 15)
select player_id, count(*) as games_won
from(
	select white as player_id from games where result = '1-0'
	union all
	select black from games where result = '0-1'
) as subquery
group by player_id
order by games_won desc
limit 1;

-- 16)
select g.white, g.black
from games g
group by g.white, g.black
having count(*) >= 100;

-- 17) Python script

-- 18) Python script

-- 19)
select
	p.player_id, 
    p.player_name, 
    string_agg(distinct t.title_short, ', ') as titles
from 
    players p
join 
    games g on g.white = p.player_id or g.black = p.player_id
join 
    titles t on g.white_title = t.title_id or g.black_title = t.title_id
group by 
    p.player_id, 
    p.player_name
having 
    count(t.title_id) > 0
order by 
    p.player_id;

-- 20)
create view games_and_names as
select g.game_id, wp.player_name as white_name, bp.player_name as black_name, g.result
from games g
join players wp on g.white = wp.player_id
join players bp on g.black = bp.player_id;

-- 21)
create view games_in_tournament as
select tournament_id, count(*) as games_count
from games
where tournament_id is not null
group by tournament_id;

-- 22)
select min(games_count), avg(games_count), max(games_count)
from games_in_tournament;
