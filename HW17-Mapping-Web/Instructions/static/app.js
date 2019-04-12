// API key
var API_KEY = "pk.eyJ1IjoiZ3BvcHBlMzI5IiwiYSI6ImNqc3dsY21rOTBpd2EzeXA0bTFlZjJyNGoifQ.PVwD8icaB8LgqYS-q9yiyg";

console.log("test");




var street = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 13,
    id: 'mapbox.streets',
    accessToken: API_KEY
});


var dark = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 13,
    id: 'mapbox.dark',
    accessToken: API_KEY
});




function printMap(data, plates){

  var faultlines = L.geoJSON(plates);
  faultlines.addLayer(L.marker([22,-22]));

  var earthquakes = L.geoJSON(data);
  earthquakes.addLayer(L.marker([40,-20]));
  earthquakes.addLayer(L.marker([20,-10]));
  earthquakes.addLayer(L.marker([10,-90]));
  earthquakes.addLayer(L.circle([50,-50], {radius: 100000}));

  var bglayers = {
    'Street View' : street,
    'Dark View' : dark
  };

  var overlay_layers = {
    'Earthquakes' : earthquakes,
    'Fault Lines' : faultlines
  };

  var mymap = L.map('map',
    {'layers': [street, dark]}).setView([40, -30], 3);


  L.control.layers(bglayers, overlay_layers).addTo(mymap);


  //Legend



  var legend = L.control({position: 'bottomright'});

  legend.onAdd = function (map) {

      var div = L.DomUtil.create('div', 'info legend');

          div.innerHTML = '<p> <i style="background:red"></i> Legend 1 </p> <p> <i style="background:red"></i> Legend 2 </p> <i style="background:red"></i>Legend 3';
      

      return div;
  };

  legend.addTo(mymap); 

};



d3.json('https://raw.githubusercontent.com/fraxen/tectonicplates/master/GeoJSON/PB2002_plates.json')
  .then(plates => {
    d3.json('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_week.geojson')
      .then(data => printMap(data, plates));
  
  
  });