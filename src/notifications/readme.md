# Tiny C.S.R. Delft Notifications Server

Relatively uncomplicated bridge between redis queue and stek clients.

Stek clients connect using websocket upon which we read their session data and subscribe
to the appropriate event channels on the redis server.
Any incoming message from the redis channel is then forwarded back to the subscribed clients.

## Getting started

On unix this will do:

    npm install
    npm start

provided that a **redis server is running**.
