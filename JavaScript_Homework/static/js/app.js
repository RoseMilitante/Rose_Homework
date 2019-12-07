// from data.js
var tableData = data;

// YOUR CODE HERE!

// Get a reference to the table body
var tbody = d3.select("tbody");

// Console.log the data from data.js
console.log(tableData);

// // Create an array with the column names from the given data 
// var columns = ["datetime","city","state","country","shape","durationMinutes","comments"]

// // Loop through the array of givendata and append each row to table on to the webpage 
// function loadData(){
//     tableData.forEach(aliens =>{
//         var row = tbody.append("tr")
//         columns.forEach(column => {
//             if(column =="city" || column =="state" ||column == "country"){
//                 row.append("td").text(aliens[column].toUpperCase())
//               }
//               else row.append("td").text(aliens[column])    
//         })
//     })
// }
// // call the function to load the data 
// loadData()

// // Get a reference to the input element on the page with the id property 
// var inputDate = d3.select("#datetime");
// var inputCity = d3.select("#city");
// var inputState = d3.select("#state");
// var inputCountry = d3.select("#country");
// var inputShape = d3.select("#shape");


// // Get a reference to the filter button on the page with the id property set to `filter-btn`
// var filterButton = d3.select("#filter-btn");

// // Get a reference to the filter button on the page with the id property set to `filter-btn`
// var resetButton = d3.select("#reset-btn");

// // create a function for filtering the data with the given input
// function filterData(){

//     // Prevent the webpage from refreshing
//     d3.event.preventDefault();

//     // Extract the given input for all the fields on the web page
//     var Datevalue = inputDate.property("value")
//     var Cityvalue = inputCity.property("value")
//     var Statevalue = inputState.property("value")
//     var Countryvalue = inputCountry.property("value")
//     var Shapevalue = inputShape.property("value")

//     // Apply the conditions for filtering the data and assign it to a variable
//     var filteredData = tableData.filter(function(recorded){
//        return ((recorded.datetime === Datevalue ||Datevalue == "" ) &&
//                 (recorded.city === Cityvalue ||Cityvalue == "") &&
//                 (recorded.state === Statevalue ||Statevalue == "")&&
//                 (recorded.country === Countryvalue ||Countryvalue == "")&&
//                 (recorded.shape === Shapevalue ||Shapevalue== "")
//             )
//     })

//     // Print the filtered data to the console
//     console.log(filteredData)
//     // Empty the table to append with the filtered data 
//     tbody.text("")
//     // update the table with the filtered data     
//     filteredData.forEach(aliens =>{
//         var row = tbody.append("tr")
//         columns.forEach(column => {
//             if(column =="city" || column =="state" ||column == "country"){
//                 row.append("td").text(aliens[column].toUpperCase())
//               }
//               else row.append("td").text(aliens[column])    
//         })
//     })
// }
// // Add event handler for the click button to filter the table with the given input
// filterButton.on("click",filterData)

// // create a function for resetting the table 
// function resetData(){
//     tbody.text("")
//     loadData()
//     }
    
// // Add event handler for the reset button to reset the table to original data 
// resetButton.on("click",resetData)