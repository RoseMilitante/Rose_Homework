// @TODO: YOUR CODE HERE!

// Store width and height parameters to be used in later in the canvas
var svgWidth = 950;
var svgHeight = 600;

// Set svg margins 
var margin = {
  top: 30,
  right: 30,
  bottom: 80,
  left: 90
};

// Create the width and height based svg margins and parameters to fit chart group within the canvas
var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;

// Create the canvas to append the SVG group that contains the given data
// Give the canvas width and height calling the variables predifined.
var svg = d3.select("#scatter")
  .append("svg")
  .attr("width", svgWidth)
  .attr("height", svgHeight);

// Create the chartGroup that will contain the data
// Use transform attribute to fit it within the canvas
var chartGroup = svg.append("g")
  .attr("transform", `translate(${margin.left}, ${margin.top})`);

// Import Data
var file = "assets/data/data.csv"

// Function is called and passes csv data
d3.csv(file).then(successHandle, errorHandle);

function errorHandle(error) {
  throw err;
}

function successHandle(givenData) {

  // Loop through the data and pass argument data
    givenData.map(function(data) {
      data.smokes = +data.smokes;
      data.age = +data.age;
    });

  //  Create scale functions
  // Linear Scale takes the min to be displayed in axis, and the max of the data
  var xLinearScale = d3.scaleLinear()
    .domain([8.1, d3.max(givenData, d => d.age)])
    .range([0, width]);

  var yLinearScale = d3.scaleLinear()
    .domain([20, d3.max(givenData, d => d.smokes)])
    .range([height, 0]);

  // Create axis functions by calling the scale functions

  var bottomAxis = d3.axisBottom(xLinearScale);
  var leftAxis = d3.axisLeft(yLinearScale);

  // Append the axes to the chart group 
  // Bottom axis moves using height 
  chartGroup.append("g")
    .attr("transform", `translate(0, ${height})`)
    .call(bottomAxis);
  
  // Left axis is already at 0,0
  // Only append the left axis 
  chartGroup.append("g")
    .call(leftAxis);


  // Create Circles
  var circlesGroup = chartGroup.selectAll("circle")
    .data(givenData)
    .enter()
    .append("circle")
    .attr("cx", d => xLinearScale(d.age))
    .attr("cy", d => yLinearScale(d.smokes))
    .attr("r", "15")
    .attr("fill", "lightblue")
    .attr("opacity", ".65");


  // Append text to circles 

  var circleLabel = chartGroup.selectAll()
    .data(givenData)
    .enter()
    .append("text")
    .attr("x", d => xLinearScale(d.age))
    .attr("y", d => yLinearScale(d.smokes))
    .style("font-size", "15px")
    .style("text-anchor", "middle")
    .style('fill', "white")
    .text(d => (d.abbr));

  // Step 6: Initialize tool tip
  // ==============================
  var toolTip = d3.tip()
    .attr("class", "tooltip")
    .offset([80, -60])
    .html(function (d) {
      return (`${d.state}<br>Age: ${d.age}%<br>Smokers: ${d.smokes}% `);
    });

  // Step 7: Create tooltip in the chart
  // ==============================
  chartGroup.call(toolTip);

  // Step 8: Create event listeners to display and hide the tooltip
  // ==============================
  circlesGroup.on("click", function (data) {
    toolTip.show(data, this);
  })
    // onmouseout event
    .on("mouseout", function (data, index) {
      toolTip.hide(data);
    });

  // Create axes labels
  chartGroup.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 0 - margin.left + 40)
    .attr("x", 0 - (height / 2))
    .attr("dy", "1em")
    .attr("class", "axisText")
    .text("Smokes (%)");

  chartGroup.append("text")
    .attr("transform", `translate(${width / 2}, ${height + margin.top + 30})`)
    .attr("class", "axisText")
    .text("Age (%)");
}