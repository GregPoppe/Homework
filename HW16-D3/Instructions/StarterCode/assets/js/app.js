
var d3data;


var curX = 'poverty';
var curY = 'smokes';

var xSel = d3.select("select").property('value');
console.log(xSel);

d3.csv('assets/data/data.csv').then(data => {
  d3data = data;
  parseData();
  console.log(data);
  withD3();
});



function newchart() {
  curX = d3.select('#x').property('value');
  curY = d3.select('#y').property('value');
  console.log(curX, curY);
  withD3();
};




function parseData(){

      d3data.forEach(function(data) {
        data.income = parseFloat(data.income);
        data.smokes = parseFloat(data.smokes);
        data.healthcare = parseFloat(data.healthcare);
        data.poverty = parseFloat(data.poverty);
        data.obesity = parseFloat(data.obesity);
        data.age = parseFloat(data.age);
      });
}



function withD3() {



  var svgArea = d3.select("#scatter").select("svg");

  if (!svgArea.empty()) {
    svgArea.remove();
  }

  var svgWidth = window.innerWidth*0.5;
  var svgHeight = window.innerHeight*0.75;

  var margin = {
    top: 50,
    bottom: 50,
    right: 50,
    left: 50
  };

  var height = svgHeight - margin.top - margin.bottom;
  var width = svgWidth - margin.left - margin.right;

  // Append SVG element
  var svg = d3
    .select("#scatter")
    .append("svg")
    .attr("height", svgHeight)
    .attr("width", svgWidth);

  // Append group element
  var chartGroup = svg.append("g")
    .attr("transform", `translate(${margin.left}, ${margin.top})`);



    // create scales
    var xScale = d3.scaleLinear()
      .domain(d3.extent(d3data, d => d[curX]))
      .range([0, width]);

    var yScale = d3.scaleLinear()
      .domain(d3.extent(d3data, d => d[curY]))
      .range([height, 0]);

    // create axes
    var xAxis = d3.axisBottom(xScale)
                    .text("test");
    var yAxis = d3.axisLeft(yScale);

    // append axes
    chartGroup.append("g")
      .attr("transform", `translate(0, ${height})`)
      .text("Test")
      .call(xAxis);

    chartGroup.append("g")
      .call(yAxis);


    // append circles
    var circlesGroup = chartGroup.selectAll("circle")
      .data(d3data)
      .enter()
      .append("circle")
      .attr("cx", d => xScale(d[curX]))
      .attr("cy", d => yScale(d[curY]))
      .attr("r", "10")
      .attr("fill", "lightblue")
      .attr("stroke-width", "1")
      .attr("stroke", "grey")
      .text(function(data) {
        return data.abbr
        });


    // Step 1: Initialize Tooltip
    var toolTip = d3.tip()
      .attr("class", "d3-tip")
      .offset([80, -60])
      .html(function(d) {
        return (`State: ${d.abbr}<br>${curX}: ${d[curX]} <br>${curY}: ${d[curY]}`);
      });

    // Step 2: Create the tooltip in chartGroup.
    chartGroup.call(toolTip);

    // Step 3: Create "mouseover" event listener to display tooltip
    circlesGroup.on("mouseover", function(d) {
      toolTip.show(d, this);
    })
    // Step 4: Create "mouseout" event listener to hide tooltip
      .on("mouseout", function(d) {
        toolTip.hide(d);
      });
  
};

withD3();


d3.select(window).on("resize", makeResponsive);
