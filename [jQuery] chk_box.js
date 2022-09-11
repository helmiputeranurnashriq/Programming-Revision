// How to enable button after user clicked a checkbox
// in jQuery 
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
