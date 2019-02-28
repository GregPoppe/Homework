// from data.js
var tableData = data;

// YOUR CODE HERE!

var tbody = d3.select("#ufo-table");

var count = 0;

function tablePopulate() {
  tableData.forEach(row => {
    var newrow = tbody.append('tr');
    tbody.attr("class", "table table-striped");
    console.log(row.datetime, currentDate);
    if (row.datetime == currentDate) {
      count = count + 1;
      console.log(currentDate);
      newrow.append('td').text(row.datetime);
      newrow.append('td').text(row.city);
      newrow.append('td').text(row.state);
      newrow.append('td').text(row.country);
      newrow.append('td').text(row.shape);
      newrow.append('td').text(row.durationMinutes);
      newrow.append('td').text(row.comments);

      
    }
  })
  
};





  if (count == 0){tbody.append('td').text("Sorry, no results");

  }


// Select date filter value
var currentDate = ""
var dateSelected = d3.select('.form-control');
var buttonclicked = d3.select('#filter-btn');

function dateClick() {
 // d3.event.preventDefault();
  currentDate = d3.event.target.value;
  console.log('Setting ',currentDate);
  tablePopulate();


}


function filterclick() {
  d3.event.preventDefault();
   console.log('Setting ',currentDate);
 
 }
 

dateSelected.on("change", dateClick);
buttonclicked.on("change", filterclick);

tablePopulate();



