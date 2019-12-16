function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

  // Use `d3.json` to fetch the metadata for a sample
  
  var metaDataUrl = '/metadata/${sample}';
  d3.json(metaDataUrl).then(function(sample){
    console.log(sample);

    // Use d3 to select the panel with id of `#sample-metadata`
      var sampleData = d3.select('#sample-metadata');
    
    // Use `.html("") to clear any existing metadata
    sampleData.html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    Object.entries(sample).forEach(function([key,value]) {
      var row = sampleData.append("p");
      row.text('${key}:${value}')

    });
  });
}

function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var sampleDataUrl = '/samples/${sample}';
  d3.json(sampleDataUrl).then(function(data) {
    console.log(sample);

    // @TODO: Build a Bubble Chart using the sample data
    var x_values = data.otu_ids;
    var y_values = data.sample_values;
    var sizes = data.sample_values;
    var colors = data.otu_ids; 
    var values = data.otu_labels;

    var bubbleTrace = {
      x: x_values,
      y: y_values,
      text: values,
      mode: 'markers',
      marker: {
        color: colors,
        size: sizes} 
    };
  
    var data = [bubbleTrace];

    var layout = {
      xaxis: { title: "OTU ID"},
      title: "Belly Button Bacteria"
    };

    Plotly.plot('bubble', data, layout);
  });

    // @TODO: Build a Pie Chart
    // HINT: You will need to use slice() to grab the top 10 sample_values,
    // otu_ids, and labels (10 each).
  d3.json(sampleDataUrl).then(function(data) {  
    var pieValues = data.sample_values.slice(0,10);
    var pieLabels = data.otu_ids.slice(0,10);
    var pieHover = data.otu_labels.slice(0,10);

    var pieData = {
        values: pieValues,
        labels: pieLabels,
        hovertext: pieHover,
        type: 'pie'
      };
    Plotly.plot('pie', pieData);

  });
}



function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
