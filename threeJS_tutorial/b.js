var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var camera = new THREE.PerspectiveCamera( 45, window.innerWidth / window.innerHeight, 1, 500 );
camera.position.set( 0, 0, 100 );
camera.lookAt( 0, 0, 0 );
var controls = new THREE.OrbitControls(camera);


var scene = new THREE.Scene();

//create a blue LineBasicMaterial
var material = new THREE.LineBasicMaterial( { color: 0x00ff00 } );

var geometry = new THREE.Geometry();
geometry.vertices.push(new THREE.Vector3( -10, 0, 0) );
geometry.vertices.push(new THREE.Vector3( 0, 10, 0) );
geometry.vertices.push(new THREE.Vector3( 10, 0, 0) );
var line = new THREE.Line( geometry, material );
scene.add( line );


var geometry = new THREE.SphereGeometry( 5, 32, 32 );
var material = new THREE.MeshBasicMaterial( {color: 0xffff00} );
var sphere = new THREE.Mesh( geometry, material );
scene.add( sphere );

function animate() {
    requestAnimationFrame( animate );
    controls.update();
    renderer.render( scene, camera );
}
animate();

