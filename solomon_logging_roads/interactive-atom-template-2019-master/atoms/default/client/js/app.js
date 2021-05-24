import * as topojson from "topojson"
import * as d3 from "d3"


var target = "#graphicContainer";

function makeMap(data2, roadies) {
    // console.log(roadies)
    console.log(data2.features[0])


	d3.select("#chartTitle").text("The Solomon Islands is covered in logging roads")

	d3.select("#subTitle").html("Half of all low-lying land is within a kilometre of a <span style='color: #ff0000'>logging road</span>")

	d3.select("#sourceText").text("| Sources: Global Witness, MapHubs")

	var isMobile;
	var windowWidth = Math.max(document.documentElement.clientWidth, window.innerWidth || 0);

	if (windowWidth < 610) {
			isMobile = true;
	}	

	if (windowWidth >= 610){
			isMobile = false;
	}

	var width = document.querySelector(target).getBoundingClientRect().width
	var height = width*0.45;					
	var margin = {top: 20, right: 10, bottom: 10, left:10};

	width = width - margin.left - margin.right,
    height = height - margin.top - margin.bottom;

	console.log("width", width)

	d3.select("#graphicContainer svg").remove();

    var svg = d3.select(target).append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .attr("id", "svg")
    .attr("overflow", "hidden");		
    
    var features = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    const g= features.append("g");
   
	var projection = d3.geoMercator()
                .center([162,-9])
                // .scale(4500)
				.scale(width*5)
				.translate([width/2,height/2]); 
			

 
	var path = d3.geoPath(projection);

    svg.append("g")
    .selectAll("path")
    .data(data2.features)
    .enter()
    .append("path")
    .attr("fill", "lightgrey")
    .attr("d", path)
    .attr("title", "solsol")

    svg.append("path")
    .datum({type:"FeatureCollection", features: roadies.features})
    .attr("d", path)
    .attr("fill", "red")
    .attr("title", "Loggers")


} 

var q = Promise.all([d3.json("<%= path %>/MERC_solomonislandsadmin.geojson"),
d3.json("<%= path %>/MERC_loggingroads.geojson")])

					.then(([countries, roads]) => {
						
						makeMap(countries, roads)
						var to=null
						var lastWidth = document.querySelector("#graphicContainer").getBoundingClientRect()
						window.addEventListener('resize', function() {
							var thisWidth = document.querySelector("#graphicContainer").getBoundingClientRect()
							if (lastWidth != thisWidth) {
								window.clearTimeout(to);
								to = window.setTimeout(function() {

										makeMap(countries, roads)

									}, 100)
									}
						})
        });

		
        