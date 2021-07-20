var inputs = document.querySelectorAll( '#img-uploader' );
Array.prototype.forEach.call( inputs, function( input )
{
	var label	 = input.nextElementSibling,
		labelVal = label.innerHTML;
	input.addEventListener( 'change', function( e )
	{
		var fileName = '';
		fileName = e.target.value.split( '\\' ).pop();
		if( fileName )
			label.innerHTML = fileName;
		else
			label.innerHTML = labelVal;
	});
});
