## Run in Python to create PostgreSQL stored procedure
## for Many to Many Field

application = 'portal'
table_1 = 'entry'
table_2_sg = 'category'
table_2_pl = 'categories'
owner = 'specs'

print """BEGIN;

CREATE SEQUENCE %s_%s_%s_id_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;
ALTER TABLE %s_%s_%s_id_seq OWNER TO %s;

CREATE TABLE %s_%s_%s
(
  id int4 NOT NULL DEFAULT nextval('%s_%s_%s_id_seq'::regclass),
  %s_id int4 NOT NULL,
  %s_id int4 NOT NULL,
  CONSTRAINT %s_%s_%s_pkey PRIMARY KEY(id),
  CONSTRAINT %s_%s_%s_%s_id_fkey FOREIGN KEY (%s_id)
      REFERENCES %s_%s (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT %s_%s_%s_%s_id_fkey FOREIGN KEY (%s_id)
      REFERENCES %s_%s (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION DEFERRABLE INITIALLY DEFERRED,
  CONSTRAINT %s_%s_%s_%s_id_key UNIQUE(%s_id, %s_id)
) 
WITHOUT OIDS;
ALTER TABLE %s_%s_%s OWNER TO %s;

COMMIT;""" % (\
    application, table_1, table_2_sg,\
    application, table_1, table_2_sg, owner,\
    application, table_1, table_2_pl,\
    application, table_1, table_2_sg,\
    table_1,\
    table_2_sg,\
    application, table_1, table_2_sg,\
    application, table_1, table_2_sg, table_1, table_1,\
    application, table_1,\
    application, table_1, table_2_sg, table_2_sg, table_2_sg,\
    application, table_2_sg,\
    application, table_1, table_2_sg, table_1, table_1, table_2_sg,\
    application, table_1, table_2_pl, owner
)