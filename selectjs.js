// Assuming you're using Express.js
const express = require('express');
const mysql = require('mysql');

const app = express();
const port = 3000;

// MySQL database connection configuration
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'Gopal@2005',
    database: 'legal_link'
});

// Connect to MySQL database
connection.connect((err) => {
  if (err) {
    console.error('Error connecting to MySQL database: ' + err.stack);
    return;
  }
  console.log('Connected to MySQL database');
});

// Serve static files from the public directory
app.use(express.static('public'));

// Route for the root URL
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/select.html');
});

// Handle GET requests to '/lawyers'
app.get('/lawyers', (req, res) => {
  const specialization = req.query.specialization;

  // Check if specialization is provided
  if (!specialization) {
    res.status(400).send('Please select a specialization');
    return;
  }

  // Query to select data from the database based on the specialization
  const query = `SELECT specialization, name, contact_num, lawyer_id, base_fee FROM ${specialization}_lawyer`;

  // Execute the query
  connection.query(query, (err, results) => {
    if (err) {
      console.error('Error executing query: ' + err.stack);
      res.status(500).send('Error fetching data from database');
      return;
    }

    // Generate HTML table
    let tableHtml = '<table border="1"><tr><th>Specialization</th><th>Name</th><th>Contact Number</th><th>Lawyer ID</th><th>Base Fee</th></tr>';
    results.forEach(row => {
      tableHtml += `<tr><td>${row.specialization}</td><td>${row.name}</td><td>${row.contact_num}</td><td>${row.lawyer_id}</td><td>${row.base_fee}</td></tr>`;
    });
    tableHtml += '</table>';

    // Send the HTML response
    res.send(tableHtml);
  });
});

// Start the server
app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
