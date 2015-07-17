# Migrating

The idea is to take the existing production database, create a model + migration on the django side
that is compatible with it, migrate the existing data as exampled below and take it from there.

## Apps

### Mededelingen

We have never had a state where every field of the existing database exists in the new model.
Just migrate to 0001, clone the table `mededeling` and remove all columns that are not in the
new database at that state.
Than dump the data from the cloned table and insert them into the new one.
The migrations take care of the rest.

### Base

You can import the data from 'profielen' on the database after migration 0001 (or 0002)

    mysqldump -u root profielen --no-create-info -c > profielen_data.sql
    mysql -u root csrdelft_django < profielen_data.sql

After importing those, you can create the authentication users from the legacy `accounts` table.
Because the migration requires some transformation of the passwords and access to both
the old and new database, it has been implemented as a separate script (`bin/migrate_accounts.py`).
If you've setup the DATABASE config in your `settings.py` correctly, with legacy pointing to
a running legacy database, you can run the script `python bin/migrate_accounts.py` from the `src/`
directory.

You can import the data from 'groepen' on the database after base migration 0003:

    mysqldump -u root csrdelft \
      kringen kring_leden \
      commissies commissie_leden \
      besturen bestuurs_leden \
      werkgroepen werkgroep_deelnemers \
      verticalen verticale_leden \
      onderverenigingen ondervereniging_leden \
      lichtingen lichting_leden \
      ketzers ketzer_deelnemers \
      activiteiten activiteit_deelnemers \
      groepen groep_leden \
      --no-create-info -c > groepen_data.sql
    mysql -u root csrdelft_django < groepen_data.sql

### Forum

You can import the data from the production database after it's initial migration 0001:

    mysqldump -u root csrdelft \
      forum_posts forum_draden_gelezen forum_draden_reageren \
      forum_draden_volgen forum_draden_verbergen forum_categorien \
      forum_delen forum_draden --no-create-info -c > forum_data.sql
    mysql -u root csrdelft_django < forum_data.sql

### Announcements

You can import the data from the legacy production database after 0001, but not all columns are
included, so you'll need to clone the table, delete the columns that don't exist on the new
database, dump the data and import that data.
