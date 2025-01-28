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
    res.sendFile(__dirname + '/index.html');
});

// Handle user signup
app.post('/signup', (req, res) => {
    const newUsername = req.body.new_username;
    const newPassword = req.body.new_password;

    const insertQuery = `INSERT INTO login (user_name, password) VALUES (?, ?)`;
    connection.query(insertQuery, [newUsername, newPassword], (error, results) => {
        if (error) {
            console.error('Error inserting new user: ' + error);
            return res.status(500).send('Error inserting new user');
        }

        console.log("New user inserted successfully:", results);
        res.send('New user signed up successfully');
    });
});

app.post('/submit', (req, res) => {
    const username = req.body.username;
    const password = req.body.password;

    const query = `SELECT * FROM login WHERE user_name = ? AND password = ?`;

    connection.query(query, [username, password], (error, results) => {
        if (error) {
            console.error('Error querying database: ' + error);
            return res.status(500).send('Error querying database');
        }

        console.log("Results:", results);

        if (results.length > 0) {
            // Login successful, send welcome.html
            res.sendFile(__dirname + '/welcome.html');
        } else {
            res.send('Invalid username or password');
        }
    });
});


app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
