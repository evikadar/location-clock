ALTER TABLE IF EXISTS ONLY public.locations DROP CONSTRAINT IF EXISTS fk_user_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.people DROP CONSTRAINT IF EXISTS fk_user_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.locations DROP CONSTRAINT IF EXISTS pk_locations_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.people DROP CONSTRAINT IF EXISTS pk_people_id CASCADE;
ALTER TABLE IF EXISTS ONLY public.users DROP CONSTRAINT IF EXISTS pk_users_id CASCADE;

DROP TABLE IF EXISTS public.locations;
DROP SEQUENCE IF EXISTS public.locations_id_seq;
CREATE TABLE locations (
    id integer NOT NULL CHECK (id > 0 AND id < 12),
    title text NOT NULL,
    location varchar(12) CHECK (location ~* '^[23456789CFGHJMPQRVWX+]') NOT NULL,
    user_id integer
);

DROP TABLE IF EXISTS public.people;
DROP SEQUENCE IF EXISTS public.people_id_seq;
CREATE TABLE people (
    id serial NOT NULL,
    name text NOT NULL,
    phone text NOT NULL,
    color varchar(7) CHECK (color ~* '^#[0-9a-f]{6}') NOT NULL,
    status text,
    user_id integer
);

DROP TABLE IF EXISTS public.users;
DROP SEQUENCE IF EXISTS public.users_id_seq;
CREATE TABLE users (
    id serial NOT NULL,
    user_name text NOT NULL UNIQUE,
    password text NOT NULL,
    email text,
    phone text
);


ALTER TABLE ONLY locations
    ADD CONSTRAINT pk_locations_id PRIMARY KEY (id);

ALTER TABLE ONLY people
    ADD CONSTRAINT pk_people_id PRIMARY KEY (id);

ALTER TABLE ONLY users
    ADD CONSTRAINT pk_users_id PRIMARY KEY (id);

ALTER TABLE ONLY locations
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE ONLY people
    ADD CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users(id);
