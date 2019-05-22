/*

var data = canvas.toDataURL("image/png");
var img = new Image();
img.src = data;
$( "body" ).append( img );
*/

function create_snapshot(renderer){
    var data = renderer.domElement.toDataURL("image/png");
    var img = new Image();
    img.src = data;
    $( "body" ).append( img );
}