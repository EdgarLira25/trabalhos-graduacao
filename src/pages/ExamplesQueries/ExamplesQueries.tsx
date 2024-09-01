import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { FiCopy } from 'react-icons/fi';

const queries: string[] = [
    `SELECT * FROM movies LIMIT 10;`,
    `SELECT year, title, rating FROM movies LIMIT 10;`,
    `SELECT title, rating FROM movies\nWHERE year = 2017\nLIMIT 10;`,
    `SELECT title, rating FROM movies\nWHERE year = 2017\nLIMIT 10;`,
    `SELECT COUNT(*) FROM movies;`,
    `SELECT year, COUNT(*) as total\nFROM movies\nGROUP BY year;`,
    `SELECT year, COUNT(*) as total\nFROM movies\nGROUP BY year\nORDER BY YEAR;`,
    `SELECT type,\n       COUNT(*) as movie_count,\n       min(votes) as min_votes,\n       max(votes) as max_votes,\n       sum(votes) as sum_of_votes,\n       avg(votes) as average_votes\nFROM movies\nGROUP BY type;`,
    `SELECT sum(minutes)/1440 as days,\n       sum(votes)/COUNT(*) as average,\n       17 * (max(votes) - min(votes)) as nonsense\nFROM movies\nWHERE type = 'movie';`,
    `SELECT COUNT(*) FROM people;`,
    `SELECT * FROM people LIMIT 10;`,
    `SELECT * FROM genres;`,
    `SELECT * FROM has_genre\nLIMIT 10;`,
    `SELECT * FROM has_position LIMIT 10;`,
    `SELECT position, COUNT(*) as total\nFROM has_position\nGROUP BY position\norder by total desc;`,
    `SELECT * FROM plays_role LIMIT 10;`,
    `SELECT title, genre\nFROM movies\nJOIN has_genre on has_genre.movie_id = movies.movie_id\nJOIN genres on genres.genre_id = has_genre.genre_id\nWHERE year = 2017\nLIMIT 20;`,
    `SELECT title, genre\nFROM movies as m\nJOIN has_genre as hg on hg.movie_id = m.movie_id\nJOIN genres as g on g.genre_id = hg.genre_id\nWHERE year = 2017\nLIMIT 20;`,
    `SELECT title, year, rating, votes\nFROM movies as m\nJOIN has_genre as hg1 on hg1.movie_id = m.movie_id\nJOIN has_genre as hg2 on hg2.movie_id = m.movie_id\nJOIN genres as g1 on g1.genre_id = hg1.genre_id\nJOIN genres as g2 on g2.genre_id = hg2.genre_id\nWHERE m.votes > 100000 and g1.genre = 'Romance' and g2.genre = 'Comedy'\norder by votes desc;`,
    `SELECT m1.title, m1.year, g.genre, m1.rating, m1.votes\nFROM movies as m1\nJOIN has_genre as hg on hg.movie_id = m1.movie_id\nJOIN genres as g on g.genre_id = hg.genre_id\nWHERE m1.votes > 100000 and (not (g.genre = 'Romance' or g.genre = 'Comedy'))\n      and m1.movie_id in\n         (SELECT m2.movie_id\n         FROM movies as m2\n         JOIN has_genre as hg1 on hg1.movie_id = m2.movie_id\n         JOIN has_genre as hg2 on hg2.movie_id = m2.movie_id\n         JOIN genres as g1 on g1.genre_id = hg1.genre_id\n         JOIN genres as g2 on g2.genre_id = hg2.genre_id\n         WHERE g1.genre = 'Romance' and g2.genre = 'Comedy')\norder by m1.votes desc\nLIMIT 10;`,
    `create view romcom_ids as\n    SELECT m.movie_id as movie_id\n    FROM movies as m\n    JOIN has_genre as hg1 on hg1.movie_id = m.movie_id\n    JOIN has_genre as hg2 on hg2.movie_id = m.movie_id\n    JOIN genres as g1 on g1.genre_id = hg1.genre_id\n    JOIN genres as g2 on g2.genre_id = hg2.genre_id\n    WHERE g1.genre = 'Romance' and g2.genre = 'Comedy';`,
    `SELECT m.title, m.year, g.genre, m.rating, m.votes\nFROM romcom_ids as r\nJOIN has_genre as hg on hg.movie_id = r.movie_id\nJOIN genres as g on g.genre_id = hg.genre_id\nJOIN movies as m on m.movie_id = r.movie_id\nWHERE m.votes > 100000 and (not (g.genre = 'Romance' or g.genre = 'Comedy'))\norder by m.votes desc\nLIMIT 10;`,
    `SELECT COUNT(*)\nFROM people\nWHERE deathYear is null;`,
    `SELECT name, position\nFROM people as p\nJOIN has_position as c on p.person_id = c.person_id\nJOIN movies as m on c.movie_id = m.movie_id\nWHERE title = 'Silver Linings Playbook';`,
    `SELECT name, position, role\nFROM people as p\nJOIN has_position as c on p.person_id = c.person_id\nJOIN movies as m on c.movie_id = m.movie_id\nJOIN plays_role as r on r.movie_id = m.movie_id and r.person_id = c.person_id\nWHERE title = 'Silver Linings Playbook';`,
    `SELECT name, position, role\nFROM people as p\nJOIN has_position as c on p.person_id = c.person_id\nJOIN movies as m on c.movie_id = m.movie_id\nleft JOIN plays_role as r on r.movie_id = m.movie_id and r.person_id = c.person_id\nWHERE title = 'Silver Linings Playbook';`,
    `SELECT r1.role as role, m1.title as title, m1.year as year\nFROM plays_role as r1\nJOIN plays_role as r2 on r2.person_id = r1.person_id\nJOIN movies as m1 on m1.movie_id = r1.movie_id\nJOIN movies as m2 on m2.movie_id = r2.movie_id\nJOIN people as p on p.person_id = r1.person_id\nWHERE p.name = 'Jennifer Lawrence'\n      and r1.role = r2.role\norder by r1.role, m1.title, m1.year;`,
    `SELECT r1.role as role, m1.title as title, m1.year as year\nFROM plays_role as r1\nJOIN plays_role as r2 on r2.person_id = r1.person_id\nJOIN movies as m1 on m1.movie_id = r1.movie_id\nJOIN movies as m2 on m2.movie_id = r2.movie_id\nJOIN people as p on p.person_id = r1.person_id\nWHERE p.name = 'Jennifer Lawrence'\n      and r1.role = r2.role\n      and m1.movie_id <> m2.movie_id\norder by r1.role, m1.title, m1.year;`,
    `SELECT r1.role as role, m1.title as title, m1.year as year\nFROM plays_role as r1\nJOIN plays_role as r2 on r2.person_id = r1.person_id\nJOIN movies as m1 on m1.movie_id = r1.movie_id\nJOIN movies as m2 on m2.movie_id = r2.movie_id\nJOIN people as p on p.person_id = r1.person_id\nWHERE p.name = 'Noomi Rapace'\n      and r1.role = r2.role\n      and m1.movie_id <> m2.movie_id\norder by m1.title, r1.role, m1.year;`,
    `SELECT distinct r1.role as role, m1.title as title, m1.year as year\nFROM plays_role as r1\nJOIN plays_role as r2 on r2.person_id = r1.person_id\nJOIN movies as m1 on m1.movie_id = r1.movie_id\nJOIN movies as m2 on m2.movie_id = r2.movie_id\nJOIN people as p on p.person_id = r1.person_id\nWHERE p.name = 'Noomi Rapace'\n      and r1.role = r2.role\n      and m1.movie_id <> m2.movie_id\norder by m1.title, r1.role, m1.year;`,
    `SELECT distinct r1.role as role, m1.title as title, m1.year as year\nFROM plays_role as r1\nJOIN plays_role as r2 on r2.person_id = r1.person_id\nJOIN movies as m1 on m1.movie_id = r1.movie_id\nJOIN movies as m2 on m2.movie_id = r2.movie_id\nJOIN people as p on p.person_id = r1.person_id\nWHERE p.name = 'Scarlett Johansson'\n      and r1.role = r2.role\n      and m1.movie_id <> m2.movie_id\norder by m1.title, r1.role, m1.year;`,
    `SELECT * FROM has_alternative LIMIT 20;`,
    `SELECT * FROM languages LIMIT 10;`,
    `SELECT * FROM countries LIMIT 10;`,
    `SELECT m.title as title,\n       a.title as alt_title,\n       a.is_original as orig,\n       c.name as country,\n       l.name as language\nFROM movies as m\nJOIN has_alternative as a on a.movie_id = m.movie_id\nleft JOIN countries as c on a.country_code = c.code\nleft JOIN languages as l on a.language_code = l.code\nWHERE m.movie_id = 'tt0032138';`,
    `SELECT m.title as title,\n       a.title as alt_title,\n       a.is_original as orig,\n       c.name as country,\n       l.name as language\nFROM movies as m\nJOIN has_alternative as a on a.movie_id = m.movie_id\nleft JOIN countries as c on a.country_code = c.code\nleft JOIN languages as l on a.language_code = l.code\nWHERE m.movie_id = 'tt0032138'\n  and (a.is_original = TRUE or c.name = 'Hong Kong')\norder by a.title;`
];


const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text).then(() => {
        toast.success('Query copiada para a área de transferência!', {
            position: "bottom-center",
            autoClose: 2000,
            hideProgressBar: true,
            closeOnClick: true,
            pauseOnHover: false,
            draggable: true,
            progress: undefined,
        });
    });
};

const ExamplesQueries = () => {
    return (
        <div style={{ padding: '20px' }}>
            <h1>Lista de Queries</h1>
            <div style={{ maxHeight: '650px', overflowY: 'auto', padding: '10px' }}>
                <ul style={{ listStyleType: 'none', padding: 0 }}>
                    {queries.map((query, index) => (
                        <li key={index} style={{ marginBottom: '20px' }}>
                            <div style={{ display: 'flex', alignItems: 'center' }}>
                                <pre style={{
                                    backgroundColor: '#f4f4f4',
                                    padding: '10px',
                                    borderRadius: '5px',
                                    margin: 0,
                                    overflowX: 'auto',
                                    maxWidth: '600px',
                                    whiteSpace: 'pre-wrap',
                                    wordWrap: 'break-word',
                                    flex: 1
                                }}>
                                    {query}
                                </pre>
                                <FiCopy
                                    onClick={() => copyToClipboard(query)}
                                    style={{ marginLeft: '10px', cursor: 'pointer' }}
                                    size={24}
                                />
                            </div>
                        </li>
                    ))}
                </ul>
            </div>
            <ToastContainer />
        </div >
    );
};

export default ExamplesQueries;
