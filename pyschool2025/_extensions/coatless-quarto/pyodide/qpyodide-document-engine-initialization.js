// Create a logging setup
globalThis.qpyodideMessageArray = []

// Add messages to array
globalThis.qpyodideAddToOutputArray = function(message, type) {
  qpyodideMessageArray.push({ message, type });
}

// Function to reset the output array
globalThis.qpyodideResetOutputArray = function() {
  qpyodideMessageArray = [];
}

globalThis.qpyodideRetrieveOutput = function() {
  return qpyodideMessageArray.map(entry => entry.message).join('\n');
}

// Start a timer
const initializePyodideTimerStart = performance.now();

// Encase with a dynamic import statement
globalThis.qpyodideInstance = await import(
  qpyodideCustomizedPyodideOptions.indexURL + "pyodide.mjs").then(
   async({ loadPyodide }) => {

    console.log("Start loading Pyodide");
    
    // Populate Pyodide options with defaults or new values based on `pyodide`` meta
    let mainPyodide = await loadPyodide(
      qpyodideCustomizedPyodideOptions
    );
    
    // Setup a namespace for global scoping
    // await loadedPyodide.runPythonAsync("globalScope = {}"); 
    
    // Update status to reflect the next stage of the procedure
    qpyodideUpdateStatusHeaderSpinner("Cargando trampas...");

    // Load the `micropip` package to allow installation of packages.
    await mainPyodide.loadPackage("micropip");
    await mainPyodide.runPythonAsync(`import micropip`);

    // Load the `pyodide_http` package to shim uses of `requests` and `urllib3`.
    // This allows for `pd.read_csv(url)` to work flawlessly.
    // Details: https://github.com/coatless-quarto/pyodide/issues/9
    qpyodideUpdateStatusHeaderSpinner("Cargando serpientes...");
    await mainPyodide.loadPackage("pyodide_http");
    await mainPyodide.runPythonAsync(`
    import pyodide_http
    pyodide_http.patch_all()  # Patch all libraries
    `);

    // Load the `matplotlib` package with necessary environment hook
    await mainPyodide.loadPackage("matplotlib");

    // Set the backend for matplotlib to be interactive.
    await mainPyodide.runPythonAsync(`
    import matplotlib
    matplotlib.use("module://matplotlib_pyodide.html5_canvas_backend")
    from matplotlib import pyplot as plt
    `);

    // Load the verification file
    await mainPyodide.runPythonAsync(`
    import urllib.request
    url = "https://raw.githubusercontent.com/fralfaro/pyschool/blob/main/pyschool2025/verificar.py"
    urllib.request.urlretrieve(url, "verificar.py");
    `);
    qpyodideUpdateStatusHeader("Cargando las habitaciones...");
     
    // Unlock interactive buttons
    qpyodideSetInteractiveButtonState(
      `<i class="fa-solid fa-play qpyodide-icon-run-code"></i> <span>Run Code</span>`, 
      true
    );

    // Set document status to viable
    qpyodideUpdateStatusHeader("🟢 Escape room listo");

    // Assign Pyodide into the global environment
    globalThis.mainPyodide = mainPyodide;

    console.log("Completed loading Pyodide");
    return mainPyodide;
  }
);

// Stop timer
const initializePyodideTimerEnd = performance.now();

// Create a function to retrieve the promise object.
globalThis._qpyodideGetInstance = function() {
    return qpyodideInstance;
}
