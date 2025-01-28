const express = require('express');
const bodyParser = require('body-parser');
const mysql = require('mysql');

const app = express();
const port = 3000;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static('public'));

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Gopal@2005',
    database: 'legal_link'
});

connection.connect((err) => {
    if (err) {
        console.error('Error connecting to MySQL: ' + err.stack);
        return;
    }
    console.log('Connected to MySQL as id ' + connection.threadId);
});

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/client.html');
});

// Handle user signup
app.post('/push', (req, res) => {
    const username = req.body.username;
    const client_id = req.body.client_id;
    const name = req.body.name;
    const ph_number = req.body.ph_number;
    const address = req.body.address;
    const lawyer_id = req.body.lawyer_id;
    const type = req.body.drop; // Corrected variable name

    const insertQuery = `INSERT INTO client (user_name, client_id, name, ph_number, address, lawyer_id, type) VALUES (?, ?, ?, ?, ?, ?, ?)`; // Corrected column name
    connection.query(insertQuery, [username, client_id, name, ph_number, address, lawyer_id, type], (error, results) => { // Included 'type' in the values array
        if (error) {
            console.error('Error inserting new user: ' + error);
            return res.status(500).send('Error inserting new user');
        }

        console.log("New user inserted successfully:", results);
        res.send('New user signed up successfully');
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
