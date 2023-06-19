function print() {
    const delay = ms => new Promise(resolve => setTimeout(resolve, ms));

banner = ["aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaa"]
welcomeMsg = ["bbbbbbbbbbbb", "bbbbbbbbbbbb", "bbbbbbbbbbbb", "bbbbbbbbbbbb"]
var before = document.getElementById("before");


setTimeout(async function() {
  await loopLines(banner, "", 80);
  loopLines(welcomeMsg, "", 80);
//    loopLines(logs, "", 80);
}, 100);

async function addLine(text, style, time) {
  var t = "";
  for (let i = 0; i < text.length; i++) {
    if (text.charAt(i) == " " && text.charAt(i + 1) == " ") {
      t += "&nbsp;&nbsp;";
      i++;
    } else {
      t += text.charAt(i);
    }
  }
  await delay(time);  // <---------------
  var next = document.createElement("p");
  next.innerHTML = t;
  next.className = style;
  before.parentNode.insertBefore(next, before);
  window.scrollTo(0, document.body.offsetHeight);
}

async function loopLines(name, style, time) {
  for (var i = 0; i < name.length; i++) {
    await addLine(name[i], style, i * time);
  }
}
}