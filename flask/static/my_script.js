$(document).ready( function(){
$('#auto').load('/static/load.results');
refresh();
});
 
function refresh()
{
	setTimeout( function() {
	  $('#auto').load('/static/load.results').fadeIn('10000');
	  refresh();
	}, 2000);
}

