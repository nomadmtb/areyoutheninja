// Init variables here
var reveal_state = 'closed';

// Function that will toggle the view reveal window
function toggleReveal() {
   console.log("Toggling reveal window");
   if (reveal_state == 'closed') {
      $('#reveal_top').attr('id', 'reveal_top_small');
      $('#reveal_bottom').attr('id', 'reveal_bottom_small');
      $('#reveal_content').toggle('clip');
      reveal_state = 'opened';
   }else{
      $('#reveal_top_small').attr('id', 'reveal_top');
      $('#reveal_bottom_small').attr('id', 'reveal_bottom');
      $('#reveal_content').toggle('clip');
      reveal_state = 'closed';
   }
}

// Document is ready
$(function() {
   console.log("Ready");
   $("#reveal_content").toggle();
});
