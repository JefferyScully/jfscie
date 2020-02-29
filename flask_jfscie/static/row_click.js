$(document).ready(function () {
    $('.clickable-row').click(function(){
	var row_id = $(this).attr('row_id');

	req = $.ajax({
	    url : '/row_click',
	    type : 'POST',
	    data : {row_id : row_id}
	});
	
	req.done(function(data){
	    console.log(data.data)
	});
    });
    
});
