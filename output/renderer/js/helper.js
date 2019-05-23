/*

var data = canvas.toDataURL("image/png");
var img = new Image();
img.src = data;
$( "body" ).append( img );
*/

function create_snapshot(renderer) {
    var data = renderer.domElement.toDataURL("image/png");
    var img = new Image();
    img.src = data;
    $("body").append(img);
}

function random_rotate_camera_about_target(camera, r) { //random_rotate_camera_about_target(camera, 10)
    let xy = get_random_angle(),
        yz = get_random_angle();

    //start from 0,0,0
    let x = r,
        y = 0,
        z = 0;

    //xy is on xy plane    
    x = r * Math.cos(to_rad(xy)); //cos against x
    y = r * Math.sin(to_rad(xy)); //sin against y

    //yz is on yz plane
    let k = Math.cos(to_rad(yz)); //angle increases towards z, both x,y are shortened by k times
    x *= k;
    y *= k;
    z = r * Math.sin(to_rad(yz));

    camera.position.set(x, y, z);

    return [xy, yz];
}

function get_random_angle() {
    return Math.round(Math.random() * 360);
}

function to_rad(ang) {
    return ang / 360 * 2 * Math.PI;
}