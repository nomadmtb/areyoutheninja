// Init variables here
var reveal_state = 'closed';

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

// Document is ready
$(function() {
   console.log("Ready");
   $("#reveal_content").toggle();
});
