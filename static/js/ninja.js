// Init variables here
var ninja_data = null;

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

      // Redirect the user to the results page
      var time = setTimeout(function() {
         window.location = "/ninja/" + data["uuid"];
      }, 1500);
   });
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
