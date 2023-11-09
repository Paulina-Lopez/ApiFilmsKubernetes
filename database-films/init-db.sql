CREATE TABLE "public"."film" (
    "id" SERIAL PRIMARY KEY,
    "title" character varying,
    "length" integer,
    "year" integer,
    "director" character varying
);

CREATE TABLE "public"."actor" (
    "id" SERIAL PRIMARY KEY,
    "name" character varying,
    "film_id" integer NOT NULL REFERENCES "public"."film"("id")
);

CREATE TABLE "public"."alembic_version" (
    "version_num" character varying(32) NOT NULL PRIMARY KEY
);
