// Init variables here
var reveal_state = 'closed';
var ninja_data = null;

var data_template = `
<div id="result">
<h2 id="title_{{ is_ninja }}">{{ is_ninja_title }}</h2>
<a href="{{ image }}" target="_blank"><img src="{{ image }}"></a>
<p>{{ message }}</p>
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

   // Hide the title message
   $('#result h2').hide();

   // Hide the message
   $('#result p').hide();

   // Show the title message
   var time = setTimeout(function() {
      $('#result h2').slideToggle(750, "easeOutBounce");
   }, 1500);

   // Show the message
   var time = setTimeout(function() {
      $('#result p').slideToggle(1000, "easeOutBounce");
   }, 2500);
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
   formatted_data = formatted_data.replace(/{{ is_ninja_title }}/g, data["is_ninja"] ? "You are a ninja" : "You are not a ninja");
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
   }, 2500);
}

// Function that will dynamically add a message to the view
function addMessage(message_txt) {

   // Set the contents
   $('#messages').html("<p class='notice'>" + message_txt + "</p>");

   // Toggle the message
   toggleMessage();

}

// Function that will toggle the initial message if it exists
function checkInitialMessage() {

   if ($(".notice").length) {
      console.log("Initial message detected");

      // Hide message immediately
      $("#messages").hide();

      toggleMessage();

   }else{
      console.log("No initial message(s)");
   }
}

// Function that will show, hide, and delete the message
function toggleMessage() {

   $('#messages').hide();

   $('#messages').slideToggle("slow", function() {
      var time = setTimeout(function() {
         $("#messages").slideToggle("slow", function() {
            $(".notice").remove();
         });
      }, 3500);
   });
}

// Document is ready
$(function() {
   console.log("Ready");
   checkInitialMessage();
   $("#reveal_content").toggle();
   $("#test_btn").click(testNinja);
});
