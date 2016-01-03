// Init variables here
var ninja_data = null;
var result_template = `
<div class="modal-content">
<div class="modal-header">
<h4 class="modal-title">{{ result_message }}</h4>
</div>
<div class="modal-body" id="result_body">
<a href="{{ image_url }}" target="_blank"><img id="result_image" src="{{ image_url }}"></a>
</div>
<div class="modal-footer">
<h4>Share Your Results</h4>
<a href="/ninja/{{ uuid }}" target="_blank">Direct Link</a>
</div>
</div>
`;

// Click the test button
function testNinja() {
   console.log("Testing for ninja");

   // Set up listener to change css for result modal
   $('#resultsModal').on('show', function () {

      $(this).find('.modal-body').css({width:'auto',
         height:'auto', 
        'max-height':'100%'});
  });

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

   var dest = $("#result_wrapper");
   var formatted_data = result_template.replace(/{{ result_message }}/g, data["result_message"]);
   formatted_data = formatted_data.replace(/{{ image_url }}/g, data["image_url"]);
   formatted_data = formatted_data.replace(/{{ uuid }}/g, data["uuid"]);

   console.log(formatted_data);

   dest.html(formatted_data);

   // Create the margin-left for the image if the width is < 570px
   var img_width = $('#result_image').width();
   console.log(img_width);

   // Disable the button in the view.
   $("#test_btn").attr('disabled', 'true');

   // Wait for the data to load before showing results
   var time = setTimeout(function() {
      // Turn off modal
      $('#myModal').modal('hide');
      // Toggle the content
      $('#resultsModal').modal();
   }, 1500);
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

      var time = setTimeout(function() {
         toggleMessage();
      }, 950);

   }else{
      console.log("No initial message(s)");
      $('#messages').hide();
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
      }, 4500);
   });
}

// Function that will handle all of the ninja_past stuff
function ninjaPast() {
   $("#resultsModal").modal();
   $("#test_btn").attr('disabled', 'true');
}

// Document is ready
$(function() {
   console.log("Ready");
   checkInitialMessage();

   // We only want this to run if the "#ninja_past exists"
   if ($("#ninja_past").length) {
      ninjaPast();
   }else{
      // Else, enable the button
      $("#test_btn").click(testNinja);
   }
});
