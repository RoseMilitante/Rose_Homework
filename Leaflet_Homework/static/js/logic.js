// **Get your data set**
// Visit the [USGS GeoJSON Feed] (http://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php) page and pick a data set to visualize.

var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson";

// Perform a GET request to the query URL
d3.json(url, function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  createFeatures(data.features);
});


// Create our map
function createFeatures(data) {
    var myMap = L.map("map", {
        center: [37.09, -95.71],
        zoom: 4
    });
    
    // Define the streetmap layer
    L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "mapbox.streets",
        accessToken: API_KEY
      }).addTo(myMap);

    // Create data markers that reflect
    // the magnitude of the earthquake in their size and color. 
    // Earthquakes with higher magnitudes should appear larger and darker in color.
    data.forEach(feature => {

        var color = "";
        if (feature.properties.mag <= 1) {
            color = "green";
        }
        else if (feature.properties.mag <= 2) {
            color = "#d3e66c";
        }
        else if (feature.properties.mag <= 3) {
            color = "yellow";
        }
        else if (feature.properties.mag <= 4) {
            color = "orange";
        }
        else if (feature.properties.mag <= 5) {
            color = "#b35037";
        }
        else {
            color = "red";
        }

        L.circle([feature.geometry.coordinates[1],
                 feature.geometry.coordinates[0]], {
                    fillColor: color,
                    fillOpacity: 0.5,
                    color: color,
                    radius: feature.properties.mag * 12000
        // Add a popup that provides additional info about the earthquake when clicked            
                 }).bindPopup("<h2> Location: <br>" + feature.properties.place + "<hr>Mag: " + feature.properties.mag + "</h3>").addTo(myMap);
    });
    
    // Create a legend that will provide context for the map data
    var legend = L.control({position: 'bottomright'});
    legend.onAdd = function() {
        var div = L.DomUtil.create('div', 'info legend');
        var labels = ["0-1", "1-2", "2-3", "3-4", "4-5", "5+"];
        var colors = ["green", "#d3e66c", "yellow",
                        "orange", "#b35037", "red"];
    
        // loop through the magnitude intervals to generate the legend labels
        // coinciding with the background color of  for each magnitude interval
        for (var i = 0; i < colors.length; i++) {
            div.innerHTML +=
                '<li style="background-color:' + colors[i] + '">' + labels[i] + '</li>';
            }
        return div;
    }
    legend.addTo(myMap);
}

