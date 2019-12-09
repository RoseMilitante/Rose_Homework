// From data.js
var tableData = data;

// Select tbody, since table should be filled with the data
var tbody = d3.select("tbody");

// appends all the data from data.js file into the html page
data.forEach((ufoSighting) => {
    //add a new row for each grouping of data
    var row = tbody.append("tr");
    Object.entries(ufoSighting).forEach(([key, value]) => {
      var cell = tbody.append("td");
      cell.text(value);
    });
});

// Select the submit button when clicked
var submit = d3.select("#filter-btn");

// take the input from the user and filter the data 
submit.on("click", function() {

    // Select the input element 
    var inputElement = d3.select("#datetime");
  
    // Get the value the input
    var userInput = inputElement.property("value");
 
    // Prevent the page from refreshing
    d3.event.preventDefault();

    // filter the table to match the input given
    var filteredTable = tableData.filter(ufoSighting => ufoSighting.datetime === userInput);
    tbody.html("");
    
    // displayed only the filtered data
    filteredTable.forEach((ufoSighting) => {
        var row = tbody.append("tr");
        Object.entries(ufoSighting).forEach(([key, value]) => {
          var cell = tbody.append("td");
          cell.text(value);
        });
    });
 });