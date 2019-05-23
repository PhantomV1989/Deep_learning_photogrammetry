let renderer = new THREE.WebGLRenderer({
    preserveDrawingBuffer: true
});


renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

let camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 1, 500);
camera.position.set(10, 0, 0);
camera.lookAt(0, 0, 0);
let controls = new THREE.OrbitControls(camera);



function loadScene(path) { //path = './main.dae'
    let scene = new THREE.Scene();

    let obj;

    let loadingManager = new THREE.LoadingManager(() => {
        scene.add(obj);
    });

    let loader = new THREE.ColladaLoader(loadingManager);
    loader.load(path, function (collada) {
        obj = collada.scene;
    });

    function animate() {
        requestAnimationFrame(animate);
        controls.update();
        renderer.render(scene, camera);
    }
    animate();
}