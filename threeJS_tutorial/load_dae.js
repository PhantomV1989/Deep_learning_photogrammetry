var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var camera = new THREE.PerspectiveCamera( 45, window.innerWidth / window.innerHeight, 1, 500 );
camera.position.set( 0, 0, 10 );
camera.lookAt( 0, 0, 0 );
var controls = new THREE.OrbitControls(camera);

var scene = new THREE.Scene();

var elf;

var loadingManager = new THREE.LoadingManager(()=>{
    scene.add(elf);
});

var loader = new THREE.ColladaLoader( loadingManager );
loader.load( './3.dae', function ( collada ) {
    elf = collada.scene;
} );


function animate() {
    requestAnimationFrame( animate );
    controls.update();
    renderer.render( scene, camera );
}
animate();

