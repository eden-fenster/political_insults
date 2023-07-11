function print(log) {
    // An array of lines to print
    var lines = log;

    // Function to print lines one at a time
    function printLines() {
      var outputElement = document.getElementById("output");
      var index = 0;

      function printNextLine() {
        if (index < lines.length) {
          outputElement.innerHTML += lines[index] + "<br>";
          index++;
          setTimeout(printNextLine, 1000); // Delay between lines (in milliseconds)
        }
      }

      printNextLine();
    }

    // Start printing lines when the page loads
    window.onload = printLines;
}