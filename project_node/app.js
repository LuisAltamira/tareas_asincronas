const http = require('http').Server();
const io = require('socket.io')(http);
const redis = require('redis');

// const express = require('express');
// const bodyParser = require('body-parser');


const redisClient = redis.createClient(6379, 'localhost');
// const app = express();

// app.use(bodyParser.urlencoded({extended: false}));
// app.use(bodyParser.json());


// app.get('/', (req, res) => {
//     res.send({message: 'hola mundo'}).status(200);
// });

io.on('connection', (socket) => {
    console.log('un usuario se ha conectado');
    socket.on('subscribe', (celeryTaskId) => {
        redisClient.subscribe(celeryTaskId);
    });
    redisClient.on('message', (channel, message) => {
        console.log(message);
        console.log(channel);
        socket.emit('result', message);
    });
});

http.listen(3000, () => console.log('listening on port 3000...'));
// app.listen(3000, 'localhost', () => {
//     console.log('aplicacion andando en http://localhost:3000');
// });