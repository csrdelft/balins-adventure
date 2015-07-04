# Architectural overview of our stek stack

Our stack is set up as follows:

    +----------+           +---------+-----------+
    |          |           |         |           |           +--------------+
    |          |           |         |           |           |              |
    |          |           |      +----->        |           |              |
    |          |           |         |           | models.py |              |
    |          |           |         |   api.py +------------->     DB      |
    |          |           |         |           |           |              |
    |          |           |      +----->        |           |              |
    |          |           |         |           |           |              |
    |          |           |         |           |           +--------------+
    |          |           |         |           |
    |          |   HTTP    |         |           |
    |  Client  +-----------> Django  | Service   |
    |          |   REST    | routing | endpoints |         +-----------------+
    |          |           |         |           |         |                 |
    |          |           | urls.py |          +-----+----->     Redis      |
    |          |           |         |           |    ^    | Key-value-store |
    |          |           |      +----->        |    |    +-----------------+
    |          |           |         |           |    |
    |          |           |         |  views.py |    |    +-----------------+
    |          |           |         |           |    |    |                 |
    |          |           |      +----->        |    |    |      SOLR       |
    |          |           |         |          +-----------^ Search Ser^er  |
    |          |           |         |           |    |    +-----------------+
    |          |           +---------+-----------+    |
    |          |                                      |
    |          |           +---------------------+    |
    |          |   web     |                     |    |
    |          |  socket   |       NODEJS        |    |
    |          +----------->  Tiny Socket Server +----+
    |          |           |                     |
    +----------+           +---------------------+

Which might look daunting, but you can immediately forget about NODEJS, SOLR and Redis for now.
The important part is the "client --- HTTP --> Django --> DB" section.

This is a modern stack, so there is actually another part to this picture which isn't shown in
detail in the above schema: the client.
We'll look at the client in more detail in one of the next "chapters".
