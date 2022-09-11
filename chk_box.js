// Enable button after user clicked a checkbox
// jQuery 
$(document).ready(function(){
    $('button').prop('disabled', true);
    $('input[type="checkbox"]').click(function() {
        if($(this).prop("checked") == true) {
            $('button').prop('disabled', false);
        }
        else{
            $('button').prop('disabled', true);
        }
      });
});``