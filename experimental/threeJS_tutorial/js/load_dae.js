var renderer = new THREE.WebGLRenderer({
    preserveDrawingBuffer: true 
});


renderer.setSize( window.innerWidth, window.innerHeight);
document.body.appendChild( renderer.domElement );

var camera = new THREE.PerspectiveCamera( 45, window.innerWidth / window.innerHeight, 1, 500 );
camera.position.set( 0, 0, 3 );
camera.lookAt( 0, 0, 0 );
var controls = new THREE.OrbitControls(camera);

var scene = new THREE.Scene();

var elf;

var loadingManager = new THREE.LoadingManager(()=>{
    scene.add(elf);
});

var loader = new THREE.ColladaLoader( loadingManager );
loader.load( './dae/5.dae', function ( collada ) {
    elf = collada.scene;
} );


function animate() {
    requestAnimationFrame( animate );
    controls.update();
    renderer.render( scene, camera );
}
animate();

