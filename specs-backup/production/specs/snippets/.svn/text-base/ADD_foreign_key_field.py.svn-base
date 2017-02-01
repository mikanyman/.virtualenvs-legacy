application = 'portal'
table = 'entry'
foreign_table = 'targetgroup'

print """BEGIN;
  ALTER TABLE %s_%s ADD COLUMN %s_id integer;
  ALTER TABLE %s_%s ALTER COLUMN %s_id SET STORAGE PLAIN;
  -- ALTER TABLE %s_%s ALTER COLUMN %s_id SET NOT NULL;
COMMIT;""" % (\
    application, table, foreign_table, \
    application, table, foreign_table, \
    application, table, foreign_table
)