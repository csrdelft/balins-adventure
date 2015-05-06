## Apps

### Forum

You can import the data from the production database, like so:

    mysqldump -u root csrdelft forum_posts forum_draden_gelezen forum_draden_reageren forum_draden_volgen forum_draden_verbergen forum_categorien forum_delen forum_draden --no-create-info -c > forum_data.sql
  mysql -u root csrdelft_django < forum_data.sql

Into the forum app right after it's initial migration 0001
