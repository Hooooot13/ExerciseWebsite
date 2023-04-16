<?php
$servername = "localhost";
$username = "postgres";
$password = "postgres";
$dbname = "exercise-db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Get query from AJAX request
$query = $_POST['query'];

// Execute query
$result = $conn->query($query);

// Check if query was successful
if ($result === FALSE) {
  echo "Error: " . $conn->error;
} else {
  // Display query result
  echo "<table>";
  while ($row = $result->fetch_assoc()) {
    echo "<tr>";
    foreach ($row as $key => $value) {
      echo "<td>" . $value . "</td>";
    }
    echo "</tr>";
  }
  echo "</table>";

  // Free result set
  $result->free();
}

// Close connection
$conn->close();
?>
