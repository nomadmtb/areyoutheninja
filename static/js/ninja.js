// Init variables here
var reveal_state = 'closed';
var ninja_data = null;

var data_template = `
<div id="result">
<h2 id="title_{{ is_ninja }}">{{ is_ninja }}</h2>
<p>{{ message }}</p>
<img src="{{ image }}">
</div>
`;

// Function that will toggle the view reveal window
function toggleReveal() {
   console.log("Toggling reveal window");
   if (reveal_state == 'closed') {
      $('#reveal_top').animate({height: "75px"});
      $('#reveal_bottom').animate({height: "75px"});
      $('#reveal_content').toggle('clip');
      reveal_state = 'opened';
   }else{
      $('#reveal_top').animate({height: "300px"});
      $('#reveal_bottom').animate({height: "300px"});
      $('#reveal_content').toggle('clip');
      reveal_state = 'closed';
   }
}

// Click the test button
function testNinja() {
   console.log("Testing for ninja");

   // Turn on the modal
   $('#myModal').modal('show');

   // Get the data from the api endpoint
   $.get("/api/isninja", function(data) {
      ninja_data = data;
      console.log(ninja_data);

      // Apply the new data to the view
      applyData(data);
   });
}

// Function to apply the data to the view after load
function applyData(data) {
   console.log("Applying data to the view");

   var dest = $("#reveal_content");
   var formatted_data = data_template.replace(/{{ is_ninja }}/g, data["is_ninja"]);
   formatted_data = formatted_data.replace(/{{ message }}/g, data["message"]);
   formatted_data = formatted_data.replace(/{{ image }}/g, data["image"]);

   console.log(formatted_data);

   $("#reveal_content").html(formatted_data);

   // Disable the button in the view.
   $("#test_btn").attr('disabled', 'true');

   // Wait for the data to load before showing results
   var time = setTimeout(function() {
      // Turn off modal
      $('#myModal').modal('hide');
      // Toggle the content
      toggleReveal();
   }, 3000);
}

// Document is ready
$(function() {
   console.log("Ready");
   $("#reveal_content").toggle();
   $("#test_btn").click(testNinja);
});
